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

import pandas as pd
from lux.core.series import LuxSeries
from lux.vis.Clause import Clause
from lux.vis.Vis import Vis
from lux.vis.VisList import VisList
from lux.history.history import History
from lux.utils.date_utils import is_datetime_series
from lux.utils.message import Message
from lux.utils.utils import check_import_lux_widget
from typing import Dict, Union, List, Callable

# from lux.executor.Executor import *
import warnings
import traceback
import lux


class LuxDataFrameMixin:
    """
    A subclass of pd.DataFrame that supports all dataframe operations while housing other variables and functions for generating visual recommendations.
    """

    # MUST register here for new properties!!
    _metadata = [
        "_intent",
        "_inferred_intent",
        "_data_type",
        "unique_values",
        "cardinality",
        "_rec_info",
        "_min_max",
        "_current_vis",
        "_widget",
        "_recommendation",
        "_prev",
        "_history",
        "_saved_export",
        "_sampled",
        "_toggle_pandas_display",
        "_message",
        "_pandas_only",
        "pre_aggregated",
        "_type_override",
    ]

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self._history = History()
        self._intent = []
        self._inferred_intent = []
        self._recommendation = {}
        self._saved_export = None
        self._current_vis = []
        self._prev = None
        self._widget = None

        self.table_name = ""
        if lux.config.SQLconnection == "":
            from lux.executor.PandasExecutor import PandasExecutor

            lux.config.executor = PandasExecutor()
        else:
            from lux.executor.SQLExecutor import SQLExecutor

            # lux.config.executor = SQLExecutor()

        self._sampled = None
        self._approx_sample = None
        self._toggle_pandas_display = True
        self._message = Message()
        self._pandas_only = False
        # Metadata
        self._data_type = {}
        self.unique_values = None
        self.cardinality = None
        self._min_max = None
        self.pre_aggregated = None
        self._type_override = {}
        warnings.formatwarning = lux.warning_format

    @property
    def history(self):
        pass

    @property
    def data_type(self):
        pass

    def compute_metadata(self) -> None:
        """
        Compute dataset metadata and statistics
        """
        pass

    def maintain_metadata(self):
        """
        Maintain dataset metadata and statistics (Compute only if needed)
        """
        pass

    def expire_recs(self) -> None:
        """
        Expires and resets all recommendations
        """
        pass

    def expire_metadata(self) -> None:
        """
        Expire all saved metadata to trigger a recomputation the next time the data is required.
        """
        pass

    #####################
    ## Override Pandas ##
    #####################
    def __getattr__(self, name):
        ret_value = super().__getattr__(name)
        self.expire_metadata()
        self.expire_recs()
        return ret_value

    def _set_axis(self, axis, labels):
        pass

    def _update_inplace(self, *args, **kwargs):
        pass

    def _set_item(self, key, value):
        pass

    def _infer_structure(self):
        # If the dataframe is very small and the index column is not a range index, then it is likely that this is an aggregated data
        pass

    @property
    def intent(self):
        """
        Main function to set the intent of the dataframe.
        The intent input goes through the parser, so that the string inputs are parsed into a lux.Clause object.

        Parameters
        ----------
        intent : List[str,Clause]
                intent list, can be a mix of string shorthand or a lux.Clause object

        Notes
        -----
                :doc:`../guide/intent`
        """
        pass

    @intent.setter
    def intent(self, intent_input: Union[List[Union[str, Clause]], Vis]):
        pass

    def clear_intent(self):
        pass

    def set_intent(self, intent: List[Union[str, Clause]]):
        pass

    def _parse_validate_compile_intent(self):
        pass

    def copy_intent(self):
        # creates a true copy of the dataframe's intent
        pass

    def set_intent_as_vis(self, vis: Vis):
        """
        Set intent of the dataframe based on the intent of a Vis

        Parameters
        ----------
        vis : Vis
            Input Vis object
        """
        pass

    def set_data_type(self, types: dict):
        """
        Set the data type for a particular attribute in the dataframe
        overriding the automatically-detected type inferred by Lux

        Parameters
        ----------
        types: dict
            Dictionary that maps attribute/column name to a specified Lux Type.
            Possible options: "nominal", "quantitative", "id", and "temporal".

        Example
        ----------
        df = pd.read_csv("https://raw.githubusercontent.com/lux-org/lux-datasets/master/data/absenteeism.csv")
        df.set_data_type({"ID":"id",
                          "Reason for absence":"nominal"})
        """
        pass

    def to_pandas(self):
        pass

    @property
    def recommendation(self):
        pass

    @recommendation.setter
    def recommendation(self, recommendation: Dict):
        pass

    @property
    def current_vis(self):
        pass

    @current_vis.setter
    def current_vis(self, current_vis: Dict):
        pass

    def _append_rec(self, rec_infolist, recommendations: Dict):
        pass

    def show_all_column_vis(self):
        pass

    def maintain_recs(self, is_series="DataFrame"):
        # `rec_df` is the dataframe to generate the recommendations on
        # check to see if globally defined actions have been registered/removed
        pass

    #######################################################
    ############## LuxWidget Result Display ###############
    #######################################################
    @property
    def widget(self):
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

    def remove_deleted_recs(self, change):
        pass

    def set_intent_on_click(self, change):
        pass

    def _ipython_display_(self):
        pass

    def display_pandas(self):
        pass

    def render_widget(self, renderer: str = "altair", input_current_vis=""):
        """
        Generate a LuxWidget based on the LuxDataFrame

        Structure of widgetJSON:

        {

            'current_vis': {},
            'recommendation': [

                {

                    'action': 'Correlation',
                    'description': "some description",
                    'vspec': [

                            {Vega-Lite spec for vis 1},
                            {Vega-Lite spec for vis 2},
                            ...

                    ]

                },
                ... repeat for other actions

            ]

        }

        Parameters
        ----------
        renderer : str, optional
                Choice of visualization rendering library, by default "altair"
        input_current_vis : lux.LuxDataFrame, optional
                User-specified current vis to override default Current Vis, by default

        """
        pass

    @staticmethod
    def intent_to_JSON(intent):
        pass

    @staticmethod
    def intent_to_string(intent):
        pass

    def to_JSON(self, rec_infolist, input_current_vis=""):
        pass

    @staticmethod
    def current_vis_to_JSON(vlist, input_current_vis=""):
        pass

    @staticmethod
    def rec_to_JSON(recs):
        pass

    def save_as_html(self, filename: str = "export.html", output=False):
        """
        Save dataframe widget as static HTML file

        Parameters
        ----------
        filename : str
            Filename for the output HTML file
        """
        pass

    # Overridden Pandas Functions
    def head(self, n: int = 5):
        pass

    def tail(self, n: int = 5):
        pass

    def groupby(self, *args, **kwargs):
        pass


class LuxDataFrame(LuxDataFrameMixin, pd.DataFrame):
    @property
    def _constructor(self):
        pass

    @property
    def _constructor_sliced(self):
        pass
