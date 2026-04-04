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
import lux
from lux.executor.PandasExecutor import PandasExecutor
from lux.executor.SQLExecutor import SQLExecutor
import lux


def custom(ldf):
    """
    Generates user-defined vis based on the intent.

    Parameters
    ----------
    ldf : lux.core.frame
        LuxDataFrame with underspecified intent.

    Returns
    -------
    recommendations : Dict[str,obj]
        object with a collection of visualizations that result from the Distribution action.
    """
    pass


def custom_actions(ldf):
    """
    Generates user-defined vis based on globally defined actions.

    Parameters
    ----------
    ldf : lux.core.frame
        LuxDataFrame with underspecified intent.

    Returns
    -------
    recommendations : Dict[str,obj]
        object with a collection of visualizations that were previously registered.
    """
    pass
