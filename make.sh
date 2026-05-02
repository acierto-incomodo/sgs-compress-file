#!/bin/bash

echo "📦 Installing Node deps..."
npm install

echo "🐍 Building Python engine..."
pip install pyinstaller
pyinstaller --onefile engine/sgs_compressor.py

echo "🚀 Building Electron app..."
npm run dist

echo "✅ DONE!"