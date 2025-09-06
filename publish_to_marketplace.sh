#!/bin/bash
# Publish KRISPER to VS Code Marketplace

echo "📦 Publishing KRISPER to VS Code Marketplace"
echo "==========================================="

# Check if vsce is installed
if ! command -v vsce &> /dev/null; then
    echo "Installing vsce..."
    npm install -g @vscode/vsce
fi

echo ""
echo "Step 1: Create publisher account"
echo "--------------------------------"
echo "1. Go to: https://marketplace.visualstudio.com/manage"
echo "2. Sign in with Microsoft account"
echo "3. Create publisher ID: 'echo-labs' (or 'echo313unfolding')"
echo "4. Get Personal Access Token from: https://dev.azure.com"
echo ""
echo "Step 2: Package the extension"
echo "-----------------------------"
vsce package

echo ""
echo "Step 3: Publish to marketplace"
echo "------------------------------"
echo "Run: vsce publish"
echo "(You'll be prompted for your Personal Access Token)"
echo ""
echo "Alternative: Publish via web"
echo "---------------------------"
echo "1. Go to: https://marketplace.visualstudio.com/manage"
echo "2. Upload the .vsix file created by 'vsce package'"
echo ""
echo "🎯 After publishing, share these links:"
echo "- Marketplace: https://marketplace.visualstudio.com/items?itemName=echo-labs.krisper"
echo "- Install: ext install echo-labs.krisper"