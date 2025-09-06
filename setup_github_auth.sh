#!/bin/bash

echo "🔐 Setting up GitHub Authentication"
echo "==================================="
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "📦 Installing GitHub CLI..."
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
    sudo apt update
    sudo apt install gh -y
fi

echo ""
echo "🔑 Authenticating with GitHub..."
echo "You'll be asked to:"
echo "1. Choose 'GitHub.com'"
echo "2. Choose 'HTTPS'"
echo "3. Authenticate with browser or token"
echo ""

gh auth login

echo ""
echo "✅ Authentication complete! Now pushing..."
echo ""

# Create and push the repo
gh repo create echo313unfolding/krisper-vscode \
    --public \
    --description "VS Code extension for KRISPER - Write code in plain English" \
    --source=. \
    --push

echo ""
echo "🎉 Success! Your VS Code extension is now on GitHub!"
echo "📍 URL: https://github.com/echo313unfolding/krisper-vscode"
echo ""
echo "Next step: Run ./publish_to_marketplace.sh"