# agents/agent_memoire.py
import math
from agents.agent_base import BaseAgent

class AgentMemoire(BaseAgent):
    """
    Cet agent induit une 'règle' depuis ce qu'il a déjà vu.
    S'il voit plusieurs fois a+b, il essaie de déduire
    un pattern général.
    """

    def __init__(self, name):
        super().__init__(name)
        self.examples = []  # stocke (a, b, op, result)

    def propose_result(self, operand_a, operand_b, operation="+"):
        # Cherche si on a déjà vu un cas similaire
        for (aa, bb, op, res) in self.examples:
            if op == operation and aa == operand_a and bb == operand_b:
                return res
        # Sinon, devine
        return 0

    def learn_from_feedback(self, operand_a, operand_b, operation, true_result):
        # Ajoute l'exemple s'il n'existe pas
        found = False
        for (aa, bb, op, res) in self.examples:
            if aa == operand_a and bb == operand_b and op == operation:
                found = True
                break
        if not found:
            self.examples.append((operand_a, operand_b, operation, true_result))
