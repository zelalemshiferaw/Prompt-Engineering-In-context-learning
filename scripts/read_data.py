import sys
import os
import pandas as pd
import dvc.api
from logger import logger


sys.path.append(os.path.abspath(os.path.join("./scripts/")))

class ReadData():
    def dvc_get_data(self, path, version='v1') :
        try:
            repo = "/home/zelax/10Accademy/Tenx/Prompt-Engineering-In-context-learning"
            data_url = dvc.api.get_url(path=path, repo=repo, rev=version)
            data_url = str(data_url)[6:]
            df = pd.read_csv(data_url, sep=",", low_memory=False)
            logger.info("Data read")
        except Exception as e:
            df = None
            logger.error(e)
        return df