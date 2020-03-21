import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import itertools
import csv
import numpy as np


def _save_png(input_path, x_label, y_label):
        x = []
        y = []
        with open(input_path, "r") as scores:
            reader = csv.reader(scores)
            data = list(reader)
            for i in range(0, len(data)):
                x.append(float(i))
                y.append(float(data[i][0]))

        plt.subplots()
        plt.plot(x, y, color='green', label="score per run")

        average_range = len(x)
        plt.plot(x[-average_range:], [np.mean(y[-average_range:])] * len(y[-average_range:]), linestyle="--", label="average")

        plt.title("monte_carlo")
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        plt.legend(loc="lower right")
        plt.savefig("results/" + "monte_carlo" + ".png", bbox_inches="tight")
        plt.close() 


_save_png("results/monte_carlo.csv", "runs", "results")