from random import randint


# constantes propres aux entités

MATURITY_AGE = 100
MAX_ALIENS = 50
GRID_WIDTH = 80
GRID_HEIGHT = 80


class Predator:
    population = [] # variable de classe pour stocker tous les prédateurs

    @classmethod
    def update_all(cls): # MAJ de tous les prédateurs
        for predator in cls.population:
            predator.update()

    def __init__(self, x, y): # tout bête
        self.x = x
        self.y = y
        Predator.population.append(self)

    def update(self): # voilà ce que fait un prédateur
        self.move()
        self.predate()

    def move(self):
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)
        self.x = min(max(0, self.x), GRID_WIDTH - 1)
        self.y = min(max(0, self.y), GRID_HEIGHT - 1)

    def predate(self): # bien regarder comment on gère la disparition des Aliens
        casualties = []
        for i in range(len(Alien.population)):
            if abs(self.x - Alien.population[i].x) + abs(self.y - Alien.population[i].y) < 5:
                casualties.append(i)
        Alien.kill(casualties) # on a la liste des Aliens à tuer, on la passe à la méthode de classe Alien.kill


class Alien:
    population = []

    @classmethod
    def kill(cls, casualties): # pour gérer les morts
        new_population = []
        for i in range(len(Alien.population)):
            if i not in casualties:
                new_population.append(Alien.population[i])
        Alien.population = new_population

    @classmethod
    def update_all(cls): # pareil que pour les prédateurs en plus compliqué

        new_individuals = []
        for i in range(len(cls.population)):
            cls.population[i].update() # chaque Alien est MAJ

            # Ensuite on regarde ceux qui sont matures et proches pour les faire se reproduire
            if len(cls.population) < MAX_ALIENS:
                if cls.population[i].maturity == MATURITY_AGE:
                    for j in range(i + 1, len(cls.population)):
                        if cls.population[j].maturity == MATURITY_AGE:
                            if abs(cls.population[i].x - cls.population[j].x) + abs(
                                    cls.population[i].y - cls.population[j].y) < 4:
                                new_individuals.append((i, j)) # on utilise une nouvelle liste pour ne pas
                                # << bousiller >> celle sur laquelle on boucle

            for (i, j) in new_individuals:
                if len(cls.population) < MAX_ALIENS:
                    cls.population[i] + cls.population[j] # et c'est là qu'on la change, à la fin.

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.maturity = 0
        Alien.population.append(self)

    def update(self):
        self.move()
        self.age()

    def move(self):
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)
        self.x = min(max(0, self.x), GRID_WIDTH - 1)
        self.y = min(max(0, self.y), GRID_HEIGHT - 1)

    def age(self):
        self.maturity += 1
        self.maturity = min(self.maturity, MATURITY_AGE)

    def __add__(self, other): # surcharge de << + >> qui permet de faire a1 + a2 --> un petit bébé alien trop mignon !
        self.maturity = 0
        other.maturity = 0
        return Alien((self.x + other.x) // 2, (self.y + other.y) // 2)
