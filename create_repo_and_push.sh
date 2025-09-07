#!/bin/bash

echo "🚀 Creating krisper-vscode repository on GitHub"
echo "=============================================="
echo ""
echo "Since the repo doesn't exist yet, you need to create it first."
echo ""
echo "QUICKEST METHOD:"
echo "==============="
echo ""
echo "1. Open this link in your browser:"
echo "   https://github.com/new"
echo ""
echo "2. Fill in these EXACT values:"
echo "   Repository name: krisper-vscode"
echo "   Description: VS Code extension for KRISPER - Write code in plain English"
echo "   Public: ✓ (checked)"
echo ""
echo "3. Click 'Create repository'"
echo ""
echo "4. IMMEDIATELY come back here and press ENTER"
echo ""
read -p "Press ENTER after creating the repo on GitHub... "

echo ""
echo "Pushing your code..."
git push -u origin master

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Your code is now on GitHub!"
    echo "🌐 https://github.com/echo313unfolding/krisper-vscode"
    echo ""
    echo "You've successfully pushed:"
    echo "- KRISPER plain English programming"
    echo "- Bio_Poetica cross-language support"
    echo "- 15+ language transformations"
    echo ""
    echo "Next: Run ./publish_to_marketplace.sh"
else
    echo ""
    echo "If push failed, make sure you created the repo with the exact name: krisper-vscode"
fi