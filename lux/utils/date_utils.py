#  Copyright 2019-2020 The Lux Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import re
from typing import Any

import lux
import pandas as pd
import numpy as np

timedelta_re = re.compile(r"^timedelta64\[\w+\]$")


def is_timedelta64_series(series: pd.Series) -> bool:
    """
    Check if the Series object is of timedelta64 type

    Parameters
    ----------
    series : pd.Series

    Returns
    -------
    is_date: bool
    """
    pass


def timedelta64_to_float_seconds(series: pd.Series) -> pd.Series:
    """
    Convert a timedelta64 Series to a float Series in seconds

    Parameters
    ----------
    series : pd.Series

    Returns
    -------
    series: pd.Series
    """
    pass


def date_formatter(time_stamp, ldf):
    """
    Given a numpy timestamp and ldf, inspects which date granularity is appropriate and reformats timestamp accordingly

    Example
    ----------
    For changing granularity the results differ as so.
    days: '2020-01-01' -> '2020-1-1'
    months: '2020-01-01' -> '2020-1'
    years: '2020-01-01' -> '2020'

    Parameters
    ----------
    time_stamp: np.datetime64
            timestamp object holding the date information
    ldf : lux.core.frame
            LuxDataFrame with a temporal field

    Returns
    -------
    date_str: str
            A reformatted version of the time_stamp according to granularity
    """
    pass


def compute_date_granularity(date_column: pd.core.series.Series):
    """
    Given a temporal column (pandas.core.series.Series), finds out the granularity of dates.

    Example
    ----------
    ['2018-01-01', '2019-01-02', '2018-01-03'] -> "day"
    ['2018-01-01', '2019-02-01', '2018-03-01'] -> "month"
    ['2018-01-01', '2019-01-01', '2020-01-01'] -> "year"

    Parameters
    ----------
    date_column: pandas.core.series.Series
            Column series with datetime type

    Returns
    -------
    field: str
            A str specifying the granularity of dates for the inspected temporal column
    """
    pass


def is_datetime_series(series: pd.Series) -> bool:

    """
    Check if the Series object is of datetime type

    Parameters
    ----------
    series : pd.Series

    Returns
    -------
    is_date: bool
    """
    pass


def is_datetime_string(string: str) -> bool:
    """
    Check if the string is date-like.

    Parameters
    ----------
    string : str

    Returns
    -------
    is_date: bool
    """
    pass
