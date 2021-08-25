import math
from typing import List, Tuple
import numpy as np


def generate_random_point() -> Tuple[float, float]:
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    return x, y


def run_simulation(points: int) -> Tuple[float, float, float]:
    assert points > 0
    success = 0
    for _ in range(points):
        x, y = generate_random_point()
        if (x ** 2) + (y ** 2) < 1:
            success += 1
    pi_approx = 4 * (success) / (points)
    error = 100 * abs((pi_approx - math.pi) / math.pi)
    return pi_approx, error, points


def compare_simulations(
    approx_pi_values: List[Tuple[float]],
    errors: List[Tuple[float]],
    list_points: List[int],
):
    for approx_pi, error, points in zip(approx_pi_values, errors, list_points):
        print(
            f"Simulation ran for {points} points\n"
            f"Approx pi value: {approx_pi}\n"
            f"Error % : {error}%"
        )


def run_simulations():
    simulations = list(zip(*[run_simulation(i) for i in range(1, 100_000, 10_000)]))
    compare_simulations(
        approx_pi_values=simulations[0],
        errors=simulations[1],
        list_points=simulations[2],
    )


if __name__ == "__main__":
    run_simulations()
