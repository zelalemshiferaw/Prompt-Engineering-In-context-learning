import pandas as pd
import numpy as np
import os
import sys
from logger import logger
from datetime import date, datetime


class CleanDataFrame:
    def remove_null_row(self, df: pd.DataFrame, columns: str) -> pd.DataFrame:
        try:
            for column in columns:
                df = df[~ df[column].isna()]
                logger.info(
                    f'successfully removed empty rows with null {column} column')
        except Exception as e:
            logger.error(e)
        return df
    def drop_duplicates(self, df: pd.DataFrame, subset=None) -> pd.DataFrame:
        """
        This checkes if there are any duplicated entries for a user
        And remove the duplicated rows
        """
        try:
            if subset != None:
                df = df.drop_duplicates(subset='')
            else:
                df = df.drop_duplicates()
            logger.info(f'successfully droped duplicates')
        except Exception as e:
            logger.error(e)
        return df