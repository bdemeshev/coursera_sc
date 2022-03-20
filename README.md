# coursera_sc


ducks!

\duck[crazyhair] for informal definitions and theorems
\duck[tophat,bowtie,tshirt,jacket=gray] for formal definitions and theorems

# Week 1

Video 1 (slides). Definition Wiener process. 
Table for MGF, and $E(exp(aX)I(Z<b)))$.
W_t ~ \sqrt T Z, where Z is N(0;1).

Video 2 (board). Use MGF to calculate some Var/Cov/E.
E(tW_t^4)
Var(tW_t^4 + t^2)
Cov(tW_t, W_s^2), s < t
P(3W_4 - W_3 > 0)


Video 3 (slides). Conditional expected value. 
Informal def of sigma-algebras. 
Idea: decompose X into predictable and completely unpredictable parts. 
Properties. 

Video 4 (board). Some conditional expected values. 
E(7W_6^2 | W_4)
Var(2W_6 + W_5 | W_4)
P(3W_6 > 2 | W_4)

Video 5 (slides). Martingales: discrete time + continuous time.

Video 6 (board). Check smth is martingale!
Find a, X_t = 6W_t^2 + a t
Find b, Y_t = exp(6W_t + b t)
that X_t, Y_t are martingales. 

Video 7 (python). Simulate Wiener trajectory. 
Estimate probability that it will hit smth. 
Estimate expected time to hit smth. 


# Week 2

Video 1 (slides). Stochastic integral 
Informal definition using profit. 
Small table in continuous case. 
Short form notation. 

Video 2 (board). Calculation of stochastic integrals. 
One with discrete jumps, the second $\int_0^5 2W_u + 3 dW_u$.

Video 3 (slides). Properties of stochastic integrals. 
And Riemann integrals?

TODO: пропустил изометрию для ковариации в слайдах! ? в доп материалы или переснять?

Video 4 (slides). Short-long form notation. 
Martingale criterion: informal theorem!
No derivative! Symbolic language!

Video 5 (board). Calculate some expected value / variance / Covariance for integrals. 
E(I_t), Var(I_t), Cov(I_t, W_t^2), E(I_6 | I_4)

Video 6 (board). vasicek expected value
Calculate expected value of return in Vasicek model with specified parameters.

Video 7 (python). Simulate stochastic integral. 
Draw trajectories. 
Estimate probability. 

# Week 3


L1. Ito's lemma. V1 + V2.


B1. Apply Ito's.
X_t = W_t^2 * t^3
X_t = S_t^2 where dS_t = ...
conclusion: not martingales!

B2. Check smth is a martingale using Ito's
When is a martingale?
X_t = W_t^2 + at
Y_t = exp(a W_t + bt)


L2. Solve BS SDE using Ito's lemma!

B3. Vasicek model. solution of sde


L3. Girsanov theorem.
Informal theorem. Calculations!
Girsanov inside black and sholes: replace mu with any value. 
Let's say r.


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

B1. No arbitrage condition problem. 
A: pays you 1 dollar if S_T < 10
S: share
B: pays you 1 share if S_T < 10
r = 0.05
What is the price of Call option with strike 10?


B2. Calculate price. 
S_2^3


L3. PDE + Delta-hedging.


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




### Монтирование pptx из png
* Запускаем powerpoint
* добавить картинки - новый альбом - выбираем файлы (галочки на каждом НЕ надо ставить! просто insert)
* конструктор (или что там справа от добавить картинки) - устанавливаем формат 4:3. 
При масштабировании фон сам сменится на прозрачный.
* или: Дизайн: размер слайда (справа)
