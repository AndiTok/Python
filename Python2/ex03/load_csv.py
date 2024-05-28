import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    if path.endswith(".csv"):
        try:
            dataset = pd.read_csv(path)
            return dataset
        except (Exception):
            return None
    else:
        return None