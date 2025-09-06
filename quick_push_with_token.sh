#!/bin/bash

echo "🚀 Quick Push with GitHub Token"
echo "==============================="
echo ""
echo "Enter your GitHub Personal Access Token"
echo "(Get one from: https://github.com/settings/tokens/new)"
echo "Required scopes: repo"
echo ""
read -sp "Token: " TOKEN
echo ""

# Push with token
git push https://$TOKEN@github.com/echo313unfolding/krisper-vscode.git master

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Pushed to GitHub!"
    echo "📍 https://github.com/echo313unfolding/krisper-vscode"
    echo ""
    echo "Next: ./publish_to_marketplace.sh"
else
    echo "❌ Push failed. Check your token and try again."
fi