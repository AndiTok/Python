import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import matplotlib.ticker as ticker


def rt_format(x, pos):
    if x >= 1000:
        return f'{x/1000:.2f}k'
    else:
        return x
        # return f'{x:.0f}'


def ft_major_format(x, pos):
    if x == 1000:
        return "1K"
    elif x == 10000:
        return "10K"
    else:
        return f'{x:.2f}'


def ft_minor_format(x, pos):
    if x == 300:
        return "300"
    else:
        return ''


def projection_life():
    '''
This program display a scatter plot graph of 
world countries GDP & Life expetancy for the year 1900
    '''
# extract data
    gdp=load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    lex=load("life_expectancy_years.csv")
    gdp = gdp.loc[:,"1900"].values.tolist() # 000
    lex = lex.loc[:,"1900"].values.tolist() # 33.3
    # print(lex)

# legends
    plt.title("1900")
    plt.xlabel("Gross dometic product")
    plt.ylabel("Life Expectancy")
    
# attemp 1
    # x_axis_ticks = list(range(300,1001,100)) + list(range(1000,10001,1000))
    # # print(x_axis_ticks)
    # x_axis_labels = ['300','','','','','','','1k', '10k']
    # # plt.xticks(x_axis_ticks, x_axis_labels)

# attemp 2
    # x_big = ticker.FixedLocator([0,300, 1000, 10000])
    # plt.gca().xaxis.set_major_locator(x_big)

    # x_lst = list(range(400,901,100)) + list(range(2000,9001,1000))
    # x_lst = [0,200,378,534,667,778,867,934,978,1000]
    # x_small = ticker.FixedLocator(x_lst)
    # plt.gca().xaxis.set_minor_locator(x_small)

# attemp 3
    plt.xscale("log")

    major = ticker.FuncFormatter(ft_major_format)
    plt.gca().xaxis.set_major_formatter(major)

    minor = ticker.FuncFormatter(ft_minor_format)
    plt.gca().xaxis.set_minor_formatter(minor)

    plt.xlim(left=300,right=11000)
    plt.scatter(gdp, lex)

# the rt way
    # ax = plt.gca()
    # major = ticker.FuncFormatter(ft_major_format)
    # plt.xscale("log")
    # ax.xaxis.set_major_formatter(major)
    # plt.scatter(gdp, lex) # 1st
    # plt.xticks([300,1000,10000]) # 2nd

# Note: is better to plt.plot/scatter()... BEFORE doing any formating
# example above rt way try swapping 1st and 2nd see for urself 
    plt.show()


def main():
# your tests and your error handling
    # print(load("life_expectancy_years.csv"))
    projection_life()
    # print( projection_life.__doc__)


if __name__ == "__main__":
    main()