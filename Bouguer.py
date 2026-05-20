from turtle import Turtle, Screen
from math import sqrt

# ============================================================
# Simulation du problème de Bouguer : la courbe du chien
# ============================================================
#
# Une personne part du point (x0, 0) et monte verticalement
# à vitesse constante Vp.
#
# Un chien part de (0, 0), court à vitesse constante Vc,
# et se dirige à chaque instant vers la position actuelle
# de la personne.
#
# Si Vc > Vp, le chien finit par rattraper la personne.
# La théorie prévoit un point de rattrapage :
#
#       y = n*x0/(1 - n^2), où n = Vp/Vc.
#
# ============================================================


# -----------------------------
# Paramètres du problème
# -----------------------------

x0 = 300              # position horizontale initiale de la personne
Vp = 1.0              # vitesse de la personne
Vc = 2.0              # vitesse du chien

dt = 0.5              # pas de temps
capture_distance = 3  # distance à partir de laquelle on considère que le chien a rattrapé la personne

n = Vp / Vc

if Vc <= Vp:
    print("Attention : le chien ne court pas plus vite que la personne.")
    print("La poursuite ne se terminera pas nécessairement.")
else:
    y_theorique = n * x0 / (1 - n**2)
    print("=== Données du problème ===")
    print(f"x0 = {x0}")
    print(f"Vp = {Vp}")
    print(f"Vc = {Vc}")
    print(f"n = Vp/Vc = {n}")
    print()
    print("=== Résultat théorique ===")
    print(f"Hauteur théorique de rattrapage : y = {y_theorique:.2f}")
    print()


# -----------------------------
# Mise en place de l'écran
# -----------------------------

screen = Screen()
screen.title("La courbe du chien - problème de Bouguer")
screen.setup(width=900, height=700)
screen.tracer(0)

# -----------------------------
# Création des tortues
# -----------------------------

chien = Turtle()
personne = Turtle()
texte = Turtle()
axe = Turtle()

chien.shape("turtle")
personne.shape("circle")

chien.color("red")
personne.color("blue")

chien.penup()
personne.penup()

chien.goto(0, 0)
personne.goto(x0, 0)

chien.pendown()
personne.pendown()

chien.width(3)
personne.width(3)

texte.hideturtle()
texte.penup()
texte.goto(-420, 300)

axe.hideturtle()
axe.speed(0)
axe.penup()


# -----------------------------
# Dessin des axes
# -----------------------------

axe.goto(-400, 0)
axe.pendown()
axe.goto(400, 0)
axe.penup()

axe.goto(0, -300)
axe.pendown()
axe.goto(0, 320)
axe.penup()

axe.goto(x0, -300)
axe.pendown()
axe.goto(x0, 320)
axe.penup()


# -----------------------------
# Simulation
# -----------------------------

t = 0.0
distance = 10**9
iteration = 0
max_iterations = 10000

while distance > capture_distance and iteration < max_iterations:

    # Positions actuelles
    xc, yc = chien.position()
    xp, yp = personne.position()

    # Vecteur allant du chien vers la personne
    dx = xp - xc
    dy = yp - yc

    distance = sqrt(dx**2 + dy**2)

    # Direction unitaire du chien vers la personne
    ux = dx / distance
    uy = dy / distance

    # Déplacement du chien pendant dt
    chien.goto(xc + Vc * dt * ux, yc + Vc * dt * uy)

    # Déplacement vertical de la personne pendant dt
    personne.goto(xp, yp + Vp * dt)

    # Temps
    t += dt
    iteration += 1

    # Affichage dynamique
    if iteration % 10 == 0:
        texte.clear()
        texte.write(
            f"Temps : {t:.1f}\n"
            f"Distance chien-personne : {distance:.2f}\n"
            f"Position personne : ({xp:.1f}, {yp:.1f})\n"
            f"Position chien : ({xc:.1f}, {yc:.1f})",
            font=("Arial", 12, "normal")
        )

    screen.update()


# -----------------------------
# Résultats
# -----------------------------

xc, yc = chien.position()
xp, yp = personne.position()

texte.clear()

if iteration >= max_iterations:
    texte.write(
        "La simulation s'est arrêtée car le nombre maximal d'itérations a été atteint.\n"
        "Le chien n'a pas rattrapé la personne dans le temps imparti.",
        font=("Arial", 12, "normal")
    )
else:
    texte.write(
        "Rattrapage !\n\n"
        f"Temps de rattrapage approximatif : {t:.2f}\n"
        f"Position finale du chien : ({xc:.2f}, {yc:.2f})\n"
        f"Position finale de la personne : ({xp:.2f}, {yp:.2f})\n\n"
        f"Hauteur théorique : {y_theorique:.2f}\n"
        f"Hauteur simulée : {yp:.2f}\n"
        f"Erreur absolue : {abs(yp - y_theorique):.2f}",
        font=("Arial", 12, "normal")
    )

    print("=== Résultat de la simulation ===")
    print(f"Temps de rattrapage approximatif : {t:.2f}")
    print(f"Position finale du chien : ({xc:.2f}, {yc:.2f})")
    print(f"Position finale de la personne : ({xp:.2f}, {yp:.2f})")
    print()
    print("=== Comparaison théorie / simulation ===")
    print(f"Hauteur théorique : {y_theorique:.2f}")
    print(f"Hauteur simulée : {yp:.2f}")
    print(f"Erreur absolue : {abs(yp - y_theorique):.2f}")


screen.update()
screen.exitonclick()
