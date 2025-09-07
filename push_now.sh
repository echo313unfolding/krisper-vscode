#!/bin/bash

echo "🚀 DIRECT PUSH TO GITHUB"
echo "======================="
echo ""
echo "Enter your GitHub username (likely: echo313unfolding):"
read -p "Username: " USERNAME
echo ""
echo "Enter your GitHub Personal Access Token"
echo "(The same one you used for KRISPER repo)"
echo "Token will be hidden as you type:"
read -sp "Token: " TOKEN
echo ""
echo ""

# Create the repository via API first
echo "Creating repository..."
curl -H "Authorization: token $TOKEN" \
     -d '{"name":"krisper-vscode","description":"VS Code extension for KRISPER - Write code in plain English","public":true}' \
     https://api.github.com/user/repos

echo ""
echo "Pushing code..."

# Push using token
git push https://$USERNAME:$TOKEN@github.com/$USERNAME/krisper-vscode.git master

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS! Your VS Code extension is now live!"
    echo "📍 https://github.com/$USERNAME/krisper-vscode"
    echo ""
    echo "Next steps:"
    echo "1. Run: ./publish_to_marketplace.sh"
    echo "2. Share using: ./LAUNCH_POSTS.md"
else
    echo "❌ Push failed. Please check your credentials."
fi