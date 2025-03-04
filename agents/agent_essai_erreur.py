# agents/agent_essai_erreur.py

import random
from agents.agent_base import BaseAgent

class AgentEssaiErreur(BaseAgent):
    """
    Il propose un guess random autour de a+b, 
    puis il fait un ajustement s'il a tort,
    mais il n'enregistre pas (a,b) -> res précis. 
    Il se contente de pousser sa 'moyenne' dans la bonne direction.
    """

    def __init__(self, name):
        super().__init__(name)
        # param interne qui représente 
        # la croyance qu'il a que "result = a + b" 
        # => en moyenne, guess = factor * (a+b).
        self.factor = 1.0  

    def propose_result(self, operand_a, operand_b, operation="+"):
        if operation == "+":
            base = operand_a + operand_b
            # On fait un guess autour de factor*(a+b)
            guess = int(self.factor * base + random.randint(-1,1))
            return guess
        else:
            return 0

    def learn(self, operand_a, operand_b, operation, true_result):
        if operation == "+":
            guess = self.propose_result(operand_a, operand_b, operation)
            if guess != true_result:
                # on ajuste factor dans la bonne direction
                base = operand_a + operand_b
                if base != 0:
                    correction = (true_result - guess)/base
                    self.factor += 0.1 * correction  # petit pas

    def explanation(self):
        return (f"Je crois que a+b = factor*(a+b)~. "
                f"Actuellement, factor={self.factor:.2f}")
