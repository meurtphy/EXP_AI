from .agent_base import AgentBase  # Correct : on importe depuis le package "agents"

class MultiStateNumber:
    def __init__(self, classical_value, fusion_value=None, group_value=None, label=""):
        self.classical_value = classical_value
        self.fusion_value = fusion_value
        self.group_value = group_value
        self.label = label

    def collapse(self, mode):
        if mode == "classique":
            return self.classical_value
        elif mode == "fusion":
            return self.fusion_value
        elif mode == "groupement":
            return self.group_value
        else:
            return self.classical_value

    def __repr__(self):
        return (f"MultiStateNumber("
                f"{self.classical_value}, {self.fusion_value}, {self.group_value}, label='{self.label}')")


class AgentMultiContext:
    def __init__(self, name="AgentMultiContext"):
        self.name = name

    def propose_answer(self, a, b, **kwargs):
        """
        On effectue un calcul "a+b" de différentes façons (classique, fusion, groupement).
        On peut choisir le mode via kwargs.get('mode', ...).
        Si aucun mode n'est spécifié, on considère 'classique'.
        Retourne un MultiStateNumber (ou None).
        """
        mode = kwargs.get("mode", "classique")

        if mode == "classique":
            # Addition standard
            val = a + b
            msn = MultiStateNumber(
                classical_value=val,
                fusion_value=None,
                group_value=None,
                label=f"{a}+{b} classique"
            )
            return msn

        elif mode == "fusion":
            # Exemple: on fusionne => on prend min(a,b)
            val_fusion = min(a,b)
            val_classic = a + b
            msn = MultiStateNumber(
                classical_value=val_classic,
                fusion_value=val_fusion,
                group_value=None,
                label=f"{a}+{b} fusion"
            )
            return msn

        elif mode == "groupement":
            # Exemple: "1+1 => 1(2)"
            val_classic = a + b
            val_group = f"{a}({b})"
            msn = MultiStateNumber(
                classical_value=val_classic,
                fusion_value=None,
                group_value=val_group,
                label=f"{a}+{b} groupement"
            )
            return msn

        else:
            return None

    def learn(self, a, b, correct_answer, **kwargs):
        # S'il faut apprendre, on peut stocker un feedback.
        pass

    def __repr__(self):
        return f"<{self.name}>"
