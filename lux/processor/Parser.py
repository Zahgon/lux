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

from lux.vis.Clause import Clause
from lux.core.frame import LuxDataFrame
from typing import List, Union


class Parser:
    """
    The parser takes in the user's input specifications (with string `description` fields),
    then generates the Lux internal specification through lux.Clause.
    """

    @staticmethod
    def parse(intent: List[Union[Clause, str]]) -> List[Clause]:
        """
        Given the string description from a list of input Clauses (intent),
        assign the appropriate clause.attribute, clause.filter_op, and clause.value.

        Parameters
        ----------
        intent : List[Clause]
                Underspecified list of lux.Clause objects.

        Returns
        -------
        List[Clause]
                Parsed list of lux.Clause objects.
        """
        pass
