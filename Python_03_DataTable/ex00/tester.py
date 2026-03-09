from load_csv import load


def main():
    df = load('Python_03_DataTable/data/life_expectancy_years.csv')
    print(df)


if __name__ == "__main__":
    main()
