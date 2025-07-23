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



# Méthode de Monte-Carlo

La méthode de simulation de Monte-Carlo permet aussi d'introduire une approche statistique du risque dans une décision financière. Elle consiste à isoler des variables clés du projet, telles que le chiffre d'affaires ou la marge, et à leur affecter une loi de probabilités. Pour chacun de ces facteurs, un grand nombre de tirages aléatoires, suivant les lois de probabilité déterminées précédemment, est effectué, afin de trouver la probabilité d'occurrence de chacun des résultats

De manière générale, le problème que l'on cherche à résoudre par les méthodes de Monte-Carlo est celui de l'estimation de l'espérance d'une variable aléatoire X.


La méthode de Monte-Carlo la plus simple consiste à générer un échantillon de variables aléatoires indépendantes et identiquement distribuées (iid) X.

Ensuite on estime l'espérance
avec l'estimateur de la moyenne empirique.


# Modèle de Black-Scholes
Ce modèle Applique le GBM(Mouvement Brownien Géométrique) pour calculer le prix d’une option .

On suppose que le prix d'une action évolue selon une formule stochastique
dSt=μ*St*dt+σ*St*dWt
​ou St le prix actuel ,μ le rendement moyen (MEDAF) ,σ la volatilité ,dWt la variation infinitésimale d'un mouvement brownien(Il modélise les fluctuations aléatoires du marché).

En finance, on suppose que les mouvements aléatoires du prix suivent une loi normale avec moyenne 0 et variance qui grandit dans le temps donc dWt suit une loi normale centrée de variance dt.

En discret cela donne : St+1=St*exp( (μ− ​σ²/2)*Δt + σ*sqrt(Δt)*Z 
ou Z tiré d'une loi normale et Δt la fraction du temps (ex : 1 jour = 1/252 en bourse) 

En recommencant 1000 fois avec des Z différents , on obtient 1000 scénarios possibles dont on calculera la moyenne empirique .On aura donc fait une simulation de Monte Carlo basée sur le GBM.


# Modèles de séries temporelles classiques
## Modèle ARIMA (AutoRegressive Integrated Moving Average)

Le modèle ARIMA permet de modéliser et de prédire les valeurs futures d'une série.

En finance, les prix ne sont pas stationnaires . Mais leurs rendements  sont souvent stationnaires.

En différenciant les séries temporelles, il est possible de retirer les tendances qu’elles présentent pour les stationnariser.
 → Cela permet d’appliquer ARIMA, qui suppose une série stationnaire


Un ARIMA(p, d, q) a 3 paramètres :

-d	Nombre de différenciations pour rendre la série stationnaire : exemple si d=2 on fait une double differenciation Yt = (X_t-X_t-1) - (X_t-1 - X_t-2)

-p	Nombre de retards sur les valeurs passées (Auto-Régressif), on prédit le rendement futur en fonction des p rendements précédents : Exemple si p=2 on a Y_t = a1*Y_t-1 + a2*Y_t-2

-q	Nombre de retards sur les erreurs (Moyenne mobile) : Exemple avec q=1 on fait Y_t = b1 + b2*epsilon_t-1 + epsilon_t avec epsilon une serie de bruit aléatoire.


## Modèle GARCH : Generalized Autoregressive Conditional Heteroskedasticity

Le modèle GARCH est un outil statistique principalement pour modéliser et prévoir la volatilité des séries temporelles. Il est particulièrement utile car il prend en compte le fait que la volatilité des rendements varie dans le temps, ce que les modèles classiques ne font pas.

Structure du modèle GARCH(p,q):

On suppose une série de rendements 
𝑟_t modélisée par : 
r_t=μ+ϵ_t ou ϵ_t=σ_t​*z_t et z_t∼N(0,1)
​

Le modèle GARCH donne σ_t²=α_0 + ∑α_i*ϵ_t−i² + ∑β_j*σ_t−j² (i=1..q) (j=1..p)

Le plus utilisé en pratique est GARCH(1,1)

​












