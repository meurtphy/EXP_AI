from .agent_reflexe import AgentReflexe
from .agent_chaudfroid import AgentChaudFroid
from .agent_aleatoire import AgentAleatoire
from .agent_logique import AgentLogique
from .agent_physique import AgentPhysique
from .agent_experimentateur import AgentExperimentateur
from .agent_pattern import AgentPattern
from .agent_autocorrecteur import AgentAutoCorrecteur
from .agent_doute import AgentDoute
from .agent_multicontext import AgentMultiContext

class Orchestrateur:
    def __init__(self):
        """
        Initialise l'Orchestrateur avec tous les agents.
        Respecte la vision globale : chaque agent incarne une couche 
        (réflexe, expérimentation, logique, etc.) et le nouvel agent multi-context 
        vient enrichir la diversité des représentations mathématiques sans trahir les bases initiales.
        """
        self.agent_reflexe = AgentReflexe()
        self.agent_chaudfroid = AgentChaudFroid()
        self.agent_aleatoire = AgentAleatoire()
        self.agent_logique = AgentLogique(self.agent_reflexe)
        self.agent_physique = AgentPhysique()
        self.agent_experimentateur = AgentExperimentateur()
        self.agent_pattern = AgentPattern(self.agent_experimentateur)
        self.agent_autocorrecteur = AgentAutoCorrecteur(self.agent_pattern)
        self.agent_doute = AgentDoute(self.agent_pattern, self.agent_experimentateur, self.agent_autocorrecteur)
        self.agent_multicontext = AgentMultiContext()

    def propose_answer(self, a, b, mode="classique"):
        """
        Demande une réponse aux agents dans l'ordre de priorité, avec debug.
        """
        # 1) Réflexe
        if (a, b) in self.agent_reflexe.memoire:
            answer = self.agent_reflexe.propose_answer(a, b)
            print(f"[DEBUG] Réponse de l'agent Reflexe => {answer}")
            return answer

        # 2) Physique
        response_physique = self.agent_physique.additionner(a, b)
        if response_physique is not None:
            print(f"[DEBUG] Réponse de l'agent Physique => {response_physique}")
            return response_physique

        # 3) MultiContext
        response_multicontext = self.agent_multicontext.propose_answer(a, b, mode=mode)
        if response_multicontext is not None:
            print(f"[DEBUG] Réponse de l'agent MultiContext => {response_multicontext}")
            return response_multicontext

        # 4) Logique
        response_logique = self.agent_logique.propose_answer(a, b)
        if response_logique is not None:
            print(f"[DEBUG] Réponse de l'agent Logique => {response_logique}")
            return response_logique

        # 5) ChaudFroid
        response_chaudfroid = self.agent_chaudfroid.propose_answer(a, b)
        if response_chaudfroid is not None:
            print(f"[DEBUG] Réponse de l'agent ChaudFroid => {response_chaudfroid}")
            return response_chaudfroid

        # 6) Aléatoire (dernier recours)
        final_answer = self.agent_aleatoire.propose_answer(a, b)
        print(f"[DEBUG] Réponse de l'agent Aléatoire => {final_answer}")
        return final_answer

    def experimenter(self):
        """ L’IA génère de nouvelles expériences. """
        return self.agent_experimentateur.experimenter()

    def detecter_patterns(self):
        """ L’IA détecte des règles mathématiques dans ses expériences. """
        return self.agent_pattern.detecter_patterns()

    def verifier_doute(self):
        """ L’IA remet en question ses propres règles et déclenche un cycle de correction. """
        self.agent_doute.verifier_doute()

    def tester_regles(self):
        """ L’IA valide ou invalide les règles après correction. """
        self.agent_autocorrecteur.verifier_et_corriger()

    def afficher_regles(self):
        """ Affiche les règles mathématiques trouvées par l’IA. """
        self.agent_pattern.afficher_regles()
