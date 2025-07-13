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

Soit les prix de clôture suivants sur 5 jours 

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

### MACD
La MACD est simplement la différence entre deux Moyennes Mobiles Exponentielles de périodes différentes. On emploie couramment les périodes de 12 et 26 jours pour ces MME. MACD=EMA_12−EMA_26
L’EMA réagit plus rapidement aux changements récents que la moyenne simple

EMA_t=α×Prix_t+(1−α)×EMA_t−1 ou α=2/n+1
​
La ligne signal est la EMA sur 9 jours de la ligne MACD 

Quand la ligne MACD croise la ligne Signal vers le haut → c’est un signal d’achat

Quand la ligne MACD croise la ligne Signal vers le bas → c’est un signal de vente

Exemple :

| Jour | MACD | Signal | Interprétation |
|------|------------------|-----------|------|
| 1    | -0.5              | -0.6         | MACD < Signal, pas d’achat   |
| 2    | +0.7            | -0.1        | MACD croise au-dessus Signal → signal d’achat    |

## MEDAF -Modèle d'évaluation des actifs financiers
Le modèle d'évaluation des actifs financiers est un modèle financier qui sert à estimer le rendement qu'on devrait attendre d’un investissement risqué.


Rendement attendu de l’action=R_f+β×(R_m−R_f) ou R_f le taux sans risque (le rendement minimal qu’un investisseur peut obtenir sans prendre de risque ex. obligations d’État), R_m le taux attendu du marché (ex. SnP 500) , β risque de l'action par rapport au marché , il mesure combien une action bouge par rapport au marché si (β>1) plus volatile que le marché sinon moins volatile .

Si une action est plus risquée (β > 1), alors les investisseurs veulent un rendement plus élevé pour accepter ce risque.

Exemple Apple (AAPL) vs S&P 500: 
Avec une régression linéaire entre le rendement quotidien (la variation en pourcentage du prix d’une action entre deux jours consécutifs) entre AAPL et S&P 500 on trouve le beta de AAPL (β=1.2) et un rendement attendu d'Apple selon le MEDAF de 11.11%

Dans le projet on exploiter ça en incluant le Bêta comme une feature,ou bien utiliser le rendement attendu comme benchmark.








​












