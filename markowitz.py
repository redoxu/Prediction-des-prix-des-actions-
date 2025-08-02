import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize

# 1. Tickers du CAC 40 
tickers = {
    "LVMH": "MC.PA",
    "TotalEnergies": "TTE.PA",
    "BNP Paribas": "BNP.PA",
    "Airbus": "AIR.PA",
    "Sanofi": "SAN.PA",
    "Orange": "ORA.PA",
    "Schneider Electric": "SU.PA",
    "Dassault Systèmes": "DSY.PA"
}

raw_data = yf.download(list(tickers.values()), start="2022-08-01", end="2025-08-01", interval="1mo", group_by='ticker', auto_adjust=True)
data = pd.DataFrame({name: raw_data[ticker]["Close"] for name, ticker in tickers.items()})
data = data.dropna(axis=1)
data.columns = list(tickers.keys())[:data.shape[1]]

# Calcul des rendements lgarithmiques mensuels
returns = np.log(data / data.shift(1)).dropna()
mean_returns = returns.mean().values
cov_matrix = returns.cov().values
n = len(mean_returns)

λ = 0.1

#  Fonction objectif normalisée
equal_weights = np.ones(n) / n
ref_risk = 0.5 * np.dot(equal_weights.T, np.dot(cov_matrix, equal_weights))
ref_return = np.dot(mean_returns.T, equal_weights)

def objective(w, Σ, m, λ):
    global ref_risk, ref_return
    risk = 0.5 * np.dot(w.T, np.dot(Σ, w)) / ref_risk
    ret = np.dot(m.T, w) / ref_return
    return risk - λ * ret

#  Contraintes : somme des poids = 1, pas shorting
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
bounds = [(0, 1) for _ in range(n)]
initial_weights = np.ones(n) / n

# Optimisation
result = minimize(objective, initial_weights, args=(cov_matrix, mean_returns, λ),
                  method='SLSQP', bounds=bounds, constraints=constraints)
#Sequential Least Squares Programming
optimal_weights = result.x




print("\n Composition du portefeuille optimal :")
for asset, weight in zip(data.columns, optimal_weights):
    print(f"{asset}: {weight*100:.2f} %")

expected_return = np.dot(mean_returns, optimal_weights)
portfolio_risk = np.sqrt(np.dot(optimal_weights.T, np.dot(cov_matrix, optimal_weights)))

print(f"\n Rendement espéré mensuel du portefeuille : {expected_return*100:.2f} %")
print(f" Risque mensuel : {portfolio_risk*100:.2f} %")
