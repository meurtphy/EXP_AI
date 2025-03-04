import random

class AgentExperimentateur:
    def __init__(self):
        """
        L'Agent Experimentateur crée des additions et des soustractions de manière autonome.
        Il observe les résultats et essaie d’identifier des patterns.
        """
        self.resultats = {}  # Stocke les résultats des expériences
    
    def experimenter(self):
        """
        Génère aléatoirement des additions et soustractions et enregistre les résultats.
        """
        a = random.randint(0, 20)  # Prend un nombre aléatoire entre 0 et 20
        b = random.randint(0, 20)  # Un autre nombre aléatoire

        addition = a + b
        soustraction = max(a, b) - min(a, b)  # Toujours positif

        # Stocke les résultats
        self.enregistrer_resultat(a, b, addition, "addition")
        self.enregistrer_resultat(max(a, b), min(a, b), soustraction, "soustraction")

        return (a, b, addition, soustraction)

    def enregistrer_resultat(self, a, b, resultat, operation):
        """
        Enregistre les résultats des opérations pour voir si des patterns émergent.
        """
        if operation not in self.resultats:
            self.resultats[operation] = []

        self.resultats[operation].append((a, b, resultat))

    def afficher_resultats(self):
        """
        Affiche les résultats stockés pour voir les patterns émergents.
        """
        print("\n🔍 Résultats des expériences :")
        for operation, valeurs in self.resultats.items():
            print(f"\n📌 {operation.capitalize()} :")
            for (a, b, resultat) in valeurs:
                print(f"  {a} {'+' if operation == 'addition' else '-'} {b} = {resultat}")
