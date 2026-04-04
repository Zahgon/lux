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

from lux.vislib.altair.AltairChart import AltairChart
import altair as alt
import math

alt.data_transformers.disable_max_rows()


class Histogram(AltairChart):
    """
    Histogram is a subclass of AltairChart that render as a histograms.
    All rendering properties for histograms are set here.

    See Also
    --------
    altair-viz.github.io
    """

    def __init__(self, vis):
        super().__init__(vis)

    def __repr__(self):
        return f"Histogram <{str(self.vis)}>"

    def initialize_chart(self):
        pass


def compute_bin_width(series):
    """
    Helper function that returns optimal bin size via Freedman Diaconis's Rule
    Source: https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule
    """
    pass
