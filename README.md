# Prédiction-des-prix-des-actions-
## Introduction à la Bourse et aux Actions
La Bourse est un marché organisé où s'échangent des actifs financiers, comme des actions (parts d'entreprises) ,des obligations (dettes d'entreprises ou d’États),des ETF (fonds d'investissement) et d'autres produits financiers (options, futures…).

Une action est une part de propriété dans une entreprise cotée en Bourse. En achetant une action on peut toucher des dividendes de la part de l'entreprise ou bien revendre l’action quand son prix monte (gain en capital).

Le prix d'une action correspond au dernier prix auquel elle a été échangée sur le marché.

Par exemple, si une action est vendue à 20 $, on considère que son prix est de 20 $. Si la transaction suivante se fait à 18 $, alors le nouveau prix affiché sera 18 $.

Ainsi, le cours évolue en temps réel en fonction de l'offre et de la demande.

Il monte si beaucoup d’investisseurs veulent acheter, et il baisse s’ils veulent vendre. Parmi les facteurs influents on trouve les résultats financiers de l'entreprise, les causes économiques comme l'inflation ou des facteurs psychologique comme l'euphorie collective.

Le cours d'ouverture	est le prix de l'action à l'ouverture du marché et le cours de clôture celui à la fin de la séance.

Le volume est	le nombre d’actions échangées.

La volatilité	est l'amplitude des variations de prix.

La capitalisation boursière	est la valeur totale de l’entreprise (nombre d’actions × prix d’une action).

## Indicateurs Techniques (RSI, MACD, etc.)
Un indicateur technique est un outil mathématique basé sur les prix passés d’un actif. Il aide à mieux anticiper les mouvements futurs. Ils sont calculés à partir des données OHLC (Open, High, Low, Close).
### RSI – Relative Strength Index
RSI = 100 - [100 / (1 + RS)], avec RS = Moyenne des gains sur n jours / Moyenne des pertes sur n jours
Par défaut, n = 14 jours.
Si RSI > 70 : l’actif est considéré comme suracheté (le marché est allé trop loin trop vite -->risque de correction)

Si RSI < 30 : l’actif est considéré comme survendu (le prix est trop bas par rapport à sa vraie valeur --> possibilité de rebond)


Par exemple pour calculer le RSI sur 5 jours:
-Calculer les variations quotidiennes (hausse ou baisse entre les jours)

-Séparer les gains et les pertes

-Calculer les moyennes des gains/pertes sur 5 jours

-Diviser gains/pentes pour obtenir RS

-Appliquer la formule finale

Soit les prix de clôture suivants sur 5 jours :

| Jour | Prix de clôture | Variation | Gain | Perte |
|------|------------------|-----------|------|--------|
| 1    | 100              | —         | —    | —      |
| 2    | 102              | +2        | 2    | 0      |
| 3    | 101              | -1        | 0    | 1      |
| 4    | 103              | +2        | 2    | 0      |
| 5    | 104              | +1        | 1    | 0      |

- Moyenne des gains = (2 + 0 + 2 + 1) / 4 = **1.25**
- Moyenne des pertes = (0 + 1 + 0 + 0) / 4 = **0.25**

On calcule :
RS = 1.25 / 0.25 = 5
RSI = 100 - (100 / (1 + 5)) = 100 - (100 / 6) ≈ 83.33











