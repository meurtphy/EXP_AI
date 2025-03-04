# agents/agent_incrementeur.py

from agents.agent_base import BaseAgent

class AgentIncrementeur(BaseAgent):
    """
    "Comprend" l'addition comme un enchaînement d'incréments.
    Par exemple: a+b => part de a, et fait +1 b fois.
    Au début, il peut avoir un 'bug' dans sa boucle, 
    qu'il corrige au fur et à mesure.
    """

    def __init__(self, name):
        super().__init__(name)
        # On simule un 'bug' : parfois, il n'incrémente pas toujours b fois.
        self.increment_error_rate = 0.3  # 30% du temps, il rate une incrémentation

    def propose_result(self, operand_a, operand_b, operation="+"):
        if operation != "+":
            # pour l'instant, il ne sait faire que "+"
            return 0

        result = operand_a
        # Tente d'incrémenter b fois
        for i in range(operand_b):
            # s'il rate une incrémentation -> on saute la boucle 1 fois sur ...
            # (simplification)
            if random.random() < self.increment_error_rate:
                continue
            result += 1
        return result

    def learn(self, operand_a, operand_b, operation, true_result, was_correct):
    if operation == "+":
        if was_correct:
            # Réduire l'erreur plus vite si bonne réponse
            self.increment_error_rate = max(0.0, self.increment_error_rate * 0.9)
        else:
            # Augmenter doucement en cas d'erreur, mais jamais au-dessus de 50%
            self.increment_error_rate = min(0.5, self.increment_error_rate + 0.01)


    def explanation(self):
        return ("Je conçois l'addition comme un enchaînement de +1. "
                f"Mon taux d'erreur actuel dans l'incrément: {self.increment_error_rate:.2f}")
