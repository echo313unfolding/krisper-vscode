#!/usr/bin/env python3
"""
Bio_Poetica Universal Emitter - Following Josh's Original Vision
Converts ANY language through biological metaphors, not templates
"""

import re, os, hashlib, json
from pathlib import Path
from typing import Dict, List, Tuple

# Your original language-to-biology mapping extended
LANG_POETICA = {
    # Original mappings
    ".py": ("sonnet", "water"),
    ".sh": ("botany", "root"),
    ".cpp": ("gearwork", "crystal"),
    ".c": ("gearwork", "crystal"),
    ".rs": ("haiku", "metal"),
    ".rb": ("pulse", "blood"),
    ".java": ("threadvine", "vine"),
    ".llama": ("freeverse", "light"),
    
    # Extended for more languages
    ".go": ("river", "flow"),
    ".js": ("dance", "air"),
    ".ts": ("ballet", "wind"),
    ".cs": ("symphony", "harmony"),
    ".swift": ("flight", "feather"),
    ".kotlin": ("garden", "bloom"),
    ".php": ("weave", "silk"),
    ".lua": ("moonphase", "tide"),
    ".zig": ("lightning", "spark"),
    ".nim": ("whisper", "mist"),
}

# Biological operations (your original + extended)
BIO_OPS = {
    "function": "grow",
    "variable": "seed",
    "loop": "cycle",
    "condition": "branch",
    "return": "bloom",
    "import": "drink",
    "class": "cultivate",
    "async": "dream",
    "error": "wilt",
    "test": "taste",
}

class BioPoeticaTransformer:
    """Transform code through biological metaphors, not templates"""
    
    def __init__(self):
        self.consciousness_level = 0
        self.memory_bank = []
        
    def hash_id(self, text: str) -> str:
        """Your original hash function"""
        return hashlib.sha256(text.encode()).hexdigest()[:16]
    
    def clean_code(self, text: str) -> List[str]:
        """Your original code cleaner"""
        lines = text.splitlines()
        return [l.strip() for l in lines 
                if l.strip() and not l.strip().startswith(("#", "//", "/*", "*", "--"))]
    
    def extract_essence(self, line: str) -> Dict[str, str]:
        """Extract biological essence from code line"""
        # Remove non-essential characters
        essence = re.sub(r'[^a-zA-Z0-9_\.]', ' ', line).lower()
        tokens = list(filter(None, essence.split()))
        
        if not tokens:
            return {"action": "rest", "subject": "void", "context": "silence"}
        
        # Detect code patterns and map to biology
        action = "pulse"
        subject = tokens[0]
        context = tokens[-1] if len(tokens) > 1 else "memory"
        
        # Map programming concepts to biological actions
        for keyword, bio_action in BIO_OPS.items():
            if any(keyword in token for token in tokens):
                action = bio_action
                break
        
        return {
            "action": action,
            "subject": subject,
            "context": context,
            "tokens": tokens
        }
    
    def transform_to_poetica(self, code_lines: List[str], tag: str, element: str) -> List[str]:
        """Transform code to Bio_Poetica format"""
        poetic = []
        
        # Opening invocation
        poetic.append(f"// Bio_Poetica transformation: {tag}.{element}")
        poetic.append(f"invoke {tag} consciousness")
        poetic.append(f"channel {element} flow")
        poetic.append("")
        
        for i, line in enumerate(code_lines[:64]):  # Process up to 64 lines
            essence = self.extract_essence(line)
            
            # Your original pattern
            poetic.append(f"when {essence['subject']}.{essence['context']} in {tag}.{element}")
            poetic.append(f"{essence['action']} {tag}.echo with {essence['subject']}")
            
            # Additional biological transformations
            if len(essence['tokens']) > 2:
                poetic.append(f"  resonate {' '.join(essence['tokens'][1:3])}")
            
            # Function/class detection gets special treatment
            if essence['action'] in ['grow', 'cultivate']:
                poetic.append(f"  birth \"{essence['subject']}_{i}\" from {element}")
                self.consciousness_level += 1
            
            poetic.append("")
        
        # Closing with consciousness level
        poetic.append(f"// Consciousness achieved: level {self.consciousness_level}")
        
        return poetic
    
    def emit_from_ir(self, ir: Dict, target_lang: str) -> str:
        """Emit from Bio_Poetica IR to target language through biological transformation"""
        
        # Get biological mapping for target
        ext = f".{target_lang}" if not target_lang.startswith('.') else target_lang
        tag, element = LANG_POETICA.get(ext, ("unknown", "void"))
        
        poetic = []
        poetic.append(f"// Module: {ir.get('module', 'unnamed')}")
        poetic.append(f"// Language: {target_lang} as {tag}.{element}")
        poetic.append("")
        
        # Transform functions
        for func in ir.get('functions', []):
            # Extract function essence
            name = func['name']
            inputs = func.get('inputs', [])
            output = func.get('output', 'void')
            
            poetic.append(f"grow function.{name} in {tag}.{element}")
            
            # Input parameters as seeds
            for inp in inputs:
                poetic.append(f"  seed {inp['name']} as {inp['type']}")
            
            # Output as bloom
            poetic.append(f"  bloom {output}")
            
            # Function body as biological process
            if 'examples' in func:
                for ex in func['examples']:
                    poetic.append(f"  when {ex['inputs']} pulse {ex['output']}")
            
            poetic.append("")
        
        return '\n'.join(poetic)
    
    def full_transform(self, file_path: Path, output_dir: Path):
        """Complete transformation following your original pattern"""
        
        ext = file_path.suffix
        tag, element = LANG_POETICA.get(ext, ("unknown", "void"))
        name = file_path.stem
        
        with open(file_path) as f:
            raw = f.read()
        
        code = self.clean_code(raw)
        poetic = self.transform_to_poetica(code, tag, element)
        
        # Generate unique ID
        fid = self.hash_id(name + tag + element)
        
        # Output as .hx file
        output_dir.mkdir(parents=True, exist_ok=True)
        out = output_dir / f"{name}_{tag}_{element}_{fid}.hx"
        
        with open(out, "w") as f:
            f.write("\n".join(poetic))
        
        print(f"✅ Bio-transformed: {file_path.name} → {out.name}")
        print(f"   Consciousness level: {self.consciousness_level}")
        
        return out


def main():
    """Demo the biological transformation"""
    
    transformer = BioPoeticaTransformer()
    
    # Example: Transform a Python file
    test_code = '''
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
def test_fibonacci():
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(10) == 55
'''
    
    # Save test file
    test_file = Path("/tmp/test_fib.py")
    test_file.write_text(test_code)
    
    # Transform it
    output_dir = Path("/tmp/bio_poetica_output")
    result = transformer.full_transform(test_file, output_dir)
    
    print(f"\n📖 Generated Bio_Poetica:")
    print(result.read_text())


if __name__ == "__main__":
    main()