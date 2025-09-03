<p align="center">
  <img src="branding/krisper_readme_intro.svg" alt="KRISPER — English → IR → Execution" />
</p>

# KRISPER — Natural Language Programming (Copilot-friendly)

Write programs in **plain English**. No brackets. No boilerplate.  
KRISPER turns intent into a small IR and executes it locally.  
Works **alongside GitHub Copilot** (we keep suggestions low-noise).

## ✨ What you can do
- `compress payload "Hello" using seed=42 as greeting`
- `hash greeting as checksum`
- `compare greeting with expected_value`
- Bio_Poetica events:  
```
when user clicks button:
  emit "sparkle" {"color":"gold"}
  grow happiness by 10
```

## 🚀 Quick Start
1. Install the extension.
2. (Optional) Set env vars if your compiler lives elsewhere:
   - `KRISPER_REPO=/path/to/krisper_github`
   - `KRISPER_PYTHON=/path/to/python3`
3. **Ctrl+Shift+P → "KRISPER: Open Quickstart"**  
4. **Ctrl+Shift+K** to **Compile Current File** → IR panel  
5. **Ctrl+Shift+Enter** to **Execute Current File** → Run Log panel

## 🤝 Copilot Compatibility
KRISPER plays nice with Copilot—Copilot leads; we add tiny verb scaffolds.

Enable Copilot for our languages:
```json
{
  "github.copilot.enable": { "*": true, "krisper": true, "biopoetica": true },
  "github.copilot.editor.enableAutoCompletions": true
}
```

Toggle KRISPER's own inline hints via the status bar (**KRISPER ✦/⭘**) or command:
**"KRISPER: Toggle Inline Completions"**.

## 🧰 Commands

* **KRISPER: Open Quickstart** — insert sample
* **KRISPER: Compile Current File** — English → IR
* **KRISPER: Execute Current File** — run plan locally
* **KRISPER: Explain Selection** — readable steps
* **KRISPER: Toggle Inline Completions** — on/off

## ⌨️ Keybindings

* Compile: **Ctrl+Shift+K** / **Cmd+Shift+K**
* Execute: **Ctrl+Shift+Enter** / **Cmd+Shift+Enter**
* Explain: **Ctrl+Shift+.** / **Cmd+Shift+.**

## 📸 Screenshots

* `images/quickstart.png` — Quickstart file open
* `images/compile.png` — IR webview
* `images/execute.png` — Run Log webview
* `images/copilot.png` — Copilot + KRISPER suggestions together

## 🔒 Privacy

All compilation/execution happens locally. No external calls.

## 🗺️ Roadmap

* Verb hover docs (rich examples)
* Diagnostics & quick fixes for unknown verbs
* Live preview panel

---

Part of the [KRISPER](https://github.com/echo313unfolding/KRISPER) natural language programming project.