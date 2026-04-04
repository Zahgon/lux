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

from lux.vis import Clause
from typing import List, Dict, Union
from lux.vis.Vis import Vis
from lux.processor.Validator import Validator
from lux.core.frame import LuxDataFrame
from lux.vis.VisList import VisList
from lux.utils import date_utils
from lux.utils import utils
import pandas as pd
import numpy as np
import warnings
import lux


class Compiler:
    """
    Given a intent with underspecified inputs, compile the intent into fully specified visualizations for visualization.
    """

    def __init__(self):
        self.name = "Compiler"
        warnings.formatwarning = lux.warning_format

    def __repr__(self):
        return f"<Compiler>"

    @staticmethod
    def compile_vis(ldf: LuxDataFrame, vis: Vis) -> Vis:
        """
        Root method for compiling visualizations

        Parameters
        ----------
        ldf : LuxDataFrame
        vis : Vis

        Returns
        -------
        Vis
            Compiled Vis object
        """
        pass

    @staticmethod
    def compile_intent(ldf: LuxDataFrame, _inferred_intent: List[Clause]) -> VisList:
        """
        Compiles input specifications in the intent of the ldf into a collection of lux.vis objects for visualization.
        1) Enumerate a collection of visualizations interested by the user to generate a vis list
        2) Expand underspecified specifications(lux.Clause) for each of the generated visualizations.
        3) Determine encoding properties for each vis

        Parameters
        ----------
        ldf : lux.core.frame
                LuxDataFrame with underspecified intent.
        vis_collection : list[lux.vis.Vis]
                empty list that will be populated with specified lux.Vis objects.

        Returns
        -------
        vis_collection: list[lux.Vis]
                vis list with compiled lux.Vis objects.
        """
        pass

    @staticmethod
    def enumerate_collection(_inferred_intent: List[Clause], ldf: LuxDataFrame) -> VisList:
        """
        Given specifications that have been expanded thorught populateOptions,
        recursively iterate over the resulting list combinations to generate a vis list.

        Parameters
        ----------
        ldf : lux.core.frame
                LuxDataFrame with underspecified intent.

        Returns
        -------
        VisList: list[lux.Vis]
                vis list with compiled lux.Vis objects.
        """
        pass

    @staticmethod
    def populate_data_type_model(ldf, vlist):
        """
        Given a underspecified Clause, populate the data_type and data_model information accordingly

        Parameters
        ----------
        ldf : lux.core.frame
                LuxDataFrame with underspecified intent

        vis_collection : list[lux.vis.Vis]
                List of lux.Vis objects that will have their underspecified Clause details filled out.
        """
        pass

    @staticmethod
    def remove_all_invalid(vis_collection: VisList) -> VisList:
        """
        Given an expanded vis list, remove all visualizations that are invalid.
        Currently, the invalid visualizations are ones that do not contain:
        - two of the same attribute,
        - more than two temporal attributes,
        - no overlapping attributes (same filter attribute and visualized attribute),
        - more than 1 temporal attribute with 2 or more measures
        Parameters
        ----------
        vis_collection : list[lux.vis.Vis]
                empty list that will be populated with specified lux.Vis objects.
        Returns
        -------
        lux.vis.VisList
                vis list with compiled lux.Vis objects.
        """
        pass

    @staticmethod
    def determine_encoding(ldf: LuxDataFrame, vis: Vis):
        """
        Populates Vis with the appropriate mark type and channel information based on ShowMe logic
        Currently support up to 3 dimensions or measures

        Parameters
        ----------
        ldf : lux.core.frame
                LuxDataFrame with underspecified intent
        vis : lux.vis.Vis

        Returns
        -------
        None

        Notes
        -----
        Implementing automatic encoding from Tableau's VizQL
        Mackinlay, J. D., Hanrahan, P., & Stolte, C. (2007).
        Show Me: Automatic presentation for visual analysis.
        IEEE Transactions on Visualization and Computer Graphics, 13(6), 1137–1144.
        https://doi.org/10.1109/TVCG.2007.70594
        """
        pass

    @staticmethod
    def enforce_specified_channel(vis: Vis, auto_channel: Dict[str, str]):
        """
        Enforces that the channels specified in the Vis by users overrides the showMe autoChannels.

        Parameters
        ----------
        vis : lux.vis.Vis
                Input Vis without channel specification.
        auto_channel : Dict[str,str]
                Key-value pair in the form [channel: attributeName] specifying the showMe recommended channel location.

        Returns
        -------
        vis : lux.vis.Vis
                Vis with channel specification combining both original and auto_channel specification.

        Raises
        ------
        ValueError
                Ensures no more than one attribute is placed in the same channel.
        """
        pass

    @staticmethod
    # def populate_wildcard_options(ldf: LuxDataFrame) -> dict:
    def populate_wildcard_options(_inferred_intent: List[Clause], ldf: LuxDataFrame) -> dict:
        """
        Given wildcards and constraints in the LuxDataFrame's intent,
        return the list of available values that satisfies the data_type or data_model constraints.

        Parameters
        ----------
        ldf : LuxDataFrame
                LuxDataFrame with row or attributes populated with available wildcard options.

        Returns
        -------
        intent: Dict[str,list]
                a dictionary that holds the attributes and filters generated from wildcards and constraints.
        """
        pass
