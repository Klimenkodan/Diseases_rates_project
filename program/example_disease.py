from diseas import Disease


if __name__ == '__main__':
    """
    This module represents the work of the class Disease
    """
    new_disease = Disease('Cut/Pierce')
    print(new_disease.average_changing())
    print(new_disease.average_value())
    print(new_disease.max_value())
    print(new_disease.min_value())
    new_disease.graphic()
    print(new_disease.predicting(2018))
    print(new_disease.info)
    print(new_disease.name)