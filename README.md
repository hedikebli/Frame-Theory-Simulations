# Frame Theory: Interactive Kinematic Simulation

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the interactive Python simulation accompanying our theoretical physics paper on **Frame Theory**. It provides a real-time, interactive visualization of the kinematic transition from standard Newtonian dynamics to the Frame Theory regime.

## Features

The simulation visually and mathematically compares Newton's laws with Frame Theory across four dynamic panels:

1. **Local Orbits:** Compares the trajectory of a test mass around a central body under both paradigms, given the exact same initial velocity.
2. **Photon Deflection (Gravitational Lensing):** Demonstrates the theoretical limit of light deflection in both models, featuring a dynamic auto-zoom that scales with the galaxy's mass to perfectly illustrate the Eddington factor of 2.
3. **Galactic Rotation Curves:** Dynamically computes and plots the macroscopic rotation curves. It highlights how Frame Theory naturally predicts the flattening of galactic rotation curves at large radii **without the need for Dark Matter**.
4. **Empirical Validation (SPARC Catalog):** Plots the real-time asymptotic velocity of the simulated galaxy against empirical data from the SPARC catalog (Baryonic Tully-Fisher Relation), proving the model's accuracy across different mass scales.
5. 
## Prerequisites

To run this simulation, you will need **Python 3** installed on your machine, along with two standard scientific libraries: `numpy` and `matplotlib`.

You can install the required dependencies using `pip`:

```bash
pip install numpy matplotlib
```

## How to run

Execute the Python script from your terminal:
```bash
python3 trame_sparc_animated.py
```

## Controls
Once the simulation window opens, you can interact with the physics in real-time:

- Log10(Mass $M_\odot$): Adjust the baryonic mass of the central galaxy (from dwarf galaxies at $108M_\odot$​ to massive spirals at $10^{11.5} M_\odot$). The transition radius $R_t is dynamically computed based on this mass and the fundamental constant a0​.
- Orbit Speed: Adjust the numerical integration steps (from 10 to 50) to speed up or slow down the orbital visualization.
- Reset Button: Re-initializes all test particles and photons to their starting positions.

## Citation / Paper Reference
This code is provided as supplementary material for the paper:

    Title: The Fabric of Spacetime as a Viscoelastic Medium: Cosmological and Phenomenological Implications
    Author: Hedi Kebli
    Journal link: [Link to be added]

If you use this code or the Frame Theory equations in your work, please cite the paper accordingly.
