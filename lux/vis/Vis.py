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

from typing import List, Callable, Union
from lux.vis.Clause import Clause
from lux.utils.utils import check_import_lux_widget
import lux
import warnings


class Vis:
    """
    Vis Object represents a collection of fully fleshed out specifications required for data fetching and visualization.
    """

    def __init__(self, intent, source=None, title="", score=0.0):
        self._intent = intent  # user's original intent to Vis
        self._inferred_intent = intent  # re-written, expanded version of user's original intent
        self._source = source  # original data attached to the Vis
        self._vis_data = None  # processed data for Vis (e.g., selected, aggregated, binned)
        self._code = None
        self._mark = ""
        self._min_max = {}
        self._postbin = None
        self.title = title
        self.score = score
        self._all_column = False
        self.approx = False
        self.refresh_source(self._source)

    def __repr__(self):
        all_clause = all([isinstance(unit, lux.Clause) for unit in self._inferred_intent])
        if all_clause:
            filter_intents = None
            channels, additional_channels = [], []
            for clause in self._inferred_intent:

                if hasattr(clause, "value"):
                    if clause.value != "":
                        filter_intents = clause
                if hasattr(clause, "attribute"):
                    if clause.attribute != "":
                        if clause.aggregation != "" and clause.aggregation is not None:
                            attribute = f"{clause._aggregation_name.upper()}({clause.attribute})"
                        elif clause.bin_size > 0:
                            attribute = f"BIN({clause.attribute})"
                        else:
                            attribute = clause.attribute
                        if clause.channel == "x":
                            channels.insert(0, [clause.channel, attribute])
                        elif clause.channel == "y":
                            channels.insert(1, [clause.channel, attribute])
                        elif clause.channel != "":
                            additional_channels.append([clause.channel, attribute])

            channels.extend(additional_channels)
            str_channels = ""
            for channel in channels:
                str_channels += f"{channel[0]}: {channel[1]}, "

            if filter_intents:
                return f"<Vis  ({str_channels[:-2]} -- [{filter_intents.attribute}{filter_intents.filter_op}{filter_intents.value}]) mark: {self._mark}, score: {self.score} >"
            else:
                return f"<Vis  ({str_channels[:-2]}) mark: {self._mark}, score: {self.score} >"
        else:
            # When Vis not compiled (e.g., when self._source not populated), print original intent
            return f"<Vis  ({str(self._intent)}) mark: {self._mark}, score: {self.score} >"

    @property
    def data(self):
        pass

    @property
    def code(self):
        pass

    @property
    def mark(self):
        pass

    @property
    def min_max(self):
        pass

    @property
    def intent(self):
        pass

    @intent.setter
    def intent(self, intent: List[Clause]) -> None:
        pass

    def set_intent(self, intent: List[Clause]) -> None:
        """
        Sets the intent of the Vis and refresh the source based on the new intent

        Parameters
        ----------
        intent : List[Clause]
                Query specifying the desired VisList
        """
        pass

    def _ipython_display_(self):
        pass

    def get_attr_by_attr_name(self, attr_name):
        pass

    def get_attr_by_channel(self, channel):
        pass

    def get_attr_by_data_model(self, dmodel, exclude_record=False):
        pass

    def get_attr_by_data_type(self, dtype):
        pass

    def remove_filter_from_spec(self, value):
        pass

    def remove_column_from_spec(self, attribute, remove_first: bool = False):
        """
        Removes an attribute from the Vis's clause

        Parameters
        ----------
        attribute : str
                attribute to be removed
        remove_first : bool, optional
                Boolean flag to determine whether to remove all instances of the attribute or only one (first) instance, by default False
        """
        pass

    def to_altair(self, standalone=False) -> str:
        """
        Generate minimal Altair code to visualize the Vis

        Parameters
        ----------
        standalone : bool, optional
                Flag to determine if outputted code uses user-defined variable names or can be run independently, by default False

        Returns
        -------
        str
                String version of the Altair code. Need to print out the string to apply formatting.
        """
        pass

    def to_matplotlib(self) -> str:
        """
        Generate minimal Matplotlib code to visualize the Vis

        Returns
        -------
        str
                String version of the Matplotlib code. Need to print out the string to apply formatting.
        """
        pass

    def _to_matplotlib_svg(self) -> str:
        """
        Private method to render Vis as SVG with Matplotlib

        Returns
        -------
        str
                String version of the SVG.
        """
        pass

    def to_vegalite(self, prettyOutput=True) -> Union[dict, str]:
        """
        Generate minimal Vega-Lite code to visualize the Vis

        Returns
        -------
        Union[dict,str]
                String or Dictionary of the VegaLite JSON specification
        """
        pass

    def to_code(self, language="vegalite", **kwargs):
        """
        Export Vis object to code specification

        Parameters
        ----------
        language : str, optional
            choice of target language to produce the visualization code in, by default "vegalite"

        Returns
        -------
        spec:
            visualization specification corresponding to the Vis object
        """
        pass

    def refresh_source(self, ldf):  # -> Vis:
        """
        Loading the source data into the Vis by instantiating the specification and
        populating the Vis based on the source data, effectively "materializing" the Vis.

        Parameters
        ----------
        ldf : LuxDataframe
                Input Dataframe to be attached to the Vis

        Returns
        -------
        Vis
                Complete Vis with fully-specified fields

        See Also
        --------
        lux.Vis.VisList.refresh_source

        Note
        ----
        Function derives a new _inferred_intent by instantiating the intent specification on the new data
        """
        pass

    def check_not_vislist_intent(self):

        pass
