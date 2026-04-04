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
from lux.vis.VisList import VisList
from lux.vis.Vis import Vis
import pandas as pd
from lux.core.frame import LuxDataFrame
from lux.interestingness.interestingness import interestingness
from lux.utils import utils


def temporal(ldf):
    """
    Generates line charts for temporal fields at different granularities.
    Parameters
    ----------
    ldf : lux.core.frame
            LuxDataFrame with underspecified intent.
    Returns
    -------
    recommendations : Dict[str,obj]
            Object with a collection of visualizations that result from the Temporal action.
    """
    pass


def create_temporal_vis(ldf, col):
    """
    Creates and populates Vis objects for different timescales in the provided temporal column.
    Parameters
    ----------
    ldf : lux.core.frame
            LuxDataFrame with underspecified intent.

    col : str
            Name of temporal column.

    Returns
    -------
    vlist : [Vis]
            Collection of Vis objects.
    """
    pass
