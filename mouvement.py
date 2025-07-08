import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fonction position : s(t) = 2t³ - 15t² + 24t - 5
def position(t):
    return 2 * t**3 - 15 * t**2 + 24 * t - 5

# Fonction vitesse : v(t) = s'(t) = 6t² - 30t + 24
def velocity(t):
    return 6 * t**2 - 30 * t + 24

# Fonction accélération : a(t) = v'(t) = 12t - 30
def acceleration(t):
    return 12 * t - 30

# Configuration de l'animation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
fig.suptitle('Animation d\'une mouche en mouvement rectiligne\ns(t) = 2t³ - 15t² + 24t - 5', 
             fontsize=16, fontweight='bold')

# Paramètres temporels
t_max = 5.0
dt = 0.05
t_values = np.arange(0, t_max + dt, dt)

# Calcul des valeurs pour les graphiques
positions = [position(t) for t in t_values]
velocities = [velocity(t) for t in t_values]
accelerations = [acceleration(t) for t in t_values]

# Configuration du graphique principal (mouvement)
ax1.set_xlim(-25, 15)
ax1.set_ylim(-1, 1)
ax1.set_xlabel('Position (unités)')
ax1.set_ylabel('')
ax1.set_title('Mouvement de la mouche')
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', linewidth=1)

# Ligne de référence et graduations
for i in range(-15, 21, 5):
    ax1.axvline(x=i, color='gray', linewidth=0.5, alpha=0.5)
    ax1.text(i, -0.8, str(i), ha='center', va='center', fontsize=10)

# Éléments animés
fly, = ax1.plot([], [], 'ro', markersize=12, label='Mouche')
trail, = ax1.plot([], [], 'r-', alpha=0.3, linewidth=2, label='Trajectoire')
time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes, fontsize=12,
                     verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
info_text = ax1.text(0.02, 0.02, '', transform=ax1.transAxes, fontsize=10,
                     verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

ax1.legend(loc='upper right')

# Configuration du graphique des courbes
ax2.set_xlim(0, t_max)
ax2.set_ylim(min(min(positions), min(velocities), min(accelerations)) - 5, 
             max(max(positions), max(velocities), max(accelerations)) + 5)
ax2.set_xlabel('Temps (s)')
ax2.set_ylabel('Valeur')
ax2.set_title('Position, Vitesse et Accélération en fonction du temps')
ax2.grid(True, alpha=0.3)

# Courbes complètes
ax2.plot(t_values, positions, 'b-', label='Position s(t)', linewidth=2)
ax2.plot(t_values, velocities, 'g-', label='Vitesse v(t)', linewidth=2)
ax2.plot(t_values, accelerations, 'r-', label='Accélération a(t)', linewidth=2)

# Points animés sur les courbes
pos_point, = ax2.plot([], [], 'bo', markersize=8)
vel_point, = ax2.plot([], [], 'go', markersize=8)
acc_point, = ax2.plot([], [], 'ro', markersize=8)
time_line = ax2.axvline(x=0, color='black', linestyle='--', alpha=0.7)

ax2.legend(loc='upper right')

# Listes pour stocker la trajectoire
trail_positions = []
trail_y = []

def animate(frame):
    t = frame * dt
    
    if t > t_max:
        t = t_max
    
    # Position actuelle de la mouche
    current_pos = position(t)
    current_vel = velocity(t)
    current_acc = acceleration(t)
    
    # Mise à jour de la mouche
    fly.set_data([current_pos], [0])
    
    # Mise à jour de la trajectoire (traînée)
    trail_positions.append(current_pos)
    trail_y.append(0)
    if len(trail_positions) > 50:  # Limiter la longueur de la traînée
        trail_positions.pop(0)
        trail_y.pop(0)
    trail.set_data(trail_positions, trail_y)
    
    # Mise à jour des textes
    time_text.set_text(f'Temps: {t:.2f} s')
    info_text.set_text(f'Position: {current_pos:.2f}\nVitesse: {current_vel:.2f}\nAccélération: {current_acc:.2f}')
    
    # Mise à jour des points sur les courbes
    pos_point.set_data([t], [current_pos])
    vel_point.set_data([t], [current_vel])
    acc_point.set_data([t], [current_acc])
    time_line.set_xdata([t, t])
    
    return fly, trail, time_text, info_text, pos_point, vel_point, acc_point, time_line

# Création de l'animation
anim = animation.FuncAnimation(fig, animate, frames=int(t_max/dt), 
                             interval=100, blit=True, repeat=True)

# Ajustement de la mise en page
plt.tight_layout()

# Affichage
plt.show()

