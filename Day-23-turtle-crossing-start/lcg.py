import matplotlib.pyplot as plt

def plot_histogram(filename, title):
    with open(filename, "r") as f:
        data = [float(line.strip()) for line in f]

    plt.hist(data, bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

plot_histogram("output1.txt", "Random Numbers - Example 1")
plot_histogram("output2.txt", "Random Numbers - Example 2")
