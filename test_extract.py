import unittest
from utils.extract import scrape_data
import pandas as pd

class TestExtract(unittest.TestCase):
    def test_scrape_data_returns_dataframe(self):
        # Pakai URL dummy yang tidak akan berhasil, memastikan return DataFrame
        df = scrape_data("https://notarealwebsiteforsure.com/")
        self.assertIsInstance(df, pd.DataFrame)

    def test_scrape_data_empty_on_invalid_url(self):
        df = scrape_data("https://notarealwebsiteforsure.com/")
        self.assertTrue(df.empty)

if __name__ == "__main__":
    unittest.main()
