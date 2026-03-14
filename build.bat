@echo off
echo Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller

echo Building FoodBridge.exe...
pyinstaller FoodBridge.spec --clean --noconfirm

echo Done! Your .exe is in the dist/ folder.
pause
