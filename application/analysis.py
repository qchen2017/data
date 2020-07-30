
import math
import numpy as np

class Analysis(object):

    @staticmethod
    def get_mean(df):
        return df.mean(axis=0)
