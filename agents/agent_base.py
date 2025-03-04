# agents/agent_base.py

import random

class BaseAgent:
    """
    Classe de base. Chaque agent a:
    - un nom
    - une méthode propose_result() : retourne un int (sa prédiction)
    - une méthode learn() : il reçoit la 'vérité' et l'éventuel feedback
    - une méthode explanation() : un embryon d'explication pour montrer
      qu'il 'comprend' ce qu'il fait (éviter la chambre chinoise).
    """

    def __init__(self, name):
        self.name = name

    def propose_result(self, operand_a, operand_b, operation="+"):
        """
        Retourne un entier. Par défaut, n'importe quoi.
        """
        return random.randint(0, operand_a + operand_b + 5)

    def learn(self, operand_a, operand_b, operation, true_result):
        """
        Reçoit la correction. 
        Peut ajuster sa connaissance/règle interne.
        """
        pass

    def explanation(self):
        """
        Décrit (humainement) comment l'agent conçoit l'addition.
        On veut montrer qu'il n'est pas juste un "table de lookup".
        """
        return f"Je suis un agent de base, je ne sais rien."
