import unittest
from ex_population import city_country

class CitiesTestCase(unittest.TestCase):
    """
    Test for ex_population.py
    """

    def test_city_country(self):
        """
        Do cities like 'Chandigrah, India' work ?
        """
        city_name = city_country("chandigarh", "india")
        self.assertEqual(city_name, "Chandigarh, India")
    
    def test_city_country_population(self):
        """
        Do cities like 'Chandigarh, India - population 50000000' work ?
        """
        city_name = city_country("chandigarh", "india", 50000000)
        self.assertEqual(city_name, "Chandigarh, India - population 50000000")

unittest.main()