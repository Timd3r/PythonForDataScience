import matplotlib.pyplot as plt
from load_csv import load


def to_millions(val):
    if isinstance(val, str):
        if 'M' in val:
            return float(val.replace('M', ''))
        elif 'k' in val:
            return float(val.replace('k', '')) / 1000
    return float(val)


def aff_pop():
    """Plot the population projections for Belgium and Zimbabwe over time."""
    try:
        df = load("Python_02_DataTable/data/population_total.csv")
        if df.empty:
            print("No data to plot.")
            return

        Belgium_data = df[df["country"] == "Belgium"]
        Zimbabwe_data = df[df["country"] == "Zimbabwe"]
        le_belgium = Belgium_data.iloc[0, 1:]
        le_zimbabwe = Zimbabwe_data.iloc[0, 1:]
        le_belgium = le_belgium.apply(to_millions).to_numpy()
        le_zimbabwe = le_zimbabwe.apply(to_millions).to_numpy()
        years = Belgium_data.columns[1:].to_numpy()
        print(le_zimbabwe[250])

        plt.figure(figsize=(10, 6))
        plt.plot(years[0:250], le_belgium[0:250], label="Belgium")
        plt.plot(years[0:250], le_zimbabwe[0:250], label="Zimbabwe")
        plt.title("Population projections")
        plt.xlabel("Year")
        plt.ylabel("Population", labelpad=20)
        plt.xticks(years[0:250:40])
        yticks_values = [0, 5, 10, 15, 20, 25]
        yticks_labels = ["0M", "5M", "10M", "15M", "20M", "25M"]
        plt.yticks(yticks_values, yticks_labels)
        plt.grid(False)
        plt.legend(loc="lower right")
        plt.show()

    except Exception as e:
        print(f"Error processing dataset: {e}")


def main():
    """Main function to execute the population plotting."""
    aff_pop()


if __name__ == "__main__":
    """Entry point of the script."""
    main()
