# Option Pricing Project

##  Project Overview
This project implements, tests, and compares option pricing and hedging methods:
- **Black–Scholes Model**
- **Binomial Model**
- **Monte Carlo Simulation**

We will apply these methods to real option-chain data, analyze model performance, and evaluate hedging strategies.  
The project is structured into weekly deliverables, building from simple examples to full hedging simulations.

---

## Installation

Clone this repository and set up dependencies in a virtual environment:

```bash
# Clone the repo
git clone https://github.com/olaitann93/option-pricing-project.git
cd option-pricing-project

# (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install requirements
pip install -r requirements.txt


# Quickstart 
Run the first Jupyter notebook with a minimal Black–Scholes example:

jupyter notebook notebooks/00_environment_and_examples.ipynb

This notebook:
- Imports core libraries
- Prices a European call option with the Black–Scholes formula
- Produces a simple plot of option value vs. stock price


## Weekly Deliverables Plan

- Week 0: Repo setup, environment, and toy Black–Scholes example.
- Week 1: Full folder structure, implement Black–Scholes in src/bs.py, add unit tests.
- Week 2: Implement Binomial pricing model + compare with Black–Scholes.
- Week 3: Monte Carlo simulation for option pricing.
- Week 4: Pull real option-chain data, test models on market data.
- Week 5: Hedging simulations and evaluation.
- Week 6: Final report and presentation.