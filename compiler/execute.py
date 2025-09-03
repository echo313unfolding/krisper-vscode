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

from executors.basic_executor import BasicExecutor
from executors.file_executor import FileExecutor
from executors.compression_executor import CompressionExecutor

def main():
    if len(sys.argv) < 2:
        print("Usage: execute.py <file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    try:
        # First compile
        with open(filepath, 'r') as f:
            content = f.read()
        
        if filepath.endswith('.bio') or filepath.endswith('.poem'):
            from bio_poetica import BioPoeticaCompiler
            compiler = BioPoeticaCompiler()
            ir = compiler.compile_poem(content)
        else:
            from krisper import compile_text
            result = compile_text(content)
            ir = json.loads(result) if isinstance(result, str) else result
        
        # Then execute
        executors = [BasicExecutor(), FileExecutor(), CompressionExecutor()]
        
        print(f"Executing {os.path.basename(filepath)}...")
        print("-" * 50)
        
        if 'plan' in ir:
            for op in ir['plan']:
                executed = False
                for executor in executors:
                    if executor.can_execute(op):
                        result = executor.execute(op)
                        print(f"✓ {op['op']}: {result}")
                        executed = True
                        break
                
                if not executed:
                    print(f"✗ {op['op']}: No executor available")
        else:
            print("No execution plan found")
        
    except Exception as e:
        print(f"Execution error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()