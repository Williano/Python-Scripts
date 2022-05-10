import matplotlib.pyplot as plt


def main():

    plt.rcParams["font.size"] = 25
    plt.plot(
        [
            "2:24:10",
            "2:24:11",
            "2:24:12",
            "2:24:13",
            "2:24:14",
            "2:24:15",
            "2:24:16",
        ],
        [20, 34, 33, 29, 32, 32, 33],
        linewidth=5,
        color="red",
    )
    plt.xlabel("Time (HH:mm:ss)")
    plt.ylabel("Frame Rate (fps)")
    plt.show()


if __name__ == "__main__":
    main()
