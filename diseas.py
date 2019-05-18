from predicting import linear_regression
from parse import analyzing
from config import FILE_NAME, MAXIMUM_YEAR, MINIMUM_YEAR, PHRASE
import matplotlib.pyplot as plt


class Disease:
    """
    This class represents the disease
    """
    def __init__(self, name):
        """
        (str) -> None
        This method initializes the object of the current class
        """
        self.info = analyzing(FILE_NAME)[name]
        self.name = name

    def predicting(self, value):
        """
        This method makes the prediction of death rate for the given year
        :param value: int
        :return: list
        """
        return linear_regression(self.info, value)

    def graphic(self, value=None):
        """
        This method makes the plot of the information for the death rates.
        :param value: int
        :return: None
        """
        plt.figure()
        x_dots = []
        y_dots = []
        for element in self.info.keys():
            y_dots.append(self.info[element])
            x_dots.append(int(element))
        plt.plot(x_dots, y_dots)

        if value:
            plt.scatter(value[1], value[0])
            plt.text(value[1], value[0], f'Predicted for year {value[1]}')

        plt.text(MAXIMUM_YEAR - 7, self.average_value(), f'Plot on the\
{self.name[len(PHRASE):] if self.name.startswith(PHRASE) else self.name} disease')

        plt.grid(True)

        plt.show()

    def max_value(self):
        """
        This method returns the biggest value for specified years.
        :return: tuple
        """
        maximum = 0
        max_year = 0
        for year in self.info:
            if self.info[year] > maximum:
                maximum = self.info[year]
                max_year = year

        return maximum, max_year

    def min_value(self):
        """
        This method returns the smallest value for specified years.
        :return: tuple
        """
        minimum = self.max_value()[0]
        min_year = MINIMUM_YEAR
        for year in self.info:
            if self.info[year] < minimum:
                minimum = self.info[year]
                min_year = year

        return minimum, min_year

    def average_value(self):
        """
        This method returns the average value.
        :return: int
        """
        return sum(self.info.values()) // len(self.info.values())

    def average_changing(self):
        """
        This method returns the average changing of the death rate of the disease.
        :return: str
        """
        year_lst = sorted(list(self.info.keys()))
        change_lst = []
        for index in range(len(year_lst)):
            if index + 1 <= len(year_lst) - 1:
                change_lst.append(self.info[year_lst[index + 1]] - self.info[year_lst[index]])

        average_ch = sum(change_lst) // len(change_lst)
        new_str = 'Annual decrease is: ' if average_ch <= 0 else 'Annual increase is: '
        new_str += str(abs(average_ch)) + ' people\n'
        return new_str


if __name__ == '__main__':
    disease = Disease('Non-Injury: Tuberculosis')
    print(disease.info)
    print(disease.max_value())
    print(disease.average_value())
    print(disease.predicting(2018))
    print(disease.average_changing())
    disease.graphic([65, 2018])
