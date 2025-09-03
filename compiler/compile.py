#!/usr/bin/env python3
import sys
import os
import json

# Try multiple paths to find krisper
possible_paths = [
    os.path.join(os.path.dirname(__file__), '..', '..', '..', 'krisper_github'),
    os.path.join(os.path.expanduser('~'), 'krisper_github'),
    os.environ.get('KRISPER_REPO', '')
]

for path in possible_paths:
    if path and os.path.exists(path):
        sys.path.insert(0, path)
        break

def main():
    if len(sys.argv) < 2:
        print("Usage: compile.py <file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        if filepath.endswith('.bio') or filepath.endswith('.poem'):
            from bio_poetica import BioPoeticaCompiler
            compiler = BioPoeticaCompiler()
            result = compiler.compile_poem(content)
        else:  # .ksp or .krisper
            from krisper import compile_text
            result = compile_text(content)
            if isinstance(result, str):
                result = json.loads(result)
        
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Compilation error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()