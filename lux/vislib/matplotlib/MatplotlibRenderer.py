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

import lux
import pandas as pd
from lux.executor.PandasExecutor import PandasExecutor
from lux.vislib.matplotlib.BarChart import BarChart
from lux.vislib.matplotlib.ScatterChart import ScatterChart
from lux.vislib.matplotlib.LineChart import LineChart
from lux.vislib.matplotlib.Histogram import Histogram
from lux.vislib.matplotlib.Heatmap import Heatmap
from lux.vislib.altair.AltairRenderer import AltairRenderer
import matplotlib.pyplot as plt
from lux.utils.utils import matplotlib_setup

import base64
from io import BytesIO


class MatplotlibRenderer:
    """
    Renderer for Charts based on Matplotlib (https://matplotlib.org/)
    """

    def __init__(self, output_type="matplotlib"):
        self.output_type = output_type

    def __repr__(self):
        return f"MatplotlibRenderer"

    def create_vis(self, vis, standalone=True):
        """
        Input Vis object and return a visualization specification

        Parameters
        ----------
        vis: lux.vis.Vis
                Input Vis (with data)
        standalone: bool
                Flag to determine if outputted code uses user-defined variable names or can be run independently
        Returns
        -------
        chart : altair.Chart
                Output Altair Chart Object
        """
        pass
