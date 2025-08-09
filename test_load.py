import unittest
import os
import pandas as pd
from utils.load import load_data

class TestLoad(unittest.TestCase):
    def test_load_data_creates_csv(self):
        df = pd.DataFrame({
            "Title": ["Test"],
            "Price": [12345],
            "Rating": [4.5],
            "Colors": [3],
            "Size": ["M"],
            "Gender": ["Man"],
            "Timestamp": ["2024-01-01T00:00:00"]
        })
        filename = "test_products.csv"
        load_data(df, filename)
        self.assertTrue(os.path.exists(filename))
        # Cleanup
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
