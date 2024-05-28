import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import matplotlib.ticker as ticker


def convert_suffix(str):
    if 'B' in str:
        return float(str.rstrip('B')) * 1000000000  # Convert 'B' to billion
    elif 'M' in str:
        return float(str.rstrip('M')) * 1000000  # Convert 'M' to million
    elif 'k' in str:
        return float(str.rstrip('k')) * 1000  # Convert 'K' to thousand
    else:
        return float(str)


def nb_formatter(x, pos):
    if abs(x) >= 1e9:
        # Format numbers in millions
        return f'{x / 1e9:.0f}B'
    elif abs(x) >= 1e6:
        # Format numbers in millions
        return f'{x / 1e6:.0f}M'
    elif abs(x) >= 1e3:
        # Format numbers in thousands
        return f'{x / 1e3:.0f}k'
    else:
        return f'{x:.0f}'
    # return f'{int(x / 1e6)}M'
    # return str(int(x))


def aff_pop(df: pd.core.frame.DataFrame):
    '''
This program display a graph of Population Projections
of Malaysia against France
    '''
# using list method b converti dataframe obect to list
    # yr = df.columns[1,:-50] # years
    # test = df.columns[1,:-50].tolist() # years in list
    # test = df.iloc[123,:-50].values.tolist() # a country in a list

# auto use x axis from df
    ms = df.iloc[123, 1:-50] # Malaysia
    bg = df.iloc[12, 1:-50] # Belgium
    pf = df.iloc[58, 1:-50] # ParisFrance
    # find = df.loc[12]
    # print (find)
    # print(test)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    mss = ms.apply(convert_suffix)
    pff = pf.apply(convert_suffix)
    bgg = bg.apply(convert_suffix)
    # plt.plot(yr,mss, label='Malaysia',color='orange') # specify x and y if use list
    plt.plot(mss, label='Malaysia',color='orange')
    plt.plot(bgg, label='Belgium',color='cyan')
    plt.plot(pff, label='France',color='green')

# subplot testing
    # x = range(1800, 2051)
    # pf = pf.str.rstrip('M').astype(float)
    # fig, ax = plt.subplots()
    # ax.plot(x, pf)
    # ax.set_yticks(range(0, 70, 20))
    # ax.set_xticks(range(1800, 2101, 40))
    # ax.set_xlabel('Year')
    # ax.set_ylabel('Population')
    # ax.set_title('Population Projections')

# x ticks 
    x_ticks = ticker.MultipleLocator(base=40)
    plt.gca().xaxis.set_major_locator(x_ticks)

# specif number of tick to show for y-axis ticks
    # plt.locator_params(axis='y', nbins=4)

# another ways to hande y ticks, chose either 1 and use plt.gcs()...
    # y_ticks = ticker.MaxNLocator(nbins=4)
    # y_ticks = ticker.AutoLocator()
    # y_ticks = ticker.LinearLocator(5)
    y_ticks = ticker.MultipleLocator(base=20000000)
 
    plt.gca().yaxis.set_major_locator(y_ticks)

# hard code way to format
    # y_axis_ticks = [0, 20_000_000, 40_000_000, 60_000_000]
    # y_axis_labels = ['', '20M', '40M', '60M']
    # plt.yticks(y_axis_ticks, y_axis_labels)

# y ticks formatter, similar to hard code above
    y_formatter = ticker.FuncFormatter(nb_formatter)
    plt.gca().yaxis.set_major_formatter(y_formatter)

# axis limit if needed
    # plt.xlim(-10,270)
    # plt.ylim(top=70e6)

# others
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()


def main():
# your tests and your error handling
    # print(load("life_expectancy_years.csv"))
    aff_pop(load("population_total.csv"))
    # print(aff_pop.__doc__)


if __name__ == "__main__":
    main()