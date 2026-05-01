import matplotlib.pyplot as plt
import numpy as np

# Рисунок 1: Диаграмма QPSK
fig, ax = plt.subplots(figsize=(6,6))
points = [(1,1), (-1,1), (-1,-1), (1,-1)]
labels = ['00', '01', '11', '10']
for (x,y), label in zip(points, labels):
    ax.plot(x, y, 'bo', markersize=12)
    ax.annotate(label, (x, y), xytext=(5,5), textcoords='offset points', fontsize=14)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('I (In-phase)')
ax.set_ylabel('Q (Quadrature)')
ax.set_title('QPSK Constellation Diagram')
ax.grid(True, alpha=0.3)
plt.savefig('images/qpsk_constellation.png', dpi=150, bbox_inches='tight')
plt.close()

# Рисунок 2: Диаграмма 16-QAM
fig, ax = plt.subplots(figsize=(6,6))
I_vals = [-3, -1, 1, 3]
for I in I_vals:
    for Q in I_vals:
        ax.plot(I, Q, 'ro', markersize=8)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_xlabel('I (In-phase)')
ax.set_ylabel('Q (Quadrature)')
ax.set_title('16-QAM Constellation Diagram')
ax.grid(True, alpha=0.3)
plt.savefig('images/qam16_constellation.png', dpi=150, bbox_inches='tight')
plt.close()

print("Графики сохранены в папку images/")
