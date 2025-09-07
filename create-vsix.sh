#!/bin/bash

echo "📦 Creating KRISPER VSIX package manually..."

# Create a clean copy
rm -rf vsix_temp
mkdir vsix_temp
cp -r * vsix_temp/ 2>/dev/null || true
cd vsix_temp

# Remove unnecessary files
rm -rf node_modules .git *.sh .gitignore vsix_temp

# Create the VSIX (which is just a ZIP)
zip -r ../krisper-0.1.0.vsix . -x "*.vsix"

cd ..
rm -rf vsix_temp

echo "✅ Created krisper-0.1.0.vsix"
echo ""
echo "📤 To publish:"
echo "1. Go to: https://marketplace.visualstudio.com/manage"
echo "2. Sign in and create publisher 'echo-labs'"
echo "3. Upload the krisper-0.1.0.vsix file"
echo ""
echo "Or install locally with:"
echo "code --install-extension krisper-0.1.0.vsix"