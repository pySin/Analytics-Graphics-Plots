import csv
from matplotlib import pyplot as plt


class CSVOptions:

    def __init__(self):
        self.csv_red = csv.DictReader(open('Sales_Records.csv', "r"))
        self.regions_p: list = []

    def region_profit(self):
        all_data = list(self.csv_red)
        regions_set = [sale["Region"] for sale in all_data]
        regions_dict = dict([(region, 0) for region in regions_set])
        for sale_x in all_data:
            regions_dict[sale_x["Region"]] += float(sale_x["Total Profit"])
        self.regions_p = [(key, round(value)) for key, value in regions_dict.items()]
        return "Base dictionary created"

    # horizontal plot / padding /
    def plot_region_profits(self):
        self.region_profit()
        axis_y = [y[0] for y in self.regions_p]
        axis_x = [x[1] / 1000000 for x in self.regions_p]
        plt.xlim(0.5, 140)  # padding method through length
        plt.ylim(-0.5, 6.5)
        bars = plt.barh(axis_y, axis_x)
        plt.title("Sales Per Continent")
        plt.xlabel("Profit in millions", color="#943126")

        for bar in bars:
            width = bar.get_width()
            label_y = bar.get_y() + bar.get_height() / 2
            plt.text(width, label_y, s=f'{width:.2f}m', color="#145A32")

        plt.tight_layout()
        plt.savefig('horizontal_with_bar_labels.png')
        plt.show()

    # Export Plotting data to CSV file. / Practically
    # a list of tuples into CSV file.
    def export_to_csv(self):
        col_names = ",".join([name[0] for name in self.regions_p])
        col_values = ",".join([str(val[1]) for val in self.regions_p])
        with open("profit_per_cont.csv", "a") as cf:
            cf.write(col_names)
            cf.write("\n")
            cf.write(col_values)


if __name__ == "__main__":
    csv_ops = CSVOptions()
    csv_ops.plot_region_profits()
    csv_ops.export_to_csv()
