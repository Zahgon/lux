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

import pandas as pd
from lux.core.series import LuxSeries
from lux.vis.Clause import Clause
from lux.vis.Vis import Vis
from lux.vis.VisList import VisList
from lux.history.history import History
from lux.utils.date_utils import is_datetime_series
from lux.utils.message import Message
from lux.utils.utils import check_import_lux_widget
from typing import Dict, Union, List, Callable

# from lux.executor.Executor import *
import warnings
import traceback
import lux


class JoinedSQLTable(lux.LuxSQLTable):
    """
    A subclass of Lux.LuxDataFrame that houses other variables and functions for generating visual recommendations. Does not support normal pandas functionality.
    """

    # MUST register here for new properties!!
    _metadata = [
        "_intent",
        "_inferred_intent",
        "_data_type",
        "unique_values",
        "cardinality",
        "_rec_info",
        "_min_max",
        "_current_vis",
        "_widget",
        "_recommendation",
        "_prev",
        "_history",
        "_saved_export",
        "_sampled",
        "_toggle_pandas_display",
        "_message",
        "_pandas_only",
        "pre_aggregated",
        "_type_override",
        "joins",
        "using_view",
    ]

    def __init__(self, *args, joins=[], **kw):
        super(JoinedSQLTable, self).__init__(*args, **kw)
        from lux.executor.SQLExecutor import SQLExecutor

        lux.config.executor = SQLExecutor()
        # self._metadata.joins = []
        tables = self.extract_tables(joins)
        if len(tables) > 4:
            warnings.warn(
                f"\nPlease provide a maximum of 4 (Four) unique tables to ensure optimal performance.",
                stacklevel=2,
            )
        view_name = self.create_view(tables, joins)
        self._length = 0
        if view_name != "":
            self.set_SQL_table(view_name)
            # self._metadata.using_view = True
        warnings.formatwarning = lux.warning_format

    def len(self):
        pass

    def extract_tables(self, joins):
        pass

    def create_view(self, tables, joins):
        pass

    def _ipython_display_(self):
        pass

    # Overridden Pandas Functions
    def head(self, n: int = 5):
        pass

    def tail(self, n: int = 5):
        pass

    def info(self, *args, **kwargs):
        pass

    def describe(self, *args, **kwargs):
        pass

    def groupby(self, *args, **kwargs):
        pass
