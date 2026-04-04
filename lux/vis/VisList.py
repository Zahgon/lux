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


from lux.vislib.altair.AltairRenderer import AltairRenderer
from lux.utils.utils import check_import_lux_widget
from typing import List, Union, Callable, Dict
from lux.vis.Vis import Vis
from lux.vis.Clause import Clause
import warnings
import lux


class VisList:
    """VisList is a list of Vis objects."""

    def __init__(self, input_lst: Union[List[Vis], List[Clause]], source=None):
        # Overloaded Constructor
        self._source = source
        self._input_lst = input_lst
        if len(input_lst) > 0:
            if self._is_vis_input():
                self._collection = input_lst
                self._intent = []
            else:
                self._intent = input_lst
                self._collection = []
        else:
            self._collection = []
            self._intent = []
        self._widget = None
        self.refresh_source(self._source)
        warnings.formatwarning = lux.warning_format

    @property
    def intent(self):
        pass

    @intent.setter
    def intent(self, intent: List[Clause]) -> None:
        pass

    def set_intent(self, intent: List[Clause]) -> None:
        """
        Sets the intent of the VisList and refresh the source based on the new clause
        Parameters
        ----------
        intent : List[Clause]
                Query specifying the desired VisList
        """
        pass

    @property
    def exported(self):
        """
        Get selected visualizations as exported Vis List

        Notes
        -----
        Convert the _selectedVisIdxs dictionary into a programmable VisList
        Example _selectedVisIdxs :
                {'Vis List': [0, 2]}

        Returns
        -------
        VisList
                return a VisList of selected visualizations. -> VisList(v1, v2...)
        """
        pass

    def remove_duplicates(self) -> None:
        """
        Removes duplicate visualizations in VisList
        """
        pass

    def remove_index(self, index):
        pass

    def _is_vis_input(self):
        pass

    def __getitem__(self, key):
        return self._collection[key]

    def __setitem__(self, key, value):
        self._collection[key] = value

    def __len__(self):
        return len(self._collection)

    def __repr__(self):
        if len(self._collection) == 0:
            return str(self._input_lst)
        x_channel = ""
        y_channel = ""
        largest_mark = 0
        largest_filter = 0
        # finds longest x attribute among all visualizations
        for vis in self._collection:
            filter_intents = None
            for clause in vis._inferred_intent:
                attr = str(clause.attribute)
                if clause.value != "":
                    filter_intents = clause

                if clause.aggregation != "" and clause.aggregation is not None:
                    attribute = clause._aggregation_name.upper() + f"({attr})"
                elif clause.bin_size > 0:
                    attribute = f"BIN({attr})"
                else:
                    attribute = attr
                attribute = str(attribute)
                if clause.channel == "x" and len(x_channel) < len(attribute):
                    x_channel = attribute
                if clause.channel == "y" and len(y_channel) < len(attribute):
                    y_channel = attribute
            if len(vis.mark) > largest_mark:
                largest_mark = len(vis.mark)
            if (
                filter_intents
                and len(str(filter_intents.value)) + len(str(filter_intents.attribute)) > largest_filter
            ):
                largest_filter = len(str(filter_intents.value)) + len(str(filter_intents.attribute))
        vis_repr = []
        largest_x_length = len(x_channel)
        largest_y_length = len(y_channel)
        # pads the shorter visualizations with spaces before the y attribute
        for vis in self._collection:
            filter_intents = None
            x_channel = ""
            y_channel = ""
            additional_channels = []
            for clause in vis._inferred_intent:
                attr = str(clause.attribute)
                if clause.value != "":
                    filter_intents = clause

                if clause.aggregation != "" and clause.aggregation is not None and vis.mark != "scatter":
                    attribute = clause._aggregation_name.upper() + f"({attr})"
                elif clause.bin_size > 0:
                    attribute = f"BIN({attr})"
                else:
                    attribute = attr
                if clause.channel == "x":
                    x_channel = attribute.ljust(largest_x_length)
                elif clause.channel == "y":
                    y_channel = attribute
                elif clause.channel != "":
                    additional_channels.append([clause.channel, attribute])
            if filter_intents:
                y_channel = y_channel.ljust(largest_y_length)
            elif largest_filter != 0:
                y_channel = y_channel.ljust(largest_y_length + largest_filter + 9)
            else:
                y_channel = y_channel.ljust(largest_y_length + largest_filter)
            if x_channel != "":
                x_channel = "x: " + x_channel + ", "
            if y_channel != "":
                y_channel = "y: " + y_channel
            aligned_mark = vis.mark.ljust(largest_mark)
            str_additional_channels = ""
            for channel in additional_channels:
                str_additional_channels += ", " + channel[0] + ": " + channel[1]
            if filter_intents:
                aligned_filter = (
                    " -- ["
                    + str(filter_intents.attribute)
                    + filter_intents.filter_op
                    + str(filter_intents.value)
                    + "]"
                )
                aligned_filter = aligned_filter.ljust(largest_filter + 8)
                vis_repr.append(
                    f" <Vis  ({x_channel}{y_channel}{str_additional_channels} {aligned_filter}) mark: {aligned_mark}, score: {vis.score:.2f} >"
                )
            else:
                vis_repr.append(
                    f" <Vis  ({x_channel}{y_channel}{str_additional_channels}) mark: {aligned_mark}, score: {vis.score:.2f} >"
                )
        return "[" + ",\n".join(vis_repr)[1:] + "]"

    def map(self, function):
        # generalized way of applying a function to each element
        pass

    def get(self, field_name):
        # Get the value of the field for all objects in the collection
        pass

    def set(self, field_name, field_val):
        pass

    def sort(self, remove_invalid=True, descending=True):
        # remove the items that have invalid (-1) score
        pass

    def showK(self):
        pass

    def normalize_score(self, invert_order=False):
        pass

    def _ipython_display_(self):
        pass

    def refresh_source(self, ldf):
        """
        Loading the source into the visualizations in the VisList, then populating each visualization
        based on the new source data, effectively "materializing" the visualization collection.
        Parameters
        ----------
        ldf : LuxDataframe
                Input Dataframe to be attached to the VisList
        Returns
        -------
        VisList
                Complete VisList with fully-specified fields

        See Also
        --------
        lux.vis.Vis.refresh_source
        Note
        ----
        Function derives a new _inferred_intent by instantiating the intent specification on the new data
        """
        pass
