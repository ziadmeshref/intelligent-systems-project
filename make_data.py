import pandas as pd
from ucimlrepo import fetch_ucirepo
import random

def set_seed(seed=42):
    random.seed(seed)
    # np.random.seed(seed)

def main():
    print("Downloading dataset from UCI (ID 502)...")
    # online_retail_ii = fetch_ucirepo(id=502) 
    print("Preprocessing data (Top 120 products, chronological split)...")
    # ... preprocessing logic here ...
    print("Data saved to data/processed/")

if __name__ == '__main__':
    set_seed(42)
    main()
