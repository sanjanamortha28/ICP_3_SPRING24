import numpy as np

def replace_maximum(array, replace_value, axis):
    output = np.where(array == np.max(
        array, axis=1).reshape(-1, 1), 0 * array, array)
    print(output)


def main():
    random_values = np.random.random_sample(20) * 20 + 1
    print(random_values)
    random_4by5 = random_values.reshape((4, 5))
    print(random_4by5)
    replace_maximum(random_4by5, 0, 1)


if __name__ == "__main__":
    main()