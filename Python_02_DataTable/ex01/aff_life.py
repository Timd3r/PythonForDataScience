import matplotlib.pyplot as plt
from load_csv import load


def aff_life():
    """Plot the life expectancy projections for Belgium over time."""
    try:
        df = load("Python_02_DataTable/data/life_expectancy_years.csv")
        if df is None or df.empty:
            return

        belgium_df = df[df["country"] == "Belgium"]
        years = belgium_df.columns[1:].to_numpy()

        life_expectancy = belgium_df.iloc[0, 1:].to_numpy()

        plt.figure(figsize=(10, 8))
        plt.plot(years, life_expectancy)
        plt.title("Belgium Life Expectancy Over Time")
        plt.xlabel("Year")
        plt.ylabel("Belgium Life Expectancy Projections (years)")
        plt.xticks(years[::40])
        plt.grid(False)
        plt.show()

    except Exception as e:
        print(f"Error processing dataset: {e}")


def main():
    """Main function to execute the life expectancy plotting."""
    aff_life()


if __name__ == "__main__":
    """Entry point of the script."""
    main()
