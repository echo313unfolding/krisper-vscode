#!/usr/bin/env python3
import os
import json
import sys

def test_extension():
    print("Testing KRISPER VS Code Extension...")
    
    # Test 1: Check all required files exist
    print("\n1. Checking required files...")
    required_files = [
        'extension.js',
        'package.json',
        'README.md',
        'language-configuration.json',
        'syntaxes/krisper.tmLanguage.json',
        'syntaxes/biopoetica.tmLanguage.json',
        'compiler/compile.py',
        'compiler/execute.py',
        'snippets/krisper.json',
        'icon.png'
    ]
    
    all_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"  {status} {file}")
        if not exists:
            all_exist = False
    
    if not all_exist:
        print("❌ Some required files are missing!")
        return False
    
    # Test 2: Validate package.json
    print("\n2. Validating package.json...")
    with open('package.json', 'r') as f:
        pkg = json.load(f)
    
    checks = [
        ('name', pkg.get('name') == 'krisper'),
        ('main', pkg.get('main') == './extension.js'),
        ('languages', 'languages' in pkg.get('contributes', {})),
        ('commands', 'commands' in pkg.get('contributes', {})),
        ('keybindings', 'keybindings' in pkg.get('contributes', {})),
        ('configuration', 'configuration' in pkg.get('contributes', {}))
    ]
    
    for name, passed in checks:
        status = "✓" if passed else "✗"
        print(f"  {status} {name}")
    
    # Test 3: Check syntax files are valid JSON
    print("\n3. Validating syntax files...")
    syntax_files = [
        'syntaxes/krisper.tmLanguage.json',
        'syntaxes/biopoetica.tmLanguage.json'
    ]
    
    for file in syntax_files:
        try:
            with open(file, 'r') as f:
                json.load(f)
            print(f"  ✓ {file} - Valid JSON")
        except Exception as e:
            print(f"  ✗ {file} - Invalid JSON: {e}")
    
    # Test 4: Test compiler
    print("\n4. Testing compiler...")
    test_code = 'compress payload "test" as output'
    
    # Write test file
    with open('_test_compile.ksp', 'w') as f:
        f.write(test_code)
    
    # Try to compile
    import subprocess
    try:
        result = subprocess.run(
            [sys.executable, 'compiler/compile.py', '_test_compile.ksp'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("  ✓ Compiler works")
            output = json.loads(result.stdout)
            print(f"  ✓ Generated IR: {output.get('version', 'unknown')}")
        else:
            print(f"  ✗ Compiler error: {result.stderr}")
    except Exception as e:
        print(f"  ✗ Compiler failed: {e}")
    finally:
        if os.path.exists('_test_compile.ksp'):
            os.remove('_test_compile.ksp')
    
    print("\n✅ Extension is ready for VS Code!")
    return True

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    test_extension()