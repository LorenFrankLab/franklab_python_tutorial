from src.analysis import process_data
from src.load_data import load_data
from src.plot_data import plot_data

if __name__ == "__main__":
    print("Loading data...")
    load_data()
    print("Processing data...")
    process_data()
    print("Plotting and saving figure...")
    plot_data()
    print("Done!")
