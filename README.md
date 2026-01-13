# LaTeX-Vorlage für wissenschaftliche Abschlussarbeiten

Diese Vorlage bietet ein professionelles LaTeX-Setup für Bachelor- und Masterarbeiten im deutschsprachigen Raum. Sie ist nach akademischen und typografischen Konventionen optimiert und besonders für MINT-Themen geeignet.

### 📄 [Vollständige Beispiel-Thesis ansehen (PDF)](Thesis.pdf)

![Vorschau des Layouts](screenshot.jpg)

> **📝 Artikel-Template verfügbar!**  
> Für kürzere Seminararbeiten oder populärwissenschaftliche Artikel gibt es den Branch [`referat-template`](../../tree/referat-template) mit einem zweispaltigen Artikel-Layout (~10 Seiten).
>
> ```bash
> # Zum Artikel-Template wechseln:
> git checkout referat-template
>
> # Zurück zur Thesis-Vorlage:
> git checkout main
> ```
>
> ⚠️ **Nicht mergen!** Die Branches sind eigenständige Templates und sollten nicht zusammengeführt werden.

## Inhaltsverzeichnis

1. [Features](#features)
2. [Voraussetzungen](#voraussetzungen)
3. [Schnelleinstieg](#schnelleinstieg)
4. [Kompilierung](#kompilierung)
5. [Verwendung](#verwendung)
6. [Projektstruktur](#projektstruktur)
7. [Häufige Anpassungen](#häufige-anpassungen)
8. [Troubleshooting](#troubleshooting)
9. [Lizenz](#lizenz)

## Features

- **Vorkonfiguriertes Layout:** Optimiert für Abschlussarbeiten (Bachelor/Master) mit KOMA-Script (`scrreprt`).
- **Typografie:** Sauberer Satzspiegel, deutsche Typografie (ngerman) oder Englisch.
- **Struktur:** Modulare Kapitel in `content/`, saubere Trennung von Inhalt und Layout.
- **MINT-Support:** Optimiert für Bilder, Tabellen, Code-Listings und TikZ.
- **Automatisierung:** `build.sh` Skript für einfache Kompilierung.
- **KI-Deklaration:** Vorbereitete Vorlagen für die Deklaration von KI-Hilfsmitteln (gemäß DFG-Empfehlungen).

## Voraussetzungen

- **LaTeX-Distribution:**
  - macOS: MacTeX (`brew install --cask mactex-no-gui`)
  - Windows: MiKTeX oder TeX Live
  - Linux: TeX Live (`sudo apt install texlive-full`)
- **Editor (Empfohlen):** VS Code mit der Extension **LaTeX Workshop**.
- **Tools:** `biber` (für Literaturverzeichnisse, meist in TeX Live enthalten).

## Schnelleinstieg

### 1. Projekt herunterladen

Mit Git:
```bash
git clone https://github.com/kqc-real/thesis-template.git
cd thesis-template
```

Alternativ: Als ZIP herunterladen und entpacken.

### 2. In VS Code öffnen

1. VS Code starten.
2. `Datei` → `Ordner öffnen...` → `thesis-template` auswählen.
3. Die Datei `Thesis.tex` öffnen.

## Kompilierung

### Automatisch (Empfohlen)

Das Skript `build.sh` automatisiert die notwendigen Schritte (pdflatex → biber → pdflatex), um Querverweise und das Literaturverzeichnis korrekt zu erstellen.

#### Optionen
- `./build.sh`: Standard-Kompilierung.
- `./build.sh clean`: Entfernt temporäre Dateien (build/, *.aux, *.log usw.).

*Falls das Skript nicht ausführbar ist:*
```bash
chmod +x build.sh
./build.sh
```

### Manuell

Falls das Skript nicht genutzt werden kann, führen Sie folgende Befehle nacheinander aus:

```bash
pdflatex Thesis.tex
biber Thesis
pdflatex Thesis.tex
pdflatex Thesis.tex
```

## Verwendung

### Metadaten anpassen

Öffnen Sie `Thesis.tex` und passen Sie die Variablen am Anfang der Datei an:

```tex
% Metadaten der Arbeit
\author{Max Mustermann}
\studentID{1234567}
\studentAddress{Musterstraße 1, 12345 Musterstadt}
\thesis{Bachelor-Thesis}
\title{Titel der Arbeit}
\academicTitle{Bachelor of Science}
\firstReferee{Prof. Dr. A. Müller}
\secondReferee{Prof. Dr. B. Schmidt}
```

### Inhalt schreiben

Der Inhalt liegt im Ordner `content/`. Jedes Kapitel hat eine eigene `.tex`-Datei (z. B. `01_Einfuehrung.tex`).
Diese werden in `Thesis.tex` mittels `\input{content/...}` eingebunden.

### Bilder einfügen

Bilder im Ordner `images/` ablegen:

```tex
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.8\textwidth]{images/diagramm.png}
  \caption{Beschriftung des Diagramms}
  \label{fig:diagramm}
\end{figure}
```

### Tabellen einfügen

Für einfache Tabellen verwenden Sie die Standard-LaTeX-Syntax mit `booktabs`:

```tex
\begin{table}[ht]
  \centering
  \begin{tabular}{lcc}
    \toprule
    Name & Wert A & Wert B \\
    \midrule
    Zeile 1 & 10 & 20 \\
    Zeile 2 & 15 & 25 \\
    \bottomrule
  \end{tabular}
  \caption{Beschreibung der Tabelle}
  \label{tab:beispiel}
\end{table}
```

> **Tipp:** Für längere Tabellen oder mehrseitige Übersichten steht `longtable` zur Verfügung. Weitere LaTeX-Tabellen-Anleitungen finden Sie in der [Overleaf-Dokumentation](https://www.overleaf.com/learn/latex/Tables).

### Literatur zitieren

1. Literaturquellen in `bib/BibtexDatabase.bib` im BibTeX-Format eintragen.
2. Im Text zitieren: `\cite{key}` oder `\textcite{key}`.

## Projektstruktur

```text
thesis-template/
├── Thesis.tex          # Hauptdatei (Einstiegspunkt)
├── Thesis.pdf          # Beispiel-Ausgabe
├── build.sh            # Kompilierungs- und Clean-Skript
├── content/            # Inhalt (Kapitel)
├── preambel/           # LaTeX-Einstellungen & Pakete
├── bib/                # Literaturdatenbank (.bib)
├── images/             # Abbildungen
├── macros/             # Eigene Makros/Befehle
└── docs_KI_GENERIERT/  # KI-generierte Zusatzmaterialien (siehe unten)
```

## KI-generierte Zusatzmaterialien

Im Ordner `docs_KI_GENERIERT/` finden Sie mit KI-Tools (Gamma, NotebookLM) erstellte Beispielmaterialien:

- **LaTeX-Präsentation:** Einführung in LaTeX für Anfänger
- **Thesis-Präsentation:** Beispiel für Verteidigung/Kolloquium
- **Poster & Mind-Map:** Visualisierungen für Konferenzen
- **Audio-/Video-Podcast:** Zusammenfassungen der Thesis

Diese Materialien dienen als Inspiration für die Vorbereitung Ihrer eigenen Präsentation. Details finden Sie in der [README des Ordners](docs_KI_GENERIERT/README.md).

## Häufige Anpassungen

- **Sprache ändern:** In `Thesis.tex` die Zeile `\def\lang{ngerman}` zu `\def\lang{english}` ändern.
- **Schriftart:** In `preambel/Fonts.tex` können alternative Schriftarten (z. B. Palatino, Times) aktiviert werden.

## Troubleshooting

- **Kein PDF erstellt?** Prüfen Sie die Log-Datei (`Thesis.log`) auf Fehlermeldungen.
- **Fragezeichen statt Referenzen (??)?** Führen Sie die Kompilierung mehrfach aus oder nutzen Sie `./build.sh`.
- **Literatur fehlt?** Stellen Sie sicher, dass `biber` ausgeführt wurde.
- **Fehler `Undefined control sequence`:** Meist ein Tippfehler in einem Befehl oder ein fehlendes Paket.

## Lizenz

MIT License — siehe LICENSE.
