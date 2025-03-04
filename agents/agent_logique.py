# agents/agent_logique.py

from agents.agent_base import BaseAgent

class AgentLogique(BaseAgent):
    """
    Agent qui a la 'règle' a+b = a+b (trivial).
    
    Au début, on lui met un paramètre offset 
    (il calcule a+b + offset, simulant qu'il n'a pas 
    compris la base 10 ou un décalage).
    """

    def __init__(self, name, offset=0):
        super().__init__(name)
        self.offset = offset

    def propose_result(self, operand_a, operand_b, operation="+"):
        if operation == "+":
            return operand_a + operand_b + self.offset
        else:
            return 0

    def learn(self, operand_a, operand_b, operation, true_result):
        if operation == "+":
            guess = operand_a + operand_b + self.offset
            if guess == true_result:
                # On ne change rien
                pass
            else:
                # On ajuste l'offset
                self.offset = self.offset - (guess - true_result)

    def explanation(self):
        return (f"Je connais la règle a+b, "
                f"mais j'avais un offset={self.offset}. "
                f"Je corrige cet offset avec le temps.")
