# KRISPER for VS Code

<p align="center">
  <img src="branding/krisper_readme_intro.svg" alt="KRISPER — English → IR → Execution" />
</p>

Write code in plain English directly in VS Code!

## Features

### 🧬 Natural Language Programming
![Demo](images/demo.gif)

Write:
```krisper
compress file "data.txt" as backup
compare backup with original
if different: alert user
```

Get executable code!

### 🎨 Bio_Poetica Poetry Support
```biopoetica
when user saves file:
    emit "autosave" {"timestamp": now}
    compress changes as backup
```

### ✨ Features
- Syntax highlighting for .ksp and .bio files
- Real-time compilation to JSON IR
- Execute directly from VS Code
- IntelliSense for common patterns
- Snippets for quick starts

## Usage

1. Create a file with `.ksp` or `.bio` extension
2. Write in plain English
3. Press `Ctrl+Shift+K` to compile
4. See the JSON output in the side panel

## Example

```krisper
// data_processor.ksp
load csv file "sales.csv" as data
filter data where amount > 1000 as high_value
sort high_value by date descending
export high_value to "report.json"
```

## Installation

1. Install from VS Code Marketplace: search "KRISPER"
2. Or install manually: `code --install-extension krisper-0.1.0.vsix`

## Requirements

- VS Code 1.74.0+
- Python 3.8+ (for execution)

## Commands

- `KRISPER: Compile Current File` - Convert natural language to IR
- `KRISPER: Execute Current File` - Run the compiled code
- `KRISPER: Explain Selection` - Explain what selected code does
- `KRISPER: Open Quickstart` - Open a sample file
- `KRISPER: Toggle Inline Completions` - Toggle KRISPER suggestions

## Keybindings

- `Ctrl+Shift+K` / `Cmd+Shift+K` - Compile current file
- `Ctrl+Shift+Enter` / `Cmd+Shift+Enter` - Execute current file
- `Ctrl+Shift+.` / `Cmd+Shift+.` - Explain selection

## Copilot Compatibility
KRISPER plays nicely with GitHub Copilot.

Enable Copilot for our languages:

```json
{
  "github.copilot.enable": {
    "*": true,
    "krisper": true,
    "biopoetica": true
  },
  "github.copilot.editor.enableAutoCompletions": true
}
```

Use **KRISPER: Toggle Inline Completions** to switch our tiny scaffolds on/off. We let Copilot take the lead; KRISPER adds low-noise verb scaffolds and one-shot commands (Quickstart, Compile, Execute).

## Coming Soon

- Live preview panel
- Debugging support
- More language patterns
- GitHub Copilot integration

---

Part of the [KRISPER](https://github.com/echo313unfolding/KRISPER) natural language programming project.