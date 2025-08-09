import unittest
from utils.transform import transform_data
import pandas as pd

class TestTransform(unittest.TestCase):
    def test_transform_returns_dataframe(self):
          
        df = pd.DataFrame({
        "Title": ["Test"],
        "Price": ["$12345"],  # String, bukan angka!
        "Rating": ["4.5 out of 5"],
        "Colors": ["3 colors"],
        "Size": ["Size: M"],
        "Gender": ["Gender: Man"],
        "Timestamp": ["2024-01-01T00:00:00"]
})

        result = transform_data(df)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIn("Title", result.columns)
        self.assertIn("Price", result.columns)

    def test_transform_empty(self):
        df = pd.DataFrame()
        result = transform_data(df)
        self.assertTrue(result.empty)

if __name__ == "__main__":
    unittest.main()
