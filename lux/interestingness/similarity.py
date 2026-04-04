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

import lux
import pandas as pd
import math
import numpy as np
from lux.vis.VisList import VisList
from lux.utils.utils import get_filter_specs


def interpolate(vis, length):
    """
    Interpolates the vis data so that the number of data points is fixed to a constant

    Parameters
    ----------
    vis : lux.vis.Vis
        vis that represents the candidate visualization
    length : int
        number of points a vis should have

    Returns
    -------
    None
    """
    pass


# interpolate dataset


def normalize(vis):
    """
    Normalizes the vis data so that the range of values is 0 to 1 for the vis

    Parameters
    ----------
    vis : lux.vis.Vis
        vis that represents the candidate visualization
    Returns
    -------
    None
    """
    pass


def euclidean_dist(query_vis, vis):
    """
    Calculates euclidean distance score for similarity between two visualizations

    Parameters
    ----------
    query_vis : lux.vis.Vis
        vis that represents the query pattern
    vis : lux.vis.Vis
        vis that represents the candidate visualization

    Returns
    -------
    score : float
        euclidean distance score
    """
    pass


def preprocess(vis):
    """
    Processes vis data to allow similarity comparisons between visualizations

    Parameters
    ----------
    vis : lux.vis.Vis
        vis that represents the candidate visualization
    Returns
    -------
    None
    """
    pass
