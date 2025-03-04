class AgentAutoCorrecteur:
    def __init__(self, agent_pattern):
        """
        L'Agent Auto-Correcteur teste les règles découvertes et les ajuste si elles sont fausses.
        """
        self.agent_pattern = agent_pattern

    def verifier_et_corriger(self):
        """
        Vérifie si les règles découvertes sont toujours valides et les corrige si besoin.
        """
        nouvelles_regles = []
        for regle in self.agent_pattern.regles:
            if "a + a = 2a" in regle:
                if not self.verifier_regle_doublon():
                    print(f"❌ Suppression de la règle incorrecte : {regle}")
                    continue  # On passe à la règle suivante

            elif "a + 1 = suivant" in regle:
                if not self.verifier_regle_suivant():
                    print(f"❌ Suppression de la règle incorrecte : {regle}")
                    continue

            nouvelles_regles.append(regle)

        self.agent_pattern.regles = nouvelles_regles  # On garde seulement les règles valides

    def verifier_regle_doublon(self):
        """
        Vérifie si la règle a + a = 2a est toujours valide.
        """
        for i in range(1, 100):
            if i + i != 2 * i:
                return False  # Une seule erreur et la règle est fausse
        return True  # Si elle est toujours vraie, on la garde

    def verifier_regle_suivant(self):
        """
        Vérifie si la règle a + 1 = suivant est toujours valide.
        """
        for i in range(1, 100):
            if i + 1 != i + 1:
                return False
        return True
