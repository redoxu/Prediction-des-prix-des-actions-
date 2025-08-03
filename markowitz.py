import yfinance as yf
import numpy as np
import pandas as pd
import cvxpy as cp
import matplotlib.pyplot as plt

# Tickers des actions françaises (Yahoo Finance)
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

# Télécharger les données sur 2 ans
data = yf.download(list(tickers.values()), start="2023-08-01", end="2025-08-01")['Close']
# Calculer les rendements journaliers
returns = data.pct_change().dropna()
# Moyenne et matrice de covariance
mu = returns.mean()
Sigma = returns.cov()

# Nombre d'actifs
n = len(tickers)

# Variable d'optimisation : poids du portefeuille
w = cp.Variable(n)
# Rendement cible
target_return = 0.0005  # 13% par an

# Problème d’optimisation de Markowitz
objective = cp.Minimize(cp.quad_form(w, Sigma))
constraints = [
    mu.values @ w >= target_return,
    cp.sum(w) == 1,
    w >= 0  # pas de vente à découvert
]
problem = cp.Problem(objective, constraints)
problem.solve()
print("Status:", problem.status)
print("w.value:", w.value)
# Résultats
port_weights = pd.Series(w.value, index=tickers.keys())
expected_return = mu @ w.value
portfolio_vol = np.sqrt(w.value @ Sigma.values @ w.value)
port_weights_percent = (port_weights * 100).round(2)
print("=== Portefeuille optimal (%) ===")
print(port_weights_percent.astype(str) + " %")

print(f"\nRendement espéré : {expected_return:.4%}")
print(f"Volatilité : {portfolio_vol:.4%}")
