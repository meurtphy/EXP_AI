class AgentDoute:
    def __init__(self, agent_pattern, agent_experimentateur, agent_autocorrecteur):
        self.agent_pattern = agent_pattern
        self.agent_experimentateur = agent_experimentateur
        self.agent_autocorrecteur = agent_autocorrecteur

    def verifier_doute(self):
        """ Vérifie si certaines règles de l'IA mènent à des contradictions 
            et déclenche un cycle d'actions pour résoudre ces contradictions. """
        for regle in self.agent_pattern.regles:
            contradiction = self.tester_regle_avec_valeurs_limites(regle)
            if contradiction:
                print(f"⚠️ Contradiction trouvée pour la règle : {regle}")

                # 1) Génère plus de data autour de la zone de contradiction
                self.lancer_experiences_ciblees(regle)

                # 2) Redemande à AgentPattern de redétecter les règles
                nouvelles_regles = self.agent_pattern.detecter_patterns()

                # 3) On relance l'auto-correcteur pour valider/invalider
                self.agent_autocorrecteur.verifier_et_corriger()

    def tester_regle_avec_valeurs_limites(self, regle):
        """ 
        Teste la règle sur des valeurs atypiques (négatifs, fractions, grands nombres).
        Retourne True s'il y a contradiction, False sinon.
        """
        # Pseudocode qui parse la règle et vérifie sur différents cas
        # ex: si "a + a = 2a", on teste i + i vs 2*i, etc.
        pass

    def lancer_experiences_ciblees(self, regle):
        """
        Génère exprès des cas-tests qui se situent dans la zone où la règle semble fausse.
        Exemple: si la règle coince sur les négatifs, on va générer -5 + -2, etc.
        """
        # On peut forcer l'AgentExpérimentateur à tester ces calculs
        for _ in range(10):
            # On choisit a, b autour de la zone de contradiction
            # ex: entiers négatifs, fractions, etc.
            a = ...
            b = ...
            self.agent_experimentateur.resultats.setdefault("addition", []).append((a, b, a+b))
        print("🔬 Nouvelles expériences ciblées ajoutées au data.")
