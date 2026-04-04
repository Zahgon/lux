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

from lux.interestingness.interestingness import interestingness
from lux.vis.VisList import VisList
import lux
from lux.utils import utils


def univariate(ldf, *args):
    """
    Generates bar chart distributions of different attributes in the dataframe.

    Parameters
    ----------
    ldf : lux.core.frame
            LuxDataFrame with underspecified intent.

    data_type_constraint: str
            Controls the type of distribution chart that will be rendered.

    Returns
    -------
    recommendations : Dict[str,obj]
            object with a collection of visualizations that result from the Distribution action.
    """
    pass
