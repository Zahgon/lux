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

from lux.vislib.matplotlib.MatplotlibChart import MatplotlibChart
from lux.utils.utils import get_agg_title
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from lux.utils.utils import matplotlib_setup
from matplotlib.cm import ScalarMappable
from lux.utils.date_utils import compute_date_granularity
from matplotlib.ticker import MaxNLocator
import lux


class BarChart(MatplotlibChart):
    """
    BarChart is a subclass of MatplotlibChart that render as a bar charts.
    All rendering properties for bar charts are set here.

    See Also
    --------
    matplotlib.org
    """

    def __init__(self, dobj, fig, ax):
        super().__init__(dobj, fig, ax)

    def __repr__(self):
        return f"Bar Chart <{str(self.vis)}>"

    def initialize_chart(self):
        pass
