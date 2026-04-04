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

import re

import lux
import numpy as np
import pandas as pd
from lux.utils.date_utils import compute_date_granularity

import altair as alt


class AltairChart:
    """
    AltairChart is a representation of a chart.
    Common utilities for charts that is independent of chart types should go here.

    See Also
    --------
    altair-viz.github.io

    """

    def __init__(self, vis):
        self.vis = vis
        self.data = vis.data
        self.tooltip = True
        # ----- START self.code modification -----
        self.code = ""
        self.width = 160
        self.height = 150
        self.chart = self.initialize_chart()
        # self.add_tooltip()
        self.encode_color()
        self.add_title()
        self.apply_default_config()

        # ----- END self.code modification -----

    def __repr__(self):
        return f"AltairChart <{str(self.vis)}>"

    def add_tooltip(self):
        pass

    def apply_default_config(self):
        pass

    def encode_color(self):
        pass

    def add_title(self):
        pass

    def initialize_chart(self):
        pass

    @classmethod
    def sanitize_dataframe(self, df):
        pass
