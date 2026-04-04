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
from __future__ import annotations

import pandas as pd
import lux
import warnings
import traceback
import numpy as np
from lux.history.history import History
from lux.utils.message import Message
from lux.vis.VisList import VisList
from typing import Dict, Union, List, Callable


class LuxSeriesMixin:
    """
    A subclass of pd.Series that supports all 1-D Series operations
    """

    _metadata = [
        "_intent",
        "_inferred_intent",
        "_data_type",
        "unique_values",
        "cardinality",
        "_rec_info",
        "_min_max",
        "plotting_style",
        "_current_vis",
        "_widget",
        "_recommendation",
        "_prev",
        "_history",
        "_saved_export",
        "name",
        "_sampled",
        "_toggle_pandas_display",
        "_message",
        "_pandas_only",
        "pre_aggregated",
        "_type_override",
        "name",
    ]

    _default_metadata = {
        "_intent": list,
        "_inferred_intent": list,
        "_current_vis": list,
        "_recommendation": list,
        "_toggle_pandas_display": lambda: True,
        "_pandas_only": lambda: False,
        "_type_override": dict,
        "_history": History,
        "_message": Message,
    }

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for attr in self._metadata:
            if attr in self._default_metadata:
                self.__dict__[attr] = self._default_metadata[attr]()
            else:
                self.__dict__[attr] = None

    def to_pandas(self) -> pd.Series:
        """
        Convert Lux Series to Pandas Series

        Returns
        -------
        pd.Series
        """
        pass

    def unique(self):
        """
        Overridden method for pd.Series.unique with cached results.
        Return unique values of Series object.
        Uniques are returned in order of appearance. Hash table-based unique,
        therefore does NOT sort.
        Returns
        -------
        ndarray or ExtensionArray
            The unique values returned as a NumPy array.
        See Also
        --------
        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html
        """
        pass

    def _ipython_display_(self):
        pass

    @property
    def recommendation(self):
        pass

    @property
    def exported(self) -> Union[Dict[str, VisList], VisList]:
        """
        Get selected visualizations as exported Vis List

        Notes
        -----
        Convert the _selectedVisIdxs dictionary into a programmable VisList
        Example _selectedVisIdxs :

            {'Correlation': [0, 2], 'Occurrence': [1]}

        indicating the 0th and 2nd vis from the `Correlation` tab is selected, and the 1st vis from the `Occurrence` tab is selected.

        Returns
        -------
        Union[Dict[str,VisList], VisList]
                When there are no exported vis, return empty list -> []
                When all the exported vis is from the same tab, return a VisList of selected visualizations. -> VisList(v1, v2...)
                When the exported vis is from the different tabs, return a dictionary with the action name as key and selected visualizations in the VisList. -> {"Enhance": VisList(v1, v2...), "Filter": VisList(v5, v7...), ..}
        """
        pass

    def groupby(self, *args, **kwargs):
        pass


class LuxSeries(LuxSeriesMixin, pd.Series):
    @property
    def _constructor(self):
        pass

    @property
    def _constructor_expanddim(self):
        pass
