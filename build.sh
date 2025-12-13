#!/bin/bash
set -e

# Name der Hauptdatei (ohne .tex Endung)
MAIN="Thesis"

echo "🚀 Starte Build-Prozess für $MAIN..."

# 1. Initialer LaTeX-Lauf (erstellt .aux, .toc, etc.)
pdflatex "$MAIN.tex"

# 2. Literaturverzeichnis verarbeiten
biber "$MAIN"

# 3. Verzeichnisse und Referenzen aktualisieren
pdflatex "$MAIN.tex"

# 4. Finaler Lauf für korrekte Seitenzahlen und Verweise
pdflatex "$MAIN.tex"

echo "✅ Build erfolgreich! $MAIN.pdf wurde erstellt."