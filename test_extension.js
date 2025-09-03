// Test the VS Code extension basics
const path = require('path');
const assert = require('assert');

// Test 1: Extension can be loaded
console.log('Testing extension loading...');
const ext = require('./extension.js');
assert(typeof ext.activate === 'function', 'Extension must export activate function');
assert(typeof ext.deactivate === 'function', 'Extension must export deactivate function');
console.log('✓ Extension structure valid');

// Test 2: Language files exist
console.log('\nTesting language files...');
const fs = require('fs');
assert(fs.existsSync('./syntaxes/krisper.tmLanguage.json'), 'KRISPER syntax file must exist');
assert(fs.existsSync('./syntaxes/biopoetica.tmLanguage.json'), 'Bio_Poetica syntax file must exist');
assert(fs.existsSync('./language-configuration.json'), 'Language config must exist');
console.log('✓ Language files present');

// Test 3: Package.json is valid
console.log('\nTesting package.json...');
const pkg = require('./package.json');
assert(pkg.name === 'krisper', 'Package name must be krisper');
assert(pkg.main === './extension.js', 'Main must point to extension.js');
assert(Array.isArray(pkg.contributes.languages), 'Must contribute languages');
assert(Array.isArray(pkg.contributes.commands), 'Must contribute commands');
console.log('✓ Package.json valid');

// Test 4: Compiler scripts exist
console.log('\nTesting compiler integration...');
assert(fs.existsSync('./compiler/compile.py'), 'Compile script must exist');
assert(fs.existsSync('./compiler/execute.py'), 'Execute script must exist');
console.log('✓ Compiler scripts present');

console.log('\n✅ All tests passed! Extension is ready.');