import itertools


def main():
    total = 43.94
    numbers = [
        1.22, 2.75, 1.85, 5.97, 6.47, 2.16, 7.13, 4.57, 1.46, 5.18, 3.16, 4.89,
        7.11, 6.45, 4.77, 8.04, 6.71, 2.31, 6.21, 0.98, 0.87
    ]

    attempts = 1
    count = 1
    for i in range(0, len(numbers)):
        for c in itertools.combinations(numbers, i):
            if sum(c) == total:
                print(f'{count} Found Combination: {c}')
                count = count + 1

            attempts = attempts + 1
    print(f'Numbers: {numbers}')
    print(f'Total: {total}')
    print(f'Total attempts: {attempts}')


if __name__ == "__main__":
    main()