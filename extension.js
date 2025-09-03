const vscode = require('vscode');
const { execFile } = require('child_process');
const path = require('path');
const fs = require('fs');

let statusItem;

function getRepoRoot() {
  // adjust if your KRISPER repo lives elsewhere
  const candidates = [
    path.join(__dirname, '..', 'krisper_github'),
    path.join(__dirname, '..', '..', 'krisper_github'),
    process.env.KRISPER_REPO || ''
  ].filter(Boolean);
  for (const p of candidates) if (fs.existsSync(p)) return p;
  return null;
}

function runPy(scriptAbs, args = [], cwd) {
  const python = process.env.KRISPER_PYTHON || 'python3';
  return new Promise((resolve, reject) => {
    const ps = execFile(python, [scriptAbs, ...args], { cwd });
    let out = '', err = '';
    ps.stdout.on('data', d => (out += String(d)));
    ps.stderr.on('data', d => (err += String(d)));
    ps.on('close', code => code === 0 ? resolve(out) : reject(new Error(err || `exit ${code}`)));
  });
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
}

function inline(text) { return { insertText: text }; }

function activate(context) {
  const cfg = () => vscode.workspace.getConfiguration('krisper');
  let inlineEnabled = cfg().get('inline.enabled', true);

  // status bar toggle
  statusItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 10);
  const refresh = () => {
    statusItem.text = inlineEnabled ? 'KRISPER ✦' : 'KRISPER ⭘';
    statusItem.tooltip = 'Toggle KRISPER inline completions';
  };
  statusItem.command = 'krisper.toggleInline';
  refresh(); statusItem.show();
  context.subscriptions.push(statusItem);

  context.subscriptions.push(vscode.commands.registerCommand('krisper.toggleInline', async () => {
    inlineEnabled = !inlineEnabled;
    await vscode.workspace.getConfiguration('krisper').update('inline.enabled', inlineEnabled, true);
    refresh();
  }));

  // compile → IR
  context.subscriptions.push(vscode.commands.registerCommand('krisper.compileCurrent', async () => {
    const doc = vscode.window.activeTextEditor?.document; if (!doc) return;
    await doc.save();
    const root = getRepoRoot();
    if (!root) return vscode.window.showErrorMessage('KRISPER repo not found. Set KRISPER_REPO or place krisper_github next to the extension.');
    const script = path.join(root, 'compiler', 'compile.py');
    try {
      const out = await runPy(script, [doc.fileName], root);
      const panel = vscode.window.createWebviewPanel('krisperIR', 'KRISPER IR', vscode.ViewColumn.Beside, {});
      panel.webview.html = `<pre>${escapeHtml(out)}</pre>`;
      vscode.window.showInformationMessage('Compiled to IR');
    } catch (e) { vscode.window.showErrorMessage(`Compile failed: ${e.message}`); }
  }));

  // execute plan
  context.subscriptions.push(vscode.commands.registerCommand('krisper.executeCurrent', async () => {
    const doc = vscode.window.activeTextEditor?.document; if (!doc) return;
    await doc.save();
    const root = getRepoRoot();
    if (!root) return vscode.window.showErrorMessage('KRISPER repo not found.');
    const script = path.join(root, 'compiler', 'execute.py');
    try {
      const out = await runPy(script, [doc.fileName], root);
      const panel = vscode.window.createWebviewPanel('krisperRun', 'KRISPER Run Log', vscode.ViewColumn.Beside, {});
      panel.webview.html = `<pre>${escapeHtml(out)}</pre>`;
      vscode.window.showInformationMessage('KRISPER execution complete');
    } catch (e) { vscode.window.showErrorMessage(`Execution failed: ${e.message}`); }
  }));

  // explain selection (offline)
  context.subscriptions.push(vscode.commands.registerCommand('krisper.explainSelection', async () => {
    const ed = vscode.window.activeTextEditor; if (!ed) return;
    const sel = ed.document.getText(ed.selection) || ed.document.getText();
    const bullets = sel.split(/\r?\n/).filter(Boolean).map(l => `• ${escapeHtml(l)}`).join('<br>');
    const panel = vscode.window.createWebviewPanel('krisperExplain', 'KRISPER Explain', vscode.ViewColumn.Beside, {});
    panel.webview.html = `<h2>KRISPER Intent → Steps</h2><hr>${bullets}<hr><small>Tip: Copilot is enabled for KRISPER/Bio_Poetica.</small>`;
  }));

  // gentle keyword suggestions (let Copilot lead)
  const keywords = ['compress','decompress','hash','compare','export','load','filter','sort','map','reduce','when','emit','flow','bloom','spiral','grow'];
  context.subscriptions.push(
    vscode.languages.registerCompletionItemProvider(
      [{ language: 'krisper' }, { language: 'biopoetica' }],
      {
        provideCompletionItems(doc, pos) {
          const tok = doc.lineAt(pos.line).text.slice(0, pos.character).trim().split(/\s+/).pop() || '';
          if (!/^[a-z]{2,7}$/i.test(tok)) return; // be conservative to avoid noise
          return keywords.map(k => {
            const it = new vscode.CompletionItem(k, vscode.CompletionItemKind.Keyword);
            it.insertText = k + ' ';
            it.sortText = 'z' + k; // Copilot gets priority
            return it;
          });
        }
      },
      ...'abcdefghijklmnopqrstuvwxyz'.split('')
    )
  );

  // tiny inline scaffold (off by toggle, minimal to avoid Copilot conflict)
  context.subscriptions.push(
    vscode.languages.registerInlineCompletionItemProvider(
      [{ language: 'krisper' }, { language: 'biopoetica' }],
      {
        provideInlineCompletionItems(doc, pos) {
          if (!inlineEnabled) return;
          const line = doc.getText(new vscode.Range(new vscode.Position(pos.line, 0), pos)).trim();
          const items = [];
          if (/^compress\b/i.test(line)) items.push(inline(`compress payload "Hello, World!" using seed=42 as greeting`));
          if (/^compare\b/i.test(line))  items.push(inline(`compare greeting with expected_value`));
          if (/^export\b/i.test(line))   items.push(inline(`export greeting to "output.json"`));
          if (/^when\b/i.test(line))     items.push(inline(`when user clicks button:\n    emit "sparkle" {"color":"gold"}\n    grow happiness by 10`));
          return { items };
        }
      }
    )
  );

  // quickstart
  context.subscriptions.push(vscode.commands.registerCommand('krisper.quickstart', async () => {
    const sample = `// KRISPER Quickstart
compress payload "Hello, World!" using seed=42 as greeting
hash greeting as checksum
compare greeting with expected_value
export greeting to "output.json"
`;
    const doc = await vscode.workspace.openTextDocument({ language: 'krisper', content: sample });
    vscode.window.showTextDocument(doc);
  }));
}

function deactivate() {}
module.exports = { activate, deactivate };