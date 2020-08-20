import abc
from typing import List, Tuple, Union

import pandas as pd


class SyntheticGenerator(abc.ABC):
    """The base class of synthetic data generator.
    """

    def __init__(self):
        pass

    def get_params(self):
        return self.__dict__

    def set_params(self, **kwargs):
        self.__dict__.update(kwargs)

    @abc.abstractmethod
    def generate(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """

        """
        pass


class WaveformGenerator(SyntheticGenerator):
    def __init__(self, sin_coefs: Union[List[List[int, int]], Tuple[Tuple[int, int]]],
                 cos_coefs: Union[List[List[int, int]], Tuple[Tuple[int, int]]], anomaly_ratio: float,
                 missing_ratio: float, anomaly_types: Union[List[str], Tuple[str]], noisy: bool = True):
        """

        Parameters
        ----------
        sin_coefs : list or tuple

        cos_coefs : list or tuple
        anomaly_ratio :
        missing_ratio :
        anomaly_types :
        noisy :
        """
        super(WaveformGenerator, self).__init__()

        pass

    def generate(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """

        Returns
        --------
        pd.DataFrame
            The data DataFrame
        pd.DataFrame
            The meta DataFrame
        """
        pass
