# Arbitrary Text Plot
from matplotlib import pyplot as plt


class ArbitraryTextPlot:

    @staticmethod
    def plot_text():
        plt.xlim(0, 5)
        plt.ylim(0, 6)
        plt.text(4, 4, s="Text")
        plt.text(3, 3, s="Text 2")
        plt.text(2, 2, s="Text 3")
        plt.show()


if __name__ == "__main__":
    atp = ArbitraryTextPlot()
    atp.plot_text()

