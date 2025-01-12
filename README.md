# diffusim
Diffusim is a Monte Carlo simulation of particle diffusion in gaseous or liquid substances.

# Theoretical Overview

The main goal of our simulation is to approximate the **mean** of the center of mass distance of a Brownian motion (which should converge to 0). We achieve this by implementing a **random walk**. To do so, we simulate two random variables representing the <code>X</code> and <code>Y</code> components of the movement vector of the particle. We assume that <code>X, Y ~ N(0, 1)</code>.

The resultant vector of these two components follows a **Rayleigh distribution**, with a mean of <code>1 &times; &radic;(&pi; / 2)</code> and a standard deviation of <code>&radic;(((4 &minus; &pi;) / 2) &times; 1<sup>2</sup>)</code>.

---

## Central Limit Theorem (CLT)

If we simulate <code>n</code> steps as described above, with <code>n</code> large enough, the CLT tells us that:

<code>S<sub>n</sub> ~ N(0, n &times; 1)</code>

This is because the sum of all the direction vectors can be broken into the sum of their individual components, which are distributed as <code>N(0, 1)</code>.

By simulating <code>S<sub>n</sub></code> <code>N</code> times, we can approximate its mean, which by the **law of large numbers** will converge to its theoretical value, which in our case is 0.

---

## Confidence Interval

To calculate a **confidence interval**, we compute the **standard error of the mean (SEM)** and the corresponding <code>z<sub>&alpha;/2</sub></code> for <code>S<sub>n</sub></code>. The confidence interval allows us to state, with <code>(1 &minus; &alpha;)</code> &#37; confidence, that the error will be within the interval:

<code>(&minus;z<sub>&alpha;/2</sub> &times; SEM, z<sub>&alpha;/2</sub> &times; SEM)</code>

In other words, our **margin of error** <code>&varepsilon;</code> is given by:

<code>&varepsilon; = z<sub>&alpha;/2</sub> &times; SEM</code>

This ensures that <code>(1 &minus; &alpha;) &times; 100&#37;</code> of the time, the estimated mean will lie within the calculated interval.
