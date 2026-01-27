from ch11_ex01_city_country_functions import formatted_city_country

def test_city_country():
    """Do combinations like 'Santiago, Chile' work?"""
    city_country = formatted_city_country('santiago', 'chile')
    assert city_country == 'Santiago, Chile'