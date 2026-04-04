import pandas
from lux.vis.VisList import VisList
from lux.vis.Vis import Vis
from lux.core.sqltable import LuxSQLTable
from lux.executor.Executor import Executor
from lux.utils import utils
from lux.utils.utils import check_import_lux_widget, check_if_id_like
import lux

import math


class SQLExecutor(Executor):
    """
    Given a Vis objects with complete specifications, fetch and process data using SQL operations.
    """

    def __init__(self):
        self.name = "SQLExecutor"
        self.selection = []
        self.tables = []
        self.filters = ""

    def __repr__(self):
        return f"<SQLExecutor>"

    @staticmethod
    def execute_preview(tbl: LuxSQLTable, preview_size=5):
        pass

    @staticmethod
    def execute_sampling(tbl: LuxSQLTable):
        pass

    @staticmethod
    def execute(view_collection: VisList, tbl: LuxSQLTable, approx: bool = False):
        """
        Given a VisList, fetch the data required to render the view
        1) Generate Necessary WHERE clauses
        2) Query necessary data, applying appropriate aggregation for the chart type
        3) populates vis' data with a DataFrame with relevant results
        """
        for view in view_collection:
            # choose execution method depending on vis mark type

            # when mark is empty, deal with lazy execution by filling the data with a small sample of the dataframe

            if view.mark == "":
                SQLExecutor.execute_sampling(tbl)
                view._vis_data = tbl._sampled
            if view.mark == "scatter":
                where_clause, filterVars = SQLExecutor.execute_filter(view)
                length_query = pandas.read_sql(lux.config.query_templates['length_query'].format(table_name = tbl.table_name, where_clause = where_clause),lux.config.SQLconnection,)
                view_data_length = list(length_query["length"])[0]
                if view_data_length >= lux.config._heatmap_start:
                    # NOTE: might want to have a check somewhere to not use categorical variables with greater than some number of categories as a Color variable----------------
                    has_color = True
                    SQLExecutor.execute_scatter(view, tbl)
                else:
                    view._mark = "heatmap"
                    SQLExecutor.execute_2D_binning(view, tbl)
            elif view.mark == "heatmap":
                SQLExecutor.execute_2D_binning(view, tbl)
            elif view.mark == "bar" or view.mark == "line":
                SQLExecutor.execute_aggregate(view, tbl)
            elif view.mark == "histogram":
                SQLExecutor.execute_binning(view, tbl)

    @staticmethod
    def execute_scatter(view: Vis, tbl: LuxSQLTable):
        """
        Given a scatterplot vis and a Lux Dataframe, fetch the data required to render the vis.
        1) Generate WHERE clause for the SQL query
        2) Check number of datapoints to be included in the query
        3) If the number of datapoints exceeds 10000, perform a random sample from the original data
        4) Query datapoints needed for the scatterplot visualization
        5) return a DataFrame with relevant results

        Parameters
        ----------
        vislist: list[lux.Vis]
            vis list that contains lux.Vis objects for visualization.
        tbl : lux.core.frame
            LuxSQLTable with specified intent.

        Returns
        -------
        None
        """
        pass

    @staticmethod
    def execute_aggregate(view: Vis, tbl: LuxSQLTable, isFiltered=True):
        """
        Aggregate data points on an axis for bar or line charts
        Parameters
        ----------
        vis: lux.Vis
            lux.Vis object that represents a visualization
        tbl : lux.core.frame
            LuxSQLTable with specified intent.
        isFiltered: boolean
            boolean that represents whether a vis has had a filter applied to its data
        Returns
        -------
        None
        """
        pass
            # view._vis_data.length = list(length_query["length"])[0]

    @staticmethod
    def execute_binning(view: Vis, tbl: LuxSQLTable):
        """
        Binning of data points for generating histograms
        Parameters
        ----------
        vis: lux.Vis
            lux.Vis object that represents a visualization
        tbl : lux.core.frame
            LuxSQLTable with specified intent.
        Returns
        -------
        None
        """
        pass
            # view._vis_data.length = list(length_query["length"])[0]

    @staticmethod
    def execute_2D_binning(view: Vis, tbl: LuxSQLTable):
        pass

    @staticmethod
    def execute_filter(view: Vis):
        """
        Helper function to convert a Vis' filter specification to a SQL where clause.
        Takes in a Vis object and returns an appropriate SQL WHERE clause based on the filters specified in the vis' _inferred_intent.

        Parameters
        ----------
        vis: lux.Vis
            lux.Vis object that represents a visualization

        Returns
        -------
        where_clause: string
            String representation of a SQL WHERE clause
        filter_vars: list of strings
            list of variables that have been used as filters
        """
        pass

    def create_where_clause(filter_specs, view=""):
        pass

    def get_filtered_size(filter_specs, tbl):
        pass

    #######################################################
    ########## Metadata, type, model schema ###############
    #######################################################

    def compute_dataset_metadata(self, tbl: LuxSQLTable):
        """
        Function which computes the metadata required for the Lux recommendation system.
        Populates the metadata parameters of the specified Lux DataFrame.

        Parameters
        ----------
        tbl: lux.LuxSQLTable
            lux.LuxSQLTable object whose metadata will be calculated

        Returns
        -------
        None
        """
        pass

    def get_SQL_attributes(self, tbl: LuxSQLTable):
        """
        Retrieves the names of variables within a specified Lux DataFrame's Postgres SQL table.
        Uses these variables to populate the Lux DataFrame's columns list.

        Parameters
        ----------
        tbl: lux.LuxSQLTable
            lux.LuxSQLTable object whose columns will be populated

        Returns
        -------
        None
        """
        pass

    def compute_stats(self, tbl: LuxSQLTable):
        """
        Function which computes the min and max values for each variable within the specified Lux DataFrame's SQL table.
        Populates the metadata parameters of the specified Lux DataFrame.

        Parameters
        ----------
        tbl: lux.LuxSQLTable
            lux.LuxSQLTable object whose metadata will be calculated

        Returns
        -------
        None
        """
        pass

    def get_cardinality(self, tbl: LuxSQLTable):
        """
        Function which computes the cardinality for each variable within the specified Lux DataFrame's SQL table.
        Populates the metadata parameters of the specified Lux DataFrame.

        Parameters
        ----------
        tbl: lux.LuxSQLTable
            lux.LuxSQLTable object whose metadata will be calculated

        Returns
        -------
        None
        """
        pass

    def get_unique_values(self, tbl: LuxSQLTable):
        """
        Function which collects the unique values for each variable within the specified Lux DataFrame's SQL table.
        Populates the metadata parameters of the specified Lux DataFrame.

        Parameters
        ----------
        tbl: lux.LuxSQLTable
            lux.LuxSQLTable object whose metadata will be calculated

        Returns
        -------
        None
        """
        pass

    def compute_data_type(self, tbl: LuxSQLTable):
        """
        Function which the equivalent Pandas data type of each variable within the specified Lux DataFrame's SQL table.
        Populates the metadata parameters of the specified Lux DataFrame.

        Parameters
        ----------
        tbl: lux.LuxSQLTable
            lux.LuxSQLTable object whose metadata will be calculated

        Returns
        -------
        None
        """
        pass
