# diffusim
Diffusim is a Monte Carlo simulation of particle diffusion in gaseous or liquid substances.

# Implementation

## Why did we pick brownian motion as our theme?
The diffusion of particles in a continuous medium can be described by the diffusion equation or Fick's Law. Essentially, diffusion is the process by which particles move from areas of high concentration to areas of low concentration due to random movements (random in the sense that the movements of the particles are governed by stochastic processes).

Monte Carlo simulations can be used to model the movements of particles and estimate quantities of interest, such as the mean distance traveled or the mean diffusion time over a given time interval.

A concrete example would be simulating the Brownian diffusion of a particle in solution.

## How did we implement and exploit the Monte Carlo method?
The Monte Carlo method is implemented and exploited in the code by using random sampling to simulate the movement of particles in a random walk. In the simulate_random_walk and simulate_particle_collisions functions, random steps (using normal distributions for dx and dy) are taken for each particle, and multiple simulations (or "walks") are run. The results of these random walks are then analyzed, including calculating the final positions and distances. This method allows the estimation of statistical properties (such as mean distance, standard deviation, and collision count) based on random sampling, without needing an exact analytical solution.

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
