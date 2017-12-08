from datetime import datetime
import matplotlib.pyplot as plt

LOW_H = 0.1
HIGH_H = 0.9
DPI = 100

SIGNALS = {
    1: HIGH_H,
    0: LOW_H,
}


def build_figure(labels, values):
    assert len(labels) == len(values), "Labels more than values lists"
    assert len(set([len(arr) for arr in values])) == 1, "Values lists have different lengths"

    length = 0
    for k in range(len(values)):
        raw_y = [k + SIGNALS[val] for val in values[k]]
        y = double_arr(raw_y)
        x = create_x(len(raw_y))
        plt.plot(x, y, color='black')
        length = len(x)
    plt.grid(True)
    plt.yticks(range(len(labels)), labels, fontsize=18, va='bottom')
    plt.xticks(range(length))
    plt.xlim((0, length / 2))
    # plt.show()
    date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    plt.savefig("chart_%s.png" % date, fmt='png', dpi=DPI)


def double_arr(arr):
    return_array = []
    for element in arr:
        return_array = return_array + [element, element]
    return return_array


def create_x(num):
    arr = []
    for n in range(num):
        arr = arr + [n, n + 1]
    return arr


if __name__ == "__main__":
    labels_main = []
    values_main = []
    while True:
        print("Enter label:")
        label = input()
        if label == "exit":
            break
        print("Enter values:")
        numbers = [int(val) for val in list(input().replace(" ", ""))]
        for number in numbers:
            if number not in SIGNALS:
                print("Wrong value")
                continue
        labels_main.append(label)
        values_main.append(numbers)
    build_figure(labels_main, values_main)

# build_figure(["Q1", "Q2", "test", "1", "as", "ghj", "ooo"], [[1, 1, 1, 0, 0, 0, 1, 0, 0, ],
#                                                              [1, 0, 1, 1, 0, 1, 1, 0, 0, ],
#                                                              [1, 0, 1, 1, 0, 1, 1, 0, 0, ],
#                                                              [1, 0, 1, 1, 0, 1, 1, 0, 0, ],
#                                                              [1, 0, 1, 1, 0, 1, 1, 0, 0, ],
#                                                              [1, 0, 1, 1, 0, 1, 1, 0, 0, ],
#                                                              [1, 0, 1, 1, 0, 1, 1, 0, 0, ], ])
