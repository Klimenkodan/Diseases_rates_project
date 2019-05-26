import requests
from config import URL, FILE_NAME


def create_parameter_list(parameter_list):
    """
    Helper function to create a parameter list from a dictionary object
    """

    parameter_string = ""

    for key in parameter_list:
        parameter_string += "<parameter>\n"
        parameter_string += "<name>" + key + "</name>\n"

        if isinstance(parameter_list[key], list):
            for value in parameter_list[key]:
                parameter_string += "<value>" + value + "</value>\n"
        else:
            parameter_string += "<value>" + parameter_list[key] + "</value>\n"

        parameter_string += "</parameter>\n"
    return parameter_string


if __name__ == '__main__':

    b_parameters = {
        "B_1": "D76.V1-level1",
        "B_2": "D76.V23",
        "B_3": "*None*",
        "B_4": "*None*",
        "B_5": "*None*"
    }

    m_parameters = {
        "M_1": "D76.M1",  # Deaths, must be included
        "M_2": "D76.M2",  # Population, must be included
        "M_3": "D76.M3",  # Crude rate, must be included
        "M_41": "D76.M41",  # Standard error (age-adjusted rate)
        "M_42": "D76.M42"  # 95% confidence interval (age-adjusted rate)
    }

    f_parameters = {
        "F_D76.V1": ["*All*"],  # year/month
        "F_D76.V10": ["*All*"],  # Census Regions - dont change
        "F_D76.V2": ["*All*"],  # ICD-10 Codes
        "F_D76.V27": ["*All*"],  # HHS Regions - dont change
        "F_D76.V9": ["*All*"]  # State County - dont change
    }

    i_parameters = {
        "I_D76.V1": "*All* (All Dates)",  # year/month
        "I_D76.V10": "*All* (The United States)",  # Census Regions - dont change
        "I_D76.V2": "*All*",  # ICD-10 Codes
        "I_D76.V27": "*All* (The United States)",  # HHS Regions - dont change
        "I_D76.V9": "*All* (The United States)"  # State County - dont change
    }

    v_parameters = {
        "V_D76.V1": "",  # Year/Month
        "V_D76.V10": "",  # Census Regions
        "V_D76.V11": "*All*",  # 2006 Urbanization
        "V_D76.V12": "*All*",  # ICD-10 130 Cause List (Infants)
        "V_D76.V17": "*All*",  # Hispanic Origin
        "V_D76.V19": "*All*",  # 2013 Urbanization
        "V_D76.V2": "",  # ICD-10 Codes
        "V_D76.V20": "*All*",  # Autopsy
        "V_D76.V21": "*All*",  # Place of Death
        "V_D76.V22": "*All*",  # Injury Intent
        "V_D76.V23": "*All*",  # Injury Mechanism and All Other Leading Causes
        "V_D76.V24": "*All*",  # Weekday
        "V_D76.V25": "*All*",  # Drug/Alcohol Induced Causes
        "V_D76.V27": "",  # HHS Regions
        "V_D76.V4": "*All*",  # ICD-10 113 Cause List
        "V_D76.V5": ["15-24", "25-34", "35-44", "45-54"],  # Ten-Year Age Groups
        "V_D76.V51": "*All*",  # Five-Year Age Groups
        "V_D76.V52": "*All*",  # Single-Year Ages
        "V_D76.V6": "00",  # Infant Age Groups
        "V_D76.V7": "*All*",  # Gender
        "V_D76.V8": "*All*",  # Race
        "V_D76.V9": ""  # State/County
    }

    o_parameters = {
        "O_V10_fmode": "freg",  # Use regular finder and ignore v parameter value
        "O_V1_fmode": "freg",  # Use regular finder and ignore v parameter value
        "O_V27_fmode": "freg",  # Use regular finder and ignore v parameter value
        "O_V2_fmode": "freg",  # Use regular finder and ignore v parameter value
        "O_V9_fmode": "freg",  # Use regular finder and ignore v parameter value
        "O_aar": "aar_std",  # age-adjusted rates
        "O_aar_pop": "0000",  # population selection for age-adjusted rates
        "O_age": "D76.V5",  # select age-group (e.g. ten-year, five-year, single-year, infant groups)
        "O_javascript": "on",  # Set to on by default
        "O_location": "D76.V9",  # select location variable to use (e.g. state/county, census, hhs regions)
        "O_precision": "1",  # decimal places
        "O_rate_per": "100000",  # rates calculated per X persons
        "O_show_totals": "false",  # Show totals for
        "O_timeout": "300",
        "O_title": "",  # title for data run
        "O_ucd": "D76.V2",  # select underlying cause of death category
        "O_urban": "D76.V19"  # select urbanization category
    }

    vm_parameters = {
        "VM_D76.M6_D76.V10": "",  # Location
        "VM_D76.M6_D76.V17": "*All*",  # Hispanic-Origin
        "VM_D76.M6_D76.V1_S": "*All*",  # Year
        "VM_D76.M6_D76.V7": "*All*",  # Gender
        "VM_D76.M6_D76.V8": "*All*"  # Race
    }

    misc_parameters = {
        "action-Send": "Send",
        "finder-stage-D76.V1": "codeset",
        "finder-stage-D76.V2": "codeset",
        "finder-stage-D76.V27": "codeset",
        "finder-stage-D76.V9": "codeset",
        "stage": "request"
    }

    xml_request = "<request-parameters>\n"
    xml_request += create_parameter_list(b_parameters)
    xml_request += create_parameter_list(m_parameters)
    xml_request += create_parameter_list(f_parameters)
    xml_request += create_parameter_list(i_parameters)
    xml_request += create_parameter_list(o_parameters)
    xml_request += create_parameter_list(vm_parameters)
    xml_request += create_parameter_list(v_parameters)
    xml_request += create_parameter_list(misc_parameters)
    xml_request += "</request-parameters>"

    url = URL

    response = requests.post(url, data={"request_xml": xml_request, "accept_datause_restrictions": "true"})

    if response.status_code == 200:
        data = response.text
        file = open(FILE_NAME, 'w')
        file.write(data)
        file.close()

    else:
        print("something went wrong")
