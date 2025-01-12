# diffusim
Diffusim is a Monte Carlo simulation of particle diffusion in gaseous or liquid substances.

## Why did we pick brownian motion as our theme?
The diffusion of particles in a continuous medium can be described by the diffusion equation or Fick's Law. Essentially, diffusion is the process by which particles move from areas of high concentration to areas of low concentration due to random movements (random in the sense that the movements of the particles are governed by stochastic processes).

Monte Carlo simulations can be used to model the movements of particles and estimate quantities of interest, such as the mean distance traveled or the mean diffusion time over a given time interval.

A concrete example would be simulating the Brownian diffusion of a particle in solution.

## How did we implement and exploit the Monte Carlo method?
The Monte Carlo method is implemented and exploited in the code by using random sampling to simulate the movement of particles in a random walk. In the simulate_random_walk and simulate_particle_collisions functions, random steps (using normal distributions for dx and dy) are taken for each particle, and multiple simulations (or "walks") are run. The results of these random walks are then analyzed, including calculating the final positions and distances. This method allows the estimation of statistical properties (such as mean distance, standard deviation, and collision count) based on random sampling, without needing an exact analytical solution.