# coursera_sc

# Week 1

L1. Definition Wiener process. 
Table for MGF, and $E(exp(aX)I(Z<b)))$.
W_t ~ \sqrt T Z, where Z is N(0;1).

L2. Conditional expected value. 
Informal def of sigma-algebras. 
Idea: decompose X into predictable and completely unpredictable parts. 
Properties. 

L3. Martingales: discrete time + continuous time.

B1. Use MGF to calculate some Var/Cov/E.
E(tW_t^4)
Var(tW_t^4 + t^2)
Cov(tW_t, W_s^2), s < t
P(3W_4 - W_3 > 0)

B2. Some conditional expected values. 
E(7W_6^2 | W_4)
Var(2W_6 + W_5 | W_4)
P(3W_6 > 2 | W_4)

B3. Check smth is martingale!
Find a, X_t = 6W_t^2 + a t
Find b, Y_t = exp(6W_t + b t)
that X_t, Y_t are martingales. 

P1. Simulate Wiener trajectory. 
Estimate probability that it will hit smth. 
Estimate expected time to hit smth. 


# Week 2

L1. Stochastic integral 
Informal definition using profit. 
Small table in continuous case. 
Short form notation. 

L2. Properties of stochastic integrals. 
And Riemann integrals?

L3. Short-long form notation. 
Martingale criterion: informal theorem!

B1. Calculation of stochastic integrals. 
One with discrete jumps, the second $\int_0^5 2W_u + 3 dW_u$.

B2. Calculate some expected value / variance / Covariance for integrals. 
E(I_t), Var(I_t), Cov(I_t, W_t^2), E(I_6 | I_4)

B3. vasicek expected value
Calculate expected value of return in Vasicek model with specified parameters.

P1. Simulate stochastic integral. 
Draw trajectories. 
Estimate probability. 

# Week 3


L1. Ito's lemma. V1 + V2.

L2. Solve BS SDE using Ito's lemma!

L3. Girsanov theorem.
Informal theorem. Calculations!
Girsanov inside black and sholes: replace mu with any value. 
Let's say r.

B1. Apply Ito's.
X_t = W_t^2 * t^3
X_t = t^3 * S_t^2 where dS_t = ...

B2. Check smth is a martingale using Ito's

B3. Vasicek model. solution of sde

P1. Simulate SDE (Vasicek) path. 


# Week 4

L1. Discounting: discrete time, continuous time. 
Find d(discounted S_t) in BS. 
Not a martingale. 
X_0 \neq E(X_t | F_t)
Every discounted asset price is a martingale
under some P*.  

L2. Call option definition. 
Call option price calculations. 

L3. PDE + Delta-hedging.


B1. No arbitrage condition problem. 
A: pays you 1 dollar if S_T < 10
S: share
B: pays you 1 share if S_T < 10
What is the price of Call option with strike 10?


B2. Calculate price. 
S_T^2

B3. Calculate replicating strategy?
S_t = ... (prev calc)

How much shares and money to replicate this?


P1. Simulation pricing of complex option.



# Ideas 


Informal definition 

Informal theorem 


Every week: 3 lectures, 3 solved problems, 1 prerecorded python screencast. 


Cheat sheet:

* table of derivatives 

* table of expected values for standart normal and wiener 

* table of stochastic integrals 

* table of stochastic integral properties  





# Sources 




American options: simulate on webinars?
http://hsrm-mathematik.de/WS201516/master/option-pricing/American-Options-in-the-Black-Scholes-Model.pdf


http://www.columbia.edu/~mh2078/FoundationsFE/BlackScholes.pdf

http://hsrm-mathematik.de/WS201516/master/option-pricing/

