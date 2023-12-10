def get_env_report(file: str) -> list:
    with open(file) as input_file:
        return [
            [int(a) for a in line.strip().split()] for line in input_file.readlines()
        ]


def get_env_prediction(line: list) -> int:
    prediction = line[-1]
    while any(entry != 0 for entry in line):
        line = [a - b for (a, b) in zip(line[1:], line[0:-1])]
        prediction += line[-1]
    return prediction


if __name__ == "__main__":
    report = get_env_report("src\\aoc10\\input.txt")
    prediction = sum([get_env_prediction(line) for line in report])
    print(f"Sum of Predictions: {prediction}")
    backtests = sum([get_env_prediction(line[::-1]) for line in report])
    print(f"Sum of Backtests: {backtests}")
