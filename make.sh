#!/bin/bash

echo "Installing dependencies..."
npm install

echo "Building Python engine..."
pip install pyinstaller
pyinstaller --onefile engine/sgs_compressor.py

echo "Done!"
echo "Run: npm start"