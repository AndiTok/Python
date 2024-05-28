import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    '''
    a function that takes a path as argument, 
    writes the dimensions of the data set and returns it
    '''
    if path.endswith(".csv"):
        try:
            dataset = pd.read_csv(path)
            # row, col = dataset.shape
            # print(type(dataset))
            # print(f"Loading dataset of dimensions ({row}, {col})")
            # return dataset.to_string()
            return dataset
        except (Exception):# as e:
            # print(f"An error occurred: {e}")
            return None
    else:
        return None