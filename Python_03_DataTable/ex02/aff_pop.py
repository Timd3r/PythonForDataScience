import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def millions_formatter(x, pos):
    return f"{int(x)}M"


def aff_pop():
    try:
        df = load("Python_03_DataTable/data/life_expectancy_years.csv")
        if df.empty:
            print("No data to plot.")
            return

        Belgium_data = df[df["country"] == "Belgium"]
        Zimbabwe_data = df[df["country"] == "Zimbabwe"]
        le_belgium = Belgium_data.iloc[0, 1:].to_numpy()
        le_zimbabwe = Zimbabwe_data.iloc[0, 1:].to_numpy()
        years = Belgium_data.columns[1:].to_numpy()

        plt.figure(figsize=(10, 6))
        plt.plot(years[0:250], le_belgium[0:250], label="Belgium")
        plt.plot(years[0:250], le_zimbabwe[0:250], label="Zimbabwe")
        plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.title("Population projections")
        plt.xlabel("Year")
        plt.ylabel("Population", labelpad=20)
        plt.xticks(years[0:250:40])
        plt.yticks(range(0, 80, 20))
        plt.grid(False)
        plt.legend(loc="lower right")
        plt.show()

    except Exception as e:
        print(f"Error processing dataset: {e}")


def main():
    aff_pop()


if __name__ == "__main__":
    main()
