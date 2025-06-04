import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file, write its dimensions and
    return its content as a pandas dafaFrame.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))
