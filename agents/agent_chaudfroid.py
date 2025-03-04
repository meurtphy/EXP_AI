import random

class AgentChaudFroid:
    def __init__(self):
        """
        Initialise l'Agent Chaud-Froid.
        - Il ajuste progressivement ses écarts pour mieux prédire.
        - Il garde une "confiance" sur chaque écart, pour ne pas surcorriger trop vite.
        """
        self.ecarts = {}  # Stocke les écarts appris pour chaque (a, b)
        self.confiance = {}  # Stocke la fiabilité des écarts

    def propose_answer(self, a, b):
        """
        Propose une réponse ajustée en fonction des écarts précédemment appris.
        - S'il a déjà un écart enregistré, il l'utilise pour ajuster sa réponse.
        - Sinon, il commence par une supposition naïve.
        """
        if (a, b) in self.ecarts:
            return (a + b) + self.ecarts[(a, b)]  # Applique son ajustement
        else:
            return random.randint(a + b - 5, a + b + 5)  # Teste un ajustement naïf

    def learn(self, a, b, correct_answer):
        """
        Apprend de ses erreurs :
        - Si son écart était correct plusieurs fois, il le garde.
        - Sinon, il ajuste progressivement.
        """
        predicted = self.propose_answer(a, b)
        ecart = correct_answer - predicted  # Différence entre la vraie réponse et la proposition

        if (a, b) in self.ecarts:
            # Ajuster l'écart de manière progressive
            if ecart == 0:
                self.confiance[(a, b)] += 1  # Plus il a raison, plus il garde cet écart
            else:
                self.ecarts[(a, b)] += ecart // max(1, self.confiance[(a, b)])  # Ajustement progressif
                self.confiance[(a, b)] = max(1, self.confiance[(a, b)] - 1)  # Baisse la confiance s'il se trompe
        else:
            # Premier apprentissage : enregistre l'écart initial
            self.ecarts[(a, b)] = ecart
            self.confiance[(a, b)] = 1  # Confiance initiale

