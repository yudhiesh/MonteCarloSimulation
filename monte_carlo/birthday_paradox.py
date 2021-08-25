import numpy as np
from collections import Counter


def generate_random_birthdays():
    birthdays = np.random.randint(365, size=23).tolist()
    assert len(birthdays) == 23, f"Length of birthdays is {len(birthdays)}"
    return birthdays


def run_simulation():
    trials = 1_000_000
    success = 0
    for _ in range(trials):
        birthdays = generate_random_birthdays()
        counter = Counter(birthdays)
        if 2 in counter.values():
            success += 1
    probability = success / trials
    print(f"Probability : {probability}")


if __name__ == "__main__":
    run_simulation()
