import unittest
from .models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    """
    Test class to test the behaviour of the Source class
    """
    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_source = Source("news", "More News", "Get the latest updates", "https://aljazeera.com", "getnews", "eng", "end")

    def test_instance(self):  # uses the isinstance function to check if object self.new_source is an instance of the Source class
        self.assertTrue(isinstance(self.new_source, Source))

    def test_to_check_instance_variables(self):
        """
        Test function to check the variable instances
        """
        self.assertEqual(self.new_source.id, "news")
        self.assertEqual(self.new_source.name, "More News")
        self.assertEqual(self.new_source.description, "Get the latest updates")
        self.assertEqual(self.new_source.url, "https://aljazeera.com")
        self.assertEqual(self.new_source.category, "getnews")
        self.assertEqual(self.new_source.language, "eng")
        self.assertEqual(self.new_source.country, "end")


if __name__ == '__main__':
    unittest.main()
