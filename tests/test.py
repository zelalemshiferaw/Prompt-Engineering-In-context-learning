import unittest
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join("../Prompt-Engineering-In-context-learning/")))

from scripts import clean_data

class TestDataClean(unittest.TestCase):
    def setUp(self) -> None:
        self.cleaner = clean_data.drop_duplicates()