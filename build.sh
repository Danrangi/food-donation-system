#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt
pip install pyinstaller

echo "Building FoodBridge executable..."
pyinstaller FoodBridge.spec --clean --noconfirm

echo "Done! Your executable is in the dist/ folder."
