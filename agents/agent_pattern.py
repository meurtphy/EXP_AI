class AgentPattern:
    def __init__(self, agent_experimentateur):
        """
        L'Agent Pattern analyse les expériences et tente de trouver des règles.
        """
        self.agent_experimentateur = agent_experimentateur
        self.regles = []  # Stocke les règles découvertes

    def detecter_patterns(self):
        """
        Cherche des motifs récurrents dans les résultats des expériences.
        """
        donnees = self.agent_experimentateur.resultats.get("addition", [])

        for (a, b, resultat) in donnees:
            # 1️⃣ Vérifie si on a des cas du type a + a = 2a
            if a == b and resultat == 2 * a:
                regle = f"{a} + {a} = {2 * a}  →  a + a = 2a"
                if regle not in self.regles:
                    self.regles.append(regle)

            # 2️⃣ Vérifie si on a des cas du type a + 1 = suivant
            if b == 1 and resultat == a + 1:
                regle = f"{a} + 1 = {a+1}  →  a + 1 = suivant"
                if regle not in self.regles:
                    self.regles.append(regle)

        return self.regles

    def tester_regles(self):
        """
        Vérifie si les règles détectées sont toujours vraies.
        """
        nouvelles_regles = []
        for regle in self.regles:
            if "a + a = 2a" in regle:
                for i in range(1, 50):  # Test sur plusieurs valeurs
                    if i + i != 2 * i:
                        break  # La règle est fausse, on l’abandonne
                else:
                    nouvelles_regles.append(regle)  # La règle est confirmée

            elif "a + 1 = suivant" in regle:
                for i in range(1, 50):
                    if i + 1 != i + 1:
                        break
                else:
                    nouvelles_regles.append(regle)

        self.regles = nouvelles_regles  # On garde seulement les vraies règles

    def afficher_regles(self):
        """
        Affiche les règles trouvées.
        """
        print("\n📌 Règles découvertes par l’IA :")
        for regle in self.regles:
            print(f"  ✅ {regle}")
