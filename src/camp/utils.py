def hello(name):
    print(f"Hello, {name},{name},{name}!")
    # print(f"Hello, {name},{name},{name}!")
    return 0.0


def compute_mean(numbers) -> float:
    return sum(numbers) / len(numbers)