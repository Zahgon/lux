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
import pandas as pd
from iso3166 import countries

alt.data_transformers.disable_max_rows()


class Choropleth(AltairChart):
    """
    Choropleth is a subclass of AltairChart that renders choropleth maps.
    All rendering properties for proportional symbol maps are set here.

    See Also
    --------
    altair-viz.github.io
    """

    us_url = "https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/us-10m.json"
    world_url = "https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/world-110m.json"

    def __init__(self, dobj):
        super().__init__(dobj)

    def __repr__(self):
        return f"Choropleth Map <{str(self.vis)}>"

    def initialize_chart(self):
        # Override default width and height
        pass

    def get_background(self, feature):
        """Returns background projection based on geographic feature."""
        pass

    def get_geomap(self, feature):
        """Returns topological encoding, topological style,
        and translation function based on geographic feature"""
        pass

    def get_us_fips_code(self, attribute):
        """Returns FIPS code given a US state"""
        pass

    def get_country_iso_code(self, attribute):
        """Returns country ISO code given a country"""
        pass

    def get_geographical_name(self, feature):
        """Returns geographical location label based on secondary feature."""
        pass

    def encode_color(self):
        # Setting tooltip as non-null
        pass
