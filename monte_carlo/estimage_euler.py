import math
import numpy as np


def generate_random_number() -> float:
    return np.random.uniform(0, 1)


def run_simulation() -> None:
    E = math.e
    experiments = 1_000_000
    num_selections = []
    total = 0
    selection = 0
    for _ in range(experiments):
        num = generate_random_number()
        total += num
        selection += 1
        if total >= 1:
            num_selections.append(selection)
            selection = 0
            total = 0
    expected_value = np.mean(num_selections)
    error = 100 * abs((expected_value - E) / E)
    print(
        f"Running {experiments} experiments\n"
        f"Expected # {expected_value}\n"
        f"Error % : {error}%"
    )


if __name__ == "__main__":
    run_simulation()
