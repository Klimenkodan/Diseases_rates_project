import xmltodict
from config import NAME_DISEASE, FILE_NAME, YEAR, VALUE, NUM_DEATHS


def analyzing(file_name):
    """
    This function parses the xml file and returns the dict.
    :param file_name: str
    :return: dict
    """

    diseases_dict = dict()
    file = open(file_name, 'r')
    xml_inf = file.read()
    file.close()
    dictionary = xmltodict.parse(str(xml_inf))
    diseases = dictionary['page']['response']['data-table']['r']
    for disease in diseases:
        num_deaths = int(disease["c"][NUM_DEATHS]['@v'].replace(',', ''))
        disease_name = disease["c"][NAME_DISEASE]["@l"]
        year = disease["c"][YEAR]["@l"]
        if num_deaths > VALUE:
            if disease_name in diseases_dict:
                diseases_dict[disease_name][year] = num_deaths
            else:
                diseases_dict[disease_name] = dict()
                diseases_dict[disease_name][year] = num_deaths
    return diseases_dict


if __name__ == '__main__':
    print(analyzing(FILE_NAME))
    print(analyzing(FILE_NAME)['Cut/Pierce'])

