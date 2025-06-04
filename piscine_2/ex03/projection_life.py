from load_csv import load
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load the data
    try:
        file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        life_data = load("life_expectancy_years.csv")
        gdp_data = load(file)
        life = life_data["1900"]
        gdp = gdp_data["1900"]

        fig, ax = plt.subplots()
        ax.set_title("1900")
        ax.scatter(gdp, life, alpha=0.5)
        ax.set_xlabel("Gross domestic product")
        ax.xaxis.set_major_locator(MultipleLocator(1000))
        ax.set_ylabel("Life expectancy")
        ax.yaxis.set_major_locator(MultipleLocator(5))
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
