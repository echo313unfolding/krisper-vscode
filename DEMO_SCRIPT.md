# KRISPER 15-Second Demo Script

## Recording Setup
- VS Code with KRISPER extension installed
- Dark theme
- Font size 16+
- Terminal at bottom (25% height)

## Script (15 seconds)

**0:00-0:02** - Open VS Code, show empty `.ksp` file

**0:02-0:05** - Type:
```
compress payload "Hello KRISPER!" as message
```
(Show both KRISPER hint AND Copilot suggestion appearing)

**0:05-0:08** - Press `Ctrl+Shift+K`
- Compile panel opens on right
- Shows JSON IR

**0:08-0:11** - Press `Ctrl+Shift+Enter`  
- Execute panel opens
- Shows "✓ compress: success"

**0:11-0:14** - Click status bar "KRISPER ✦"
- Toggle to "KRISPER ⭘"
- Type `compare` - only Copilot suggests now

**0:14-0:15** - End card: "KRISPER + Copilot = 🚀"

## Alternative: Longer Demo (30 seconds)

Add:
- Bio_Poetica poetry example
- Multiple operations chained
- File I/O demonstration

## Recording Tools
```bash
# Option 1: asciinema
asciinema rec krisper-demo.cast
# Convert to GIF with agg

# Option 2: VS Code built-in
Ctrl+Shift+P → "Developer: Toggle Screencast Mode"

# Option 3: OBS Studio
# Best quality, more control
```