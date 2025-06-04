from load_csv import load
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load the data
    try:
        life_data = load("population_total.csv")
        country = "Singapore"
        versus = "France"
        if (
            country not in life_data["country"].values
            or versus not in life_data["country"].values
        ):
            print("Countries not found in the dataset.")
            exit(1)
        cvals = life_data.loc[life_data["country"] == country].values[0][1:]
        cyears = list(life_data.columns)[1:]
        vvals = life_data.loc[life_data["country"] == versus].values[0][1:]
        vyears = list(life_data.columns)[1:]

        fig, ax = plt.subplots()
        ax.plot(cyears, cvals, marker="o", color="blue", label=country)
        ax.plot(vyears, vvals, marker="x", color="orange", label=versus)
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.xaxis.set_major_locator(MultipleLocator(1000))
        ax.set_ylabel("Population")
        ax.yaxis.set_major_locator(MultipleLocator(100))
        ax.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
