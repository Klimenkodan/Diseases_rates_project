from sklearn.linear_model import LinearRegression
import pandas as pd


def making_suitable(info):
    """
    This function make the information available for data frame
    :param info: dict
    :return: list
    """
    coordinates_lst = list()
    for year in info.keys():
        coordinates_lst.append({'x': int(year), 'y': info[year]})
    return coordinates_lst


def linear_regression(info, value):
    """
    This function make prediction using linear regression.
    :param info: dict
    :param value: int
    :return: list
    """
    data = making_suitable(info)
    new_data = pd.DataFrame(data)
    x = new_data.iloc[:, 0:1].values
    y = new_data.iloc[:, 1].values
    lin2 = LinearRegression()
    lin2.fit(x, y)
    return lin2.predict([[value]])


if __name__ == '__main__':
    a = {'1999': 1919, '2000': 1830, '2001': 2037, '2002': 2171, '2003': 2197, '2004': 2205, '2005': 2241, '2006': 2208, '2007': 2136, '2008': 2223, '2009': 2046, '2010': 1971, '2011': 1948, '2012': 1950, '2013': 1797, '2014': 1843, '2015': 1753, '2016': 1938}
    print(linear_regression(a, 2017))

