class AgentPhysique:
    def __init__(self):
        """
        Initialise un modèle où les nombres sont des ensembles d'objets.
        L'IA voit les nombres comme des collections d'unités qu'elle peut manipuler.
        """
        self.nombres = self.initialiser_nombres()

    def initialiser_nombres(self):
        """ Crée une structure interne où chaque nombre est représenté par des unités (billes, points). """
        nombres = {}
        for i in range(101):  # On commence avec les nombres de 0 à 100
            nombres[i] = ["🟢"] * i  # Ex : 5 devient ['🟢', '🟢', '🟢', '🟢', '🟢']
        return nombres

    def visualiser_nombre(self, n):
        """ Retourne une représentation visuelle du nombre (ex: '🟢🟢🟢🟢🟢' pour 5). """
        if n in self.nombres:
            return "".join(self.nombres[n])
        return "Nombre inconnu"

    def additionner(self, a, b):
        """
        Additionne deux nombres en manipulant directement leurs unités.
        L'IA ne fait pas un calcul, elle ajoute simplement des objets.
        """
        if a in self.nombres and b in self.nombres:
            total = self.nombres[a] + self.nombres[b]  # Empile les objets des deux nombres
            return len(total)  # Le résultat est la longueur totale des objets empilés
        return None  # Si l'un des nombres est inconnu, on ne peut pas additionner

    def soustraire(self, a, b):
        """
        Soustrait un nombre d'un autre en enlevant des unités.
        """
        if a in self.nombres and b in self.nombres and len(self.nombres[a]) >= len(self.nombres[b]):
            total = self.nombres[a][:len(self.nombres[a]) - len(self.nombres[b])]  # On enlève les objets de b
            return len(total)
        return None  # Si la soustraction est impossible, on retourne None
