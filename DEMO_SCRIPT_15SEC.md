# KRISPER 15-Second Demo Script (Shot-by-Shot)

**Recording Setup:**
- Resolution: 1280×720
- FPS: 60fps
- VS Code dark theme
- Cursor visible
- GitHub Copilot enabled
- KRISPER extension loaded

## Timeline

### 0.0s – 1.5s
- Open VS Code, new file **`hello.ksp`** (empty)
- Add caption overlay: *"KRISPER: English → IR → Execution (Copilot-friendly)"*

### 1.5s – 6.0s (type slowly)
Type exactly:
```
compress payload "Hello, World!" using seed=42 as greeting
```
- Let viewers read as you type
- Pause briefly to show both KRISPER hint and Copilot ghost text

### 6.0s – 8.5s
- Press **Ctrl+Shift+K**
- IR webview opens on the right
- Move mouse to highlight "KRISPER IR" panel title

### 8.5s – 11.5s
- Press **Ctrl+Shift+Enter**
- Run Log panel shows:
  - ✓ compress: success
  - ✓ hash: complete
  - ✓ compare: true
  - ✓ export: saved

### 11.5s – 13.5s
- Click status bar **"KRISPER ✦"** → changes to **"⭘"**
- Click again → back to **"✦"**
- Shows inline hints can be toggled while keeping Copilot active

### 13.5s – 15.0s
- New line, type:
```
when user clicks button:
```
- Let Copilot/KRISPER propose the completion
- Freeze on suggestions for 0.5s
- End with KRISPER logo fade

## Recording Commands

### Using OBS Studio:
```bash
# Scene setup:
# - Window Capture: VS Code
# - Text overlay for caption
# - 1280x720 canvas
# - 60 FPS
```

### Using asciinema + agg:
```bash
asciinema rec krisper-demo.cast
# perform demo
# Ctrl+D to stop
agg krisper-demo.cast krisper-demo.gif
```

### Using VS Code's built-in:
- `Ctrl+Shift+P` → "Developer: Toggle Screencast Mode"
- Shows keypresses on screen