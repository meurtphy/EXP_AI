import json
import os
import random

class AgentReflexe:
    FICHIER_MEMOIRE = "memoire.json"  # Nom du fichier où on stocke la mémoire

    def __init__(self):
        """ Initialisation de l'agent : il charge sa mémoire s'il en a une. """
        self.memoire = {}  # Dictionnaire pour stocker les réponses connues
        self.charger_memoire()  # On charge la mémoire existante

    def propose_answer(self, a, b):
        """ L'agent propose une réponse pour l'addition a + b. """
        if (a, b) in self.memoire:
            return self.memoire[(a, b)]  # Il répond directement avec son réflexe
        else:
            return self.reaction_reflexe()  # Réponse aléatoire

    def reaction_reflexe(self):
        """ Réaction instinctive : balance un chiffre au hasard. """
        return random.randint(0, 100)  # Il réagit au hasard au début

    def learn(self, a, b, correct_answer):
        """ Il enregistre la bonne réponse pour ce calcul et sauvegarde la mémoire. """
        self.memoire[(a, b)] = correct_answer  # Il retient la correction
        self.sauvegarder_memoire()  # On sauvegarde après chaque apprentissage

    def sauvegarder_memoire(self):
        """ Sauvegarde la mémoire de l'agent dans un fichier JSON. """
        with open(self.FICHIER_MEMOIRE, "w") as f:
            # Convertir les tuples en chaînes de caractères avant d'enregistrer
            json.dump({f"{k[0]},{k[1]}": v for k, v in self.memoire.items()}, f)

    def charger_memoire(self):
        """ Charge la mémoire depuis le fichier JSON si celui-ci existe. """
        if os.path.exists(self.FICHIER_MEMOIRE):
            try:
                with open(self.FICHIER_MEMOIRE, "r") as f:
                    data = json.load(f)
                    # Convertir les clés en tuples après chargement
                    self.memoire = {tuple(map(int, k.split(","))): v for k, v in data.items()}
            except (json.JSONDecodeError, ValueError):
                print("⚠️ Erreur de chargement de la mémoire. Le fichier est peut-être corrompu. Réinitialisation.")
                self.memoire = {}  # Réinitialise en cas de fichier invalide
