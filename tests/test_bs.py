import numpy as np
from src.bs import bs_pricing


S0, K, r, sigma, t, T = 100, 105, 0, 0.2, 0, 2

# UNIT TESTS
C = bs_pricing(S0, K, r, sigma, t, T, 'C')['price']
P = bs_pricing(S0, K, r, sigma, t, T, 'P')['price']
time = bs_pricing(S0, K, r, sigma, t, T, 'C')['time']

#1 put-call parity test
lhs = C + K * np.exp(-r * time)
rhs = P + S0

assert np.isclose(lhs, rhs, atol=1e-6)


#2 check limits (e.g sigma --> 0, delta between 0 and 1)

#a delta bounds test
delta_call = bs_pricing(S0, K, r, sigma, t, T, 'C')['delta']
delta_put = bs_pricing(S0, K, r, sigma, t, T, 'P')['delta']

assert 0 <= delta_call <= 1   #call
assert -1 <= delta_put <= 0   #put


#b sigma zero limit test
call = bs_pricing(S0, K, r, 1e-8, t, T, 'C')['price']
put  = bs_pricing(S0, K, r, 1e-8, t, T, 'P')['price']

assert np.isclose(call, max(S0 - K*np.exp(-r*time), 0), atol=1e-6)   #As the volatility approaches zero, call price equals immediate payoff
assert np.isclose(put,  max(K*np.exp(-r*time) - S0, 0), atol=1e-6)   #put price equals discounted intrinsic value



#3 confirm results against known textbook values
call = bs_pricing(S0, K, r, sigma, t, T, 'C')
put  = bs_pricing(S0, K, r, sigma, t, T, 'P')

assert np.isclose(call['price'], 9.1974, atol=1e-4)     #call
assert np.isclose(put['price'],   14.1974, atol=1e-4)   #put
assert np.isclose(call["delta"],  0.4876, atol=1e-4)    #delta (call)
assert np.isclose(put['delta'],  -0.5124, atol=1e-4)    #delta (put)
