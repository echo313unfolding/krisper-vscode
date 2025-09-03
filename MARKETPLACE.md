# KRISPER - Natural Language Programming

Write code in English. KRISPER plays nice with Copilot.

## Overview

KRISPER brings natural language programming to VS Code. Type your intent in plain English and watch it transform into executable code.

### Key Features

✅ **Natural Language to Code** - Write `compress file "data.txt" as backup` instead of complex syntax  
✅ **GitHub Copilot Compatible** - Works seamlessly alongside Copilot suggestions  
✅ **Instant Compilation** - Press `Ctrl+Shift+K` to see your IR  
✅ **One-Click Execution** - Run your KRISPER code with `Ctrl+Shift+Enter`  
✅ **Poetry Mode** - Bio_Poetica support for artistic code expression

### Quick Example

```krisper
// KRISPER DSL: each line is an action
compress payload "Hello World" using seed=42 as greeting
compare greeting with expected_value
export greeting to "output.json"
```

### Commands

- **KRISPER: Open Quickstart** - Get started in seconds
- **KRISPER: Compile Current File** - See the JSON IR (`Ctrl+Shift+K`)
- **KRISPER: Execute Current File** - Run your code (`Ctrl+Shift+Enter`)
- **KRISPER: Explain Selection** - Understand what code does (`Ctrl+Shift+.`)
- **KRISPER: Toggle Inline Completions** - Control suggestion behavior

### Installation

1. Install the extension
2. Set environment (if needed):
   ```bash
   export KRISPER_REPO="/path/to/krisper"
   export KRISPER_PYTHON="python3"
   ```
3. Open any `.ksp` or `.bio` file
4. Start writing in English!

### Why KRISPER?

- **Zero Learning Curve** - If you can write a sentence, you can code
- **Copilot-Friendly** - Designed to enhance, not replace, AI assistance
- **Executable Specs** - Your documentation IS the code
- **Open Source** - Join us on [GitHub](https://github.com/echo313unfolding/KRISPER)

### Support

- [Documentation](https://github.com/echo313unfolding/KRISPER)
- [Issues](https://github.com/echo313unfolding/krisper-vscode/issues)
- [Examples](https://github.com/echo313unfolding/KRISPER/tree/main/examples)

---

*Part of the Echo Labs natural language computing initiative*