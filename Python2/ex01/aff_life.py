import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(df: pd.core.frame.DataFrame):
    '''
This program display a graph of Malaysia Life expectancy Projection
    '''
   # iloc uses 2d (row,col) while loc uses 1D (row)
    # country = df.loc[123]
    # print(country)
    ms = df.iloc[123, 1:] # Malaysia
    # ms = df.iloc[58, 1:] # ParisFrance
    # print(ms)
    # ystart = int(df.columns[1])
    # yend = int(df.columns[-1])
    # print(ystart)
    # print(yend)
    plt.plot(ms)

    # Customize graph
    plt.title("Malaysia Life Expectancy Projecion")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    x_ticks =  df.columns[1::40]
    plt.xticks(x_ticks)
    # plt.xticks(rotation=45)
    # plt.xticks(x_ticks, rotation=45)
    # plt.grid(True)
    # plt.legend()
    plt.tight_layout()
    plt.show()


def main():
# your tests and your error handling
    # print(load("life_expectancy_years.csv"))
    aff_life(load("life_expectancy_years.csv"))
    # print(aff_life.__doc__)


if __name__ == "__main__":
    main()