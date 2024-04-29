from import_data_mysql import ImportData


if __name__ == "__main__":
    im_data = ImportData(["CAvideos_test.csv", "DEvideos_test.csv"])
    im_data.open_file()

