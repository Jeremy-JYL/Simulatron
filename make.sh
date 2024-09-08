pyinstaller --onefile --collect-all Simulatron ./emulator.py
pyinstaller --onefile ./assembler/assembler.py

rm -rf build
rm *.spec
