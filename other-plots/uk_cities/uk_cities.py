# UK Cities
import matplotlib.pyplot as plt


class UKCities:

    def __init__(self):
        self.cities = ["London", "Birmingham", "Glasgow", "Liverpool", "Bristol", "Manchester"]
        self.population = [8907918, 1153717, 612040, 579256, 571922, 554400]

    def create_bar_chart(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x=range(len(self.cities)), height=self.population)
        ax.set_xticks(range(len(self.cities)), self.cities)

        for i, population in enumerate(self.population):
            ax.text(i, population, str(population),
                    ha='center', va='bottom', color="gray")

        plt.title("UK Cities Population")
        plt.xlabel("Cities")
        plt.ylabel("Population in Millions")
        plt.show()


if __name__ == "__main__":
    ukc = UKCities()
    ukc.create_bar_chart()
