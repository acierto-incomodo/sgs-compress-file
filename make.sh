#!/bin/bash

echo "🔧 Instalando dependencias..."
pip install -r requirements.txt

echo "🧹 Limpiando builds anteriores..."
rm -rf build dist __pycache__ *.spec

echo "🚀 Compilando..."

pyinstaller \
  --onefile \
  --noconsole \
  --name sgs_compressor \
  sgs_compressor.py

echo "✅ Build completado!"
echo "📁 Ejecutable en: dist/sgs_compressor"