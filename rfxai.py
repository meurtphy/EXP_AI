#!/usr/bin/env python3
"""
rfxai.py
--------
Interface interactive pour tester l'IA multi-agents.
Tu peux entrer un calcul de type "a+b" pour obtenir une réponse,
mais aussi accéder à des options supplémentaires :
  1) Effectuer un calcul interactif
  2) Lancer une expérience autonome (Agent Experimentateur)
  3) Détecter et afficher les patterns mathématiques découverts
  4) Vérifier les doutes et déclencher le cycle de correction
  5) Tester un calcul contextuel via AgentMultiContext (choix de mode)
  6) Quitter
"""
import sys
import os

BASE_DIR = os.path.dirname(__file__)  # C:\Users\erwan\13
AGENTS_DIR = os.path.join(BASE_DIR, "agents")  # C:\Users\erwan\13\agents
sys.path.insert(0, AGENTS_DIR)  # Met agents/ en priorité dans sys.path

from agents.orchestrateur import Orchestrateur


def show_menu():
    print("\n=== Menu RFXAI ===")
    print("1) Calcul interactif (ex: 2+3)")
    print("2) Lancer une expérience autonome")
    print("3) Détecter et afficher les patterns mathématiques")
    print("4) Vérifier les doutes et corriger les règles")
    print("5) Tester un calcul contextuel (choix du mode)")
    print("6) Quitter")

def calcul_interactif(orch):
    user_input = input("Donne une addition (ex: 2+3) : ").strip()
    try:
        a, b = map(int, user_input.split("+"))
    except ValueError:
        print("Format invalide ! Utilise la forme 'a+b'.")
        return
    # L'IA propose une réponse via l'ordre de priorité des agents
    reponse = orch.propose_answer(a, b)
    print(f"L'IA répond : {reponse}")
    is_correct = input("Est-ce correct ? (oui/non) : ").strip().lower()
    if is_correct == "non":
        try:
            correct_answer = int(input("Quelle est la bonne réponse ? "))
        except ValueError:
            print("La correction doit être un nombre.")
            return
        # Envoie la correction à tous les agents pertinents
        orch.agent_reflexe.learn(a, b, correct_answer)
        orch.agent_chaudfroid.learn(a, b, correct_answer)
        orch.agent_aleatoire.learn(a, b, correct_answer)
        # Les autres agents comme l'AgentLogique ne font pas de learning direct
        print(f"L'IA a appris que {a} + {b} = {correct_answer}.")
    else:
        print("Bravo à l'IA !")

def lancer_experience(orch):
    print("\n=== Lancement d'une expérience autonome ===")
    exp = orch.experimenter()
    print(f"Expérience générée : {exp}")

def detecter_patterns(orch):
    print("\n=== Détection de patterns mathématiques ===")
    patterns = orch.detecter_patterns()
    if patterns:
        print("Patterns détectés :")
        for p in patterns:
            print("  -", p)
    else:
        print("Aucun pattern détecté pour le moment.")
    orch.afficher_regles()

def verifier_doutes(orch):
    print("\n=== Vérification des doutes et correction des règles ===")
    orch.verifier_doute()
    orch.tester_regles()
    orch.afficher_regles()

def tester_contextual(orch):
    print("\n=== Test d'un calcul contextuel ===")
    user_input = input("Donne un calcul (ex: 2+3) : ").strip()
    try:
        a, b = map(int, user_input.split("+"))
    except ValueError:
        print("Format invalide ! Utilise 'a+b'.")
        return
    mode = input("Choisis le mode (classique, fusion, groupement) [classique] : ").strip().lower()
    if mode == "":
        mode = "classique"
    # Appelle directement l'agent_multiContext avec le mode choisi
    response_mc = orch.agent_multicontext.propose_answer(a, b, mode=mode)
    if response_mc is not None:
        print(f"Réponse contextuelle en mode '{mode}': {response_mc}")
        # Optionnel: affiche la valeur "collapse" pour chaque mode
        print("Collapse(classique) =>", response_mc.collapse("classique"))
        print("Collapse(fusion) =>", response_mc.collapse("fusion"))
        print("Collapse(groupement) =>", response_mc.collapse("groupement"))
    else:
        print("Aucune réponse contextuelle obtenue.")

def run_interface():
    orch = Orchestrateur()
    print("=== Interface RFXAI ===")
    print("Bienvenue dans RFXAI, le système multi-agents de mathématiques contextuelles.")
    
    while True:
        show_menu()
        choix = input("Choix : ").strip()
        if choix == "1":
            calcul_interactif(orch)
        elif choix == "2":
            lancer_experience(orch)
        elif choix == "3":
            detecter_patterns(orch)
        elif choix == "4":
            verifier_doutes(orch)
        elif choix == "5":
            tester_contextual(orch)
        elif choix == "6" or choix.lower() == "exit":
            print("Fin de l'entraînement. Au revoir !")
            sys.exit(0)
        else:
            print("Choix invalide, réessaye.")

if __name__ == "__main__":
    run_interface()
