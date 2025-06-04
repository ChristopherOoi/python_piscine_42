from load_csv import load
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load the data
    try:
        life_data = load("life_expectancy_years.csv")
        country = "Singapore"
        if country not in life_data["country"].values:
            print(f"Country '{country}' not found in the dataset.")
            exit(1)
        vals = life_data.loc[life_data["country"] == country].values[0][1:]
        years = list(life_data.columns)[1:]

        fig, ax = plt.subplots()
        ax.plot(years, vals, marker="o")
        ax.set_title(f"{country} Life expectancy Projections")
        ax.set_xlabel("Year")
        ax.xaxis.set_major_locator(MultipleLocator(50))
        ax.set_ylabel("Life expectancy")
        ax.yaxis.set_major_locator(MultipleLocator(10))
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
