from ch11_ex02_population import formatted_city_country

def test_city_country():
    """Do combinations like 'Santiago, Chile' work?"""
    city_country = formatted_city_country('santiago', 'chile', 5000000)
    assert city_country == 'Santiago, Chile - population 5000000'