import numpy as np
from scipy.stats import norm


def bs_pricing(S0, K, r, sigma, t, T, opt_type='C'):
    """Black–Scholes price for European option and analytical Greeks"""
    ttm = T-t
    
    if ttm < 0:
        return 0.0
    elif ttm == 0.0:
        if opt_type == 'C':
            return np.maximum(S0 - K, 0.0)
        else:
            return np.maximum(K - S0, 0.0)
    
    num = np.log(S0/K) + (r - 0.5 * sigma**2) * ttm
    den = sigma * np.sqrt(ttm)
    d2 = num/den

    d1 = d2 + den

    if opt_type == 'C':
        price = S0 * norm.cdf(d1) - K * np.exp(-r * ttm) * norm.cdf(d2)
        delta = norm.cdf(d1)
        theta = (-(S0 * norm.pdf(d1)) * sigma / 2 * np.sqrt(ttm)) - r * K * np.exp(-r * ttm) * norm.cdf(d2) 
        rho = ttm * K * np.exp(-r * ttm) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * ttm) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
        delta = norm.cdf(d1) - 1
        theta = (-(S0 * norm.pdf(d1)) * sigma / 2 * np.sqrt(ttm)) + r * K * np.exp(-r * ttm) * norm.cdf(-d2) 
        rho = -ttm * K * np.exp(-r * ttm) * norm.cdf(-d2)

    gamma = norm.pdf(d1)/(S0 * den)
    vega = S0 * norm.pdf(d1) * np.sqrt(ttm)
    
    return {
        'time':ttm, 
        'price':price, 
        'delta':delta, 
        'gamma':gamma, 
        'vega':vega, 
        'theta':theta, 
        'rho':rho
    }

