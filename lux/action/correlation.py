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
from lux.interestingness.interestingness import interestingness
from lux.processor.Compiler import Compiler
from lux.core.frame import LuxDataFrame
from lux.vis.VisList import VisList
from lux.utils import utils


# change ignore_transpose to false for now.
def correlation(ldf: LuxDataFrame, ignore_transpose: bool = True):
    """
    Generates bivariate visualizations that represent all pairwise relationships in the data.

    Parameters
    ----------
    ldf : LuxDataFrame
            LuxDataFrame with underspecified intent.

    ignore_transpose: bool
            Boolean flag to ignore pairs of attributes whose transpose are already computed (i.e., {X,Y} will be ignored if {Y,X} is already computed)

    Returns
    -------
    recommendations : Dict[str,obj]
            object with a collection of visualizations that result from the Correlation action.
    """
    pass


def check_transpose_not_computed(vlist: VisList, a: str, b: str):
    pass
