from sklearn.linear_model import LinearRegression
import pandas as pd


def making_suitable(info):
    """
    This function make the information available for data frame
    """
    coordinates_lst = list()
    for year in info.keys():
        coordinates_lst.append({'x': int(year), 'y': info[year]})
    return coordinates_lst


def linear_regression(info, value):
    """
    This function make prediction using linear regression.
    """
    data = making_suitable(info)
    new_data = pd.DataFrame(data)
    x = new_data.iloc[:, 0:1].values
    y = new_data.iloc[:, 1].values
    lin2 = LinearRegression()
    lin2.fit(x, y)
    return lin2.predict([[value]])

