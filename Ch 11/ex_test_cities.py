import unittest
from ex_city_country import city_country

class CitiesTestCase(unittest.TestCase):
    """
    Test for ex_city_country.py
    """

    def test_city_country(self):
        """
        Do cities like Chandigarh, India work ?
        """
        city_name = city_country("chandigarh", "india")
        self.assertEqual(city_name, "Chandigarh, India")

unittest.main()