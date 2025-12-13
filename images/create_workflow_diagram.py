#!/usr/bin/env python3
"""
Erstellt ein Workflow-Diagramm für agentische Systeme.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Figure erstellen
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Farben
color_start = '#4CAF50'
color_process = '#2196F3'
color_decision = '#FF9800'
color_end = '#F44336'

def draw_box(ax, x, y, w, h, text, color, style='round'):
    """Zeichnet eine Box mit Text."""
    if style == 'round':
        box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                             boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor='black',
                             linewidth=2)
    elif style == 'diamond':
        # Raute für Entscheidungen
        points = [(x, y+h/2), (x+w/2, y), (x, y-h/2), (x-w/2, y)]
        box = patches.Polygon(points, facecolor=color,
                            edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center',
           fontsize=10, weight='bold', color='white',
           wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, label=''):
    """Zeichnet einen Pfeil."""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=20,
                           linewidth=2, color='black')
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
        ax.text(mid_x+0.5, mid_y, label, fontsize=9,
               bbox=dict(boxstyle='round', facecolor='white',
                        edgecolor='gray'))

# Workflow-Schritte
draw_box(ax, 5, 13, 2.5, 0.8, 'Start:\nZiel empfangen', color_start)
draw_arrow(ax, 5, 12.6, 5, 11.8)

draw_box(ax, 5, 11.3, 2.5, 0.8, 'Sense:\nZustand erfassen', color_process)
draw_arrow(ax, 5, 10.9, 5, 10.1)

draw_box(ax, 5, 9.6, 2.5, 0.8, 'Plan:\nSchritte planen', color_process)
draw_arrow(ax, 5, 9.2, 5, 8.4)

draw_box(ax, 5, 7.9, 2.5, 0.8, 'Action:\nTool ausführen', color_process)
draw_arrow(ax, 5, 7.5, 5, 6.7)

draw_box(ax, 5, 6.2, 2.5, 0.8, 'Observation:\nOutput verarbeiten', color_process)
draw_arrow(ax, 5, 5.8, 5, 5.0)

draw_box(ax, 5, 4.5, 2.5, 0.8, 'Reflect:\nBewerten', color_process)
draw_arrow(ax, 5, 4.1, 5, 3.3)

# Entscheidung
draw_box(ax, 5, 2.6, 2, 1.2, 'Ziel\nerreicht?', color_decision, style='diamond')

# Pfade
draw_arrow(ax, 4.0, 2.6, 1.5, 7.9, 'Nein')  # Zurück zu Action
draw_arrow(ax, 5, 2.0, 5, 1.2, 'Ja')

draw_box(ax, 5, 0.6, 2.5, 0.8, 'Ende:\nErgebnis ausgeben', color_end)

# Seitennotizen
ax.text(8.5, 11.3, 'Episodisches\nGedächtnis', fontsize=9,
       bbox=dict(boxstyle='round', facecolor='lightyellow',
                edgecolor='gray'))
ax.text(8.5, 7.9, 'Tool Registry\n& Adapter', fontsize=9,
       bbox=dict(boxstyle='round', facecolor='lightblue',
                edgecolor='gray'))
ax.text(8.5, 4.5, 'Self-Critique\nMechanismus', fontsize=9,
       bbox=dict(boxstyle='round', facecolor='lightgreen',
                edgecolor='gray'))

# Pfeile zu Notizen
ax.plot([6.25, 7.5], [11.3, 11.3], 'k--', linewidth=1, alpha=0.5)
ax.plot([6.25, 7.5], [7.9, 7.9], 'k--', linewidth=1, alpha=0.5)
ax.plot([6.25, 7.5], [4.5, 4.5], 'k--', linewidth=1, alpha=0.5)

# Titel
ax.text(5, 13.8, 'Agentischer Workflow-Zyklus', ha='center',
       fontsize=14, weight='bold')

plt.tight_layout()
plt.savefig('/Users/kqc/thesis-template/images/agent-workflow.png',
           dpi=300, bbox_inches='tight', facecolor='white')
print("Workflow-Diagramm erstellt: agent-workflow.png")
