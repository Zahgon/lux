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

# from ..luxDataFrame.LuxDataframe import LuxDataFrame
from lux.core.frame import LuxDataFrame
from lux.vis.Clause import Clause
from typing import List
from lux.utils.date_utils import is_datetime_series, is_datetime_string
import warnings
import pandas as pd
import lux
import lux.utils.utils


class Validator:
    """
    Contains methods for validating lux.Clause objects in the intent.
    """

    def __init__(self):
        self.name = "Validator"
        warnings.formatwarning = lux.warning_format

    def __repr__(self):
        return f"<Validator>"

    @staticmethod
    def validate_intent(intent: List[Clause], ldf: LuxDataFrame, suppress_warning=False):
        """
        Validates input specifications from the user to find inconsistencies and errors.

        Parameters
        ----------
        ldf : lux.core.frame
                LuxDataFrame with underspecified intent.

        Returns
        -------
        Boolean
                True if the intent passed in is valid, False otherwise.

        Raises
        ------
        ValueError
                Ensures input intent are consistent with DataFrame content.

        """
        pass
