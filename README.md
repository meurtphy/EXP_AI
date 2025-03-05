RFXAI - Intelligence Artificielle Multi-Agents Apprenante

📖 Introduction

RFXAI est un projet d'intelligence artificielle visant à créer une IA qui comprend les mathématiques au lieu de simplement les exécuter. Contrairement aux systèmes classiques qui utilisent des opérations préprogrammées (math en Python), cette IA apprend les mathématiques par elle-même à travers l'erreur, la correction et l'expérimentation.

Le but ultime est de résoudre le problème de la "Chambre Chinoise", en faisant en sorte que l'IA ne se contente pas de manipuler des symboles mathématiques, mais qu'elle comprenne réellement ce que représente un nombre, une addition, et d'autres concepts mathématiques fondamentaux.

🎯 Objectif du projet

L'objectif principal est de développer une IA qui :

Apprend les mathématiques comme un être humain, à travers ses erreurs et ses corrections.

N'utilise pas math ou d'autres outils pré-programmés pour résoudre des opérations.

Comprend les nombres et les opérations mathématiques, au lieu de simplement appliquer des règles.

Expérimente et découvre les mathématiques par elle-même.

Tente de casser la Chambre Chinoise, en ayant une véritable représentation interne des mathématiques.

⚙️ Processus d'apprentissage

L'IA fonctionne grâce à un système multi-agents. Chaque agent a une spécificité et un mode d'apprentissage différent, permettant à l'IA de développer une compréhension progressive des nombres et des opérations.

Le processus suit ces étapes :

Un calcul est donné à l'IA (ex: 2+3).

Les agents analysent et génèrent une réponse selon leurs mécanismes propres.

L'utilisateur valide ou corrige la réponse.

L'IA apprend de cette correction et ajuste son modèle interne.

Si le même calcul est reposé, l'IA doit trouver la bonne réponse non pas parce qu'elle l'a mémorisée, mais parce qu'elle comprend comment l'obtenir.

🤖 Liste des agents et leur rôle

L'IA est composée de plusieurs agents qui interagissent ensemble pour résoudre les opérations mathématiques.

1️⃣ Agent Réflexe

Fonctionnement : Répond immédiatement s'il a déjà vu l'opération.

Apprentissage : Enregistre les résultats corrects et ne se trompe plus une fois qu'il a appris.

Limite : Ne comprend pas les mathématiques, il ne fait que retenir des résultats.

2️⃣ Agent Chaud-Froid

Fonctionnement : Corrige ses erreurs en ajustant ses réponses progressivement.

Apprentissage : Si une réponse est fausse, il apprend l'écart entre sa proposition et la réalité.

Objectif : Approcher la bonne réponse par expérience.

3️⃣ Agent Aléatoire

Fonctionnement : Propose des réponses aléatoires pour tester des hypothèses.

Apprentissage : Apprend à ne pas répondre trop loin du résultat attendu.

Utilité : Sert d'exploration initiale pour découvrir les règles sous-jacentes.

4️⃣ Agent Logique

Fonctionnement : Applique des règles déductives pour déduire des résultats.

Apprentissage : Forme progressivement une structure mathématique plus complexe.

5️⃣ Agent Physique

Fonctionnement : Simule l'ajout physique d'objets (ex: compter des pommes).

Utilité : Rapproche les mathématiques d'une expérience concrète.

6️⃣ Agent MultiContext

Fonctionnement : Peut interpréter un calcul de plusieurs manières (ex: 1+1=1(2) en groupement, 1+1=2 en classique).

Objectif : Explorer la diversité des mathématiques et découvrir des lois alternatives.

7️⃣ Agent de Doute

Fonctionnement : Remet en question les réponses d'autres agents.

Utilité : Crée une forme d'auto-validation.

🔍 Etat actuel du projet

✅ L'IA répond correctement aux additions simples sans utiliser math.
✅ Les agents interagissent et apprennent de leurs erreurs.
✅ L'IA peut choisir différentes façons d'interpréter les nombres (grâce à l'Agent MultiContext).
⚠️ L'IA applique encore des règles mais ne "comprend" pas encore vraiment ce qu'est un nombre.
⚠️ Il manque une expérience incarnée du nombre (ex: manipulation physique, explication textuelle de ses réponses).

🚀 Prochaines étapes

Ajouter un Agent Explicatif qui force l'IA à décrire comment elle obtient un résultat.

Intégrer un Agent Corps / Expérience qui manipule les quantités de manière plus concrète.

Explorer la notion de "besoin" pour qu'un agent ait un intérêt à bien calculer (ex: survie, ressources).

🛠️ Installation et exécution

Cloner le projet :

git clone https://github.com/ton-repo/rfxai.git
cd rfxai

Exécuter le programme :

python rfxai.py

