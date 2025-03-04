import random

class AgentAleatoire:
    def __init__(self):
        """
        Initialise l'Agent Aléatoire.
        - Il commence avec une exploration totale.
        - Il ajuste progressivement ses propositions en fonction des corrections reçues.
        """
        self.plage_possible = {}  # Stocke les fourchettes de valeurs possibles pour chaque (a, b)
        self.prob_exploration = 1.0  # 100% d'exploration au début

    def propose_answer(self, a, b):
        """
        Propose une réponse en fonction de son niveau d'exploration :
        - Si l'addition (a, b) est inconnue → Totalement aléatoire.
        - Si elle a déjà été corrigée → Choix dans une fourchette raisonnable.
        - Avec une petite probabilité, il propose encore du hasard.
        """
        if (a, b) in self.plage_possible:
            # Si l'agent a déjà une plage ajustée, il propose un nombre dans cette fourchette
            borne_min, borne_max = self.plage_possible[(a, b)]
            if random.random() < self.prob_exploration:  # Chance d'explorer encore un peu
                return random.randint(0, 100)  # Exploration pure
            return random.randint(borne_min, borne_max)  # Réponse dans la fourchette

        # Si aucun apprentissage n'a été fait, il explore totalement
        return random.randint(0, 100)

    def learn(self, a, b, correct_answer):
        """
        Apprend à ajuster sa plage de réponses :
        - Il réduit la fourchette des nombres plausibles.
        - Diminue la probabilité d'exploration pour être plus précis.
        """
        if (a, b) in self.plage_possible:
            # Ajuste la fourchette existante
            borne_min, borne_max = self.plage_possible[(a, b)]
            new_min = max(0, min(borne_min, correct_answer - 2))  # On ajuste progressivement
            new_max = max(borne_max, correct_answer + 2)
            self.plage_possible[(a, b)] = (new_min, new_max)
        else:
            # Première correction : création d'une fourchette autour de la bonne réponse
            self.plage_possible[(a, b)] = (correct_answer - 3, correct_answer + 3)

        # Diminue progressivement la probabilité d'exploration
        self.prob_exploration = max(0.05, self.prob_exploration * 0.9)  # Réduction progressive

