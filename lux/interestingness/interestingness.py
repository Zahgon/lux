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

from lux.core.frame import LuxDataFrame
from lux.vis.Vis import Vis
from lux.executor.PandasExecutor import PandasExecutor
from lux.utils import utils

import pandas as pd
import numpy as np
from pandas.api.types import is_datetime64_any_dtype as is_datetime
from scipy.spatial.distance import euclidean
import lux
from lux.utils.utils import get_filter_specs
from lux.interestingness.similarity import preprocess, euclidean_dist
from lux.vis.VisList import VisList
import warnings


def interestingness(vis: Vis, ldf: LuxDataFrame) -> int:
    """
    Compute the interestingness score of the vis.
    The interestingness metric is dependent on the vis type.

    Parameters
    ----------
    vis : Vis
    ldf : LuxDataFrame

    Returns
    -------
    int
            Interestingness Score
    """
    pass


def get_filtered_size(filter_specs, ldf):
    pass


def skewness(v):
    pass


def weighted_avg(x, w):
    pass


def weighted_cov(x, y, w):
    pass


def weighted_correlation(x, y, w):
    # Based on https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#Weighted_correlation_coefficient
    pass


def deviation_from_overall(
    vis: Vis,
    ldf: LuxDataFrame,
    filter_specs: list,
    msr_attribute: str,
    exclude_nan: bool = True,
) -> int:
    """
    Difference in bar chart/histogram shape from overall chart
    Note: this function assumes that the filtered vis.data is operating on the same range as the unfiltered vis.data.

    Parameters
    ----------
    vis : Vis
    ldf : LuxDataFrame
    filter_specs : list
            List of filters from the Vis
    msr_attribute : str
            The attribute name of the measure value of the chart
    exclude_nan: bool
            Whether to include/exclude NaN values as part of the deviation calculation

    Returns
    -------
    int
            Score describing how different the vis is from the overall vis
    """
    pass


def unevenness(vis: Vis, ldf: LuxDataFrame, measure_lst: list, dimension_lst: list) -> int:
    """
    Measure the unevenness of a bar chart vis.
    If a bar chart is highly uneven across the possible values, then it may be interesting. (e.g., USA produces lots of cars compared to Japan and Europe)
    Likewise, if a bar chart shows that the measure is the same for any possible values the dimension attribute could take on, then it may not very informative.
    (e.g., The cars produced across all Origins (Europe, Japan, and USA) has approximately the same average Acceleration.)

    Parameters
    ----------
    vis : Vis
    ldf : LuxDataFrame
    measure_lst : list
            List of measures
    dimension_lst : list
            List of dimensions
    Returns
    -------
    int
            Score describing how uneven the bar chart is.
    """
    pass


def mutual_information(v_x: list, v_y: list) -> int:
    # Interestingness metric for two measure attributes
    # Calculate maximal information coefficient (see Murphy pg 61) or Pearson's correlation
    pass


def monotonicity(vis: Vis, attr_specs: list, ignore_identity: bool = True) -> int:
    """
    Monotonicity measures there is a monotonic trend in the scatterplot, whether linear or not.
    This score is computed as the Pearson's correlation on the ranks of x and y.
    See "Graph-Theoretic Scagnostics", Wilkinson et al 2005: https://research.tableau.com/sites/default/files/Wilkinson_Infovis-05.pdf
    Parameters
    ----------
    vis : Vis
    attr_spec: list
            List of attribute Clause objects

    ignore_identity: bool
            Boolean flag to ignore items with the same x and y attribute (score as -1)

    Returns
    -------
    int
            Score describing the strength of monotonic relationship in vis
    """
    pass


def n_distinct(vis: Vis, dimension_lst: list, measure_lst: list) -> int:
    """
    Computes how many unique values there are for a dimensional data type.
    Ignores attributes that are latitude or longitude coordinates.

    For example, if a dataset displayed earthquake magnitudes across 48 states and
    3 countries, return 48 and 3 respectively.

    Parameters
    ----------
    vis : Vis
    dimension_lst: list
            List of dimension Clause objects.
    measure_lst: list
            List of measure Clause objects.

    Returns
    -------
    int
            Score describing the number of unique values in the dimension.
    """
    pass
