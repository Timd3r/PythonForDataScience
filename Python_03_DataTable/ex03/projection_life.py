from load_csv import load
import matplotlib.pyplot as plt


def projection_life():
    """Projection of life expectancy in 1900."""
    try:
        df_income = load("Python_03_DataTable/data/income_per_person.csv")
        df_life = load("Python_03_DataTable/data/life_expectancy_years.csv")
        data_1900_income = df_income["1900"]
        data_1900_life = df_life["1900"]

        plt.figure(figsize=(6, 4))
        plt.scatter(data_1900_income, data_1900_life)
        plt.xscale("log")
        plt.xlabel("Gross Domestic Income")
        plt.ylabel("Life Expectancy")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.title("1900")
        plt.show()
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return


def main():
    projection_life()


if __name__ == "__main__":
    main()
