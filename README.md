# Frame Theory: Interactive Kinematic Simulation

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the interactive Python simulation accompanying our theoretical physics paper on **Frame Theory**. It provides a real-time, interactive visualization of the kinematic transition from standard Newtonian dynamics to the Frame Theory regime.

## Features

The simulation visually and mathematically compares Newton's laws with Frame Theory across three physical scales:

1. **Local Orbits:** Compares the trajectory of a test mass around a central body under both paradigms, given the exact same initial velocity.
2. **Photon Deflection (Gravitational Lensing):** Demonstrates the theoretical limit of light deflection in both models.
3. **Galactic Rotation Curves:** Dynamically computes and plots the macroscopic rotation curves. It highlights how Frame Theory naturally predicts the flattening of galactic rotation curves at large radii ($v \propto \sqrt{R_t}$ mechanism) **without the need for Dark Matter**.

## Prerequisites

To run this simulation, you will need **Python 3** installed on your machine, along with two standard scientific libraries: `numpy` and `matplotlib`.

You can install the required dependencies using `pip`:

```bash
pip install numpy matplotlib
```

## How to run

Execute the Python script from your terminal:
python3 frame_simulation.py

## Controls
Once the simulation window opens, you can interact with the physics in real-time:

- Mass ($M$): Adjust the mass of the central body/galaxy.
- Rt​ (Transition Radius): Modify the characteristic scale at which the Frame effect becomes dominant.
- Simulation Speed: Speed up or slow down the numerical integration.
- Reset Button: Re-initializes all test particles to their starting positions.

## Citation / Paper Reference
This code is provided as supplementary material for the paper:

    The Fabric of Spacetime as a Viscoelastic Medium: Cosmological and Phenomenological Implications
    Author: Hedi Kebli
    Journal link: [Link to be added]

If you use this code or the Frame Theory equations in your work, please cite the paper accordingly.
