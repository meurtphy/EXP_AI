class AgentNumerique:
    def __init__(self):
        """
        Initialise un modèle interne des nombres.
        Il comprend que chaque nombre est un ensemble d'unités et que les nombres sont reliés par des relations mathématiques.
        """
        self.nombres = self.initialiser_nombres()

    def initialiser_nombres(self):
        """ Crée une structure interne qui représente les nombres comme des ensembles d'unités. """
        nombres = {}
        for i in range(101):
            nombres[i] = list(range(1, i+1))  # Ex : 5 devient [1, 2, 3, 4, 5]
        return nombres

    def visualiser_nombre(self, n):
        """ Retourne une représentation visuelle du nombre (ex: '🟢🟢🟢🟢🟢' pour 5). """
        return "🟢" * n

    def decomposer_nombre(self, n):
        """ Retourne toutes les façons de décomposer un nombre en deux parties. """
        decompositions = [(i, n-i) for i in range(1, n)]
        return decompositions

    def additionner(self, a, b):
        """
        Additionne deux nombres en manipulant directement leurs unités.
        - Il récupère les objets de `a`
        - Il ajoute les objets de `b`
        - Il vérifie si le total correspond à un nombre existant
        """
        total = len(self.nombres[a]) + len(self.nombres[b])
        return total if total in self.nombres else None
