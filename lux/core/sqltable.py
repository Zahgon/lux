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


class LuxSQLTable(lux.LuxDataFrame):
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
        "_length",
        "_setup_done",
    ]

    def __init__(self, *args, table_name="", **kw):
        super(LuxSQLTable, self).__init__(*args, **kw)

        if lux.config.executor.name != "GeneralDatabaseExecutor":
            from lux.executor.SQLExecutor import SQLExecutor

            lux.config.executor = SQLExecutor()

        self._length = 0
        self._setup_done = False
        if table_name != "":
            self.set_SQL_table(table_name)
        warnings.formatwarning = lux.warning_format

    def __len__(self):
        if self._setup_done:
            return self._length
        else:
            return super(LuxSQLTable, self).__len__()

    def set_SQL_table(self, t_name):
        # function that ties the Lux Dataframe to a SQL database table
        pass

    def maintain_metadata(self):
        # Check that metadata has not yet been computed
        pass

    def expire_metadata(self):
        """
        Expire all saved metadata to trigger a recomputation the next time the data is required.
        """
        # self._metadata_fresh = False
        # self._data_type = None
        # self.unique_values = None
        # self.cardinality = None
        # self._min_max = None
        # self.pre_aggregated = None

    def _ipython_display_(self):
        pass
