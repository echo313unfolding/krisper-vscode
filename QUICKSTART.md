# KRISPER VS Code Extension - Quick Start Guide

## 5-Minute Local Test

```bash
# From krisper-vscode directory
npm install
code --extensionDevelopmentPath="$(pwd)"
```

## In VS Code:

1. **Open Quickstart**: `Ctrl+Shift+P` → "KRISPER: Open Quickstart"
2. **Try inline hints**: Type `compress` → see KRISPER scaffold + Copilot suggestions
3. **Compile**: `Ctrl+Shift+K` → Opens IR panel
4. **Execute**: `Ctrl+Shift+Enter` → Opens run log panel
5. **Toggle inline**: Click "KRISPER ✦/⭘" in status bar

## Environment Setup

If KRISPER repo is outside the extension folder:

```bash
export KRISPER_REPO="/home/voidstr3m33/krisper_github"
export KRISPER_PYTHON="$(which python3)"
```

## Package & Publish

```bash
npm i -g vsce
vsce package
vsce publish  # needs PAT configured
```

## PR Highlights

✅ Works seamlessly with GitHub Copilot  
✅ One-keystroke Quickstart, Compile, Execute  
✅ Gentle inline hints that don't interfere  
✅ All offline/deterministic (reviewer-friendly)