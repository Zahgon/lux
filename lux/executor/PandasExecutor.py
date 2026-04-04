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
from lux.vis.VisList import VisList
from lux.vis.Vis import Vis
from lux.core.frame import LuxDataFrame
from lux.executor.Executor import Executor
from lux.utils import utils
from lux.utils.date_utils import is_datetime_series, is_timedelta64_series, timedelta64_to_float_seconds
from lux.utils.utils import check_import_lux_widget, check_if_id_like, is_numeric_nan_column
import warnings
import lux
from lux.utils.tracing_utils import LuxTracer


class PandasExecutor(Executor):
    """
    Given a Vis objects with complete specifications, fetch and process data using Pandas dataframe operations.
    """

    def __init__(self):
        self.name = "PandasExecutor"
        warnings.formatwarning = lux.warning_format

    def __repr__(self):
        return f"<PandasExecutor>"

    @staticmethod
    def execute_sampling(ldf: LuxDataFrame):
        """
        Compute and cache a sample for the overall dataframe

        - When # of rows exceeds lux.config.sampling_start, take 75% df as sample
        - When # of rows exceeds lux.config.sampling_cap, cap the df at {lux.config.sampling_cap} rows

        lux.config.sampling_start = 100k rows
        lux.config.sampling_cap = 1M rows

        Parameters
        ----------
        ldf : LuxDataFrame
        """
        pass

    @staticmethod
    def execute_approx_sample(ldf: LuxDataFrame):
        """
        Compute and cache an approximate sample of the overall dataframe
        for the purpose of early pruning of the visualization search space

        Parameters
        ----------
        ldf : LuxDataFrame
        """
        pass

    @staticmethod
    def execute(vislist: VisList, ldf: LuxDataFrame, approx=False):
        """
        Given a VisList, fetch the data required to render the vis.
        1) Apply filters
        2) Retrieve relevant attribute
        3) Perform vis-related processing (aggregation, binning)
        4) return a DataFrame with relevant results

        Parameters
        ----------
        vislist: list[lux.Vis]
            vis list that contains lux.Vis objects for visualization.
        ldf : lux.core.frame
            LuxDataFrame with specified intent.

        Returns
        -------
        None
        """

        PandasExecutor.execute_sampling(ldf)
        for vis in vislist:
            # The vis data starts off being original or sampled dataframe
            vis._source = ldf
            vis._vis_data = ldf._sampled
            # Approximating vis for early pruning
            if approx:
                vis._original_df = vis._vis_data
                PandasExecutor.execute_approx_sample(ldf)
                vis._vis_data = ldf._approx_sample
                vis.approx = True
            filter_executed = PandasExecutor.execute_filter(vis)
            # Select relevant data based on attribute information
            attributes = set([])
            for clause in vis._inferred_intent:
                if clause.attribute != "Record":
                    attributes.add(clause.attribute)
            # TODO: Add some type of cap size on Nrows ?
            vis._vis_data = vis._vis_data[list(attributes)]

            if vis.mark == "bar" or vis.mark == "line" or vis.mark == "geographical":
                PandasExecutor.execute_aggregate(vis, isFiltered=filter_executed)
            elif vis.mark == "histogram":
                PandasExecutor.execute_binning(ldf, vis)
            elif vis.mark == "heatmap":
                # Early pruning based on interestingness of scatterplots
                if approx:
                    vis._mark = "scatter"
                else:
                    vis._mark = "heatmap"
                    PandasExecutor.execute_2D_binning(vis)
            # Ensure that intent is not propogated to the vis data (bypass intent setter, since trigger vis.data metadata recompute)
            vis.data._intent = []

    @staticmethod
    def execute_aggregate(vis: Vis, isFiltered=True):
        """
        Aggregate data points on an axis for bar or line charts

        Parameters
        ----------
        vis: lux.Vis
            lux.Vis object that represents a visualization
        ldf : lux.core.frame
            LuxDataFrame with specified intent.

        Returns
        -------
        None
        """
        pass

    @staticmethod
    def execute_binning(ldf: LuxDataFrame, vis: Vis):
        """
        Binning of data points for generating histograms

        Parameters
        ----------
        vis: lux.Vis
            lux.Vis object that represents a visualization
        ldf : lux.core.frame
            LuxDataFrame with specified intent.

        Returns
        -------
        None
        """
        pass

    @staticmethod
    def execute_filter(vis: Vis) -> bool:
        """
        Apply a Vis's filter to vis.data

        Parameters
        ----------
        vis : Vis

        Returns
        -------
        bool
            Boolean flag indicating if any filter was applied
        """
        pass

    @staticmethod
    def apply_filter(df: pd.DataFrame, attribute: str, op: str, val: object) -> pd.DataFrame:
        """
        Helper function for applying filter to a dataframe

        Parameters
        ----------
        df : pandas.DataFrame
            Dataframe to filter on
        attribute : str
            Filter attribute
        op : str
            Filter operation, '=', '<', '>', '<=', '>=', '!='
        val : object
            Filter value

        Returns
        -------
        df: pandas.DataFrame
            Dataframe resulting from the filter operation
        """
        pass

    @staticmethod
    def execute_2D_binning(vis: Vis) -> None:
        """
        Apply 2D binning (heatmap) to vis.data

        Parameters
        ----------
        vis : Vis
        """
        pass

    #######################################################
    ############ Metadata: data type, model #############
    #######################################################
    def compute_dataset_metadata(self, ldf: LuxDataFrame):
        pass

    def compute_data_type(self, ldf: LuxDataFrame):
        pass

    @staticmethod
    def _is_datetime_string(series):
        pass

    @staticmethod
    def _is_geographical_attribute(series):
        # run detection algorithm
        pass

    @staticmethod
    def _is_datetime_number(series):
        pass

    def compute_stats(self, ldf: LuxDataFrame):
        # precompute statistics
        pass
