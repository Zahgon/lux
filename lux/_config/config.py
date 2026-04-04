"""
This config file was largely borrowed from Pandas config.py set_action functionality.
For more resources, see https://github.com/pandas-dev/pandas/blob/master/pandas/_config
"""
from collections import namedtuple
from typing import Any, Callable, Dict, Iterable, List, Optional, Union
import lux
import warnings
from lux.utils.tracing_utils import LuxTracer
import os
from lux._config.template import postgres_template, mysql_template

RegisteredOption = namedtuple("RegisteredOption", "name action display_condition args")


class Config:
    """
    Class for Lux configurations applied globally across entire session
    """

    def __init__(self):
        self._default_display = "pandas"
        self.plotting_style = None
        self.SQLconnection = ""
        self.executor = None
        # holds registered option metadata
        self.actions: Dict[str, RegisteredOption] = {}
        # flags whether or not an action has been registered or removed and should be re-rendered by frame.py
        self.update_actions: Dict[str, bool] = {}
        self.update_actions["flag"] = False
        self._plotting_backend = "vegalite"
        self._plotting_scale = 1
        self._topk = 15
        self._number_of_bars = 10  # max no of bars displayed (rest shown as "+ k more")
        self._label_len = 25  # max length of x and y axis labels
        self._sort = "descending"
        self._pandas_fallback = True
        self._interestingness_fallback = True
        self.heatmap_bin_size = 40
        self.tracer_relevant_lines = []
        self.tracer = LuxTracer()
        self.query_templates = {}
        self.handle_quotes = True
        #####################################
        #### Optimization Configurations ####
        #####################################
        self._sampling_start = 100000
        self._sampling_cap = 1000000
        self._sampling_flag = True
        self._heatmap_flag = True
        self._heatmap_start = 5000
        self.lazy_maintain = True
        self.early_pruning = True
        self.early_pruning_sample_cap = 30000
        # Apply sampling only if the dataset is 150% larger than the sample cap
        self.early_pruning_sample_start = self.early_pruning_sample_cap * 1.5
        self.streaming = False
        self.render_widget = True

    @property
    def number_of_bars(self):
        pass

    @number_of_bars.setter
    def number_of_bars(self, k: int) -> None:
        """
        Parameters
        ----------
        k : int
            Number of bars in output bar charts; rest are not displayed
        """
        pass

    @property
    def label_len(self):
        pass

    @label_len.setter
    def label_len(self, l: int) -> None:
        """
        Parameters
        ----------
        l : int
            Maximum length of string axis labels
        """
        pass

    @property
    def topk(self):
        pass

    @topk.setter
    def topk(self, k: Union[int, bool]):
        """
        Setting parameter to display top k visualizations in each action

        Parameters
        ----------
        k : Union[int,bool]
            False: if display all visualizations (no top-k)
            k: number of visualizations to display
        """
        pass

    @property
    def sort(self):
        pass

    @sort.setter
    def sort(self, flag: Union[str]):
        """
        Setting parameter to determine sort order of each action

        Parameters
        ----------
        flag : Union[str]
            "none", "ascending","descending"
            No sorting, sort by ascending order, sort by descending order
        """
        pass

    @property
    def pandas_fallback(self):
        pass

    @pandas_fallback.setter
    def pandas_fallback(self, fallback: bool) -> None:
        """
        Parameters
        ----------
        fallback : bool
            If an error occurs, whether or not to raise an exception or fallback to default Pandas.
        """
        pass

    @property
    def interestingness_fallback(self):
        pass

    @interestingness_fallback.setter
    def interestingness_fallback(self, fallback: bool) -> None:
        """
        Parameters
        ----------
        fallback : bool
            If an error occurs while calculating interestingness, whether or not
            to raise an exception or fallback to default Pandas.
        """
        pass

    @property
    def sampling_cap(self):
        """
        Parameters
        ----------
        sample_number : int
            Cap on the number of rows to sample. Must be larger than _sampling_start
        """
        pass

    @sampling_cap.setter
    def sampling_cap(self, sample_number: int) -> None:
        """
        Parameters
        ----------
        sample_number : int
            Cap on the number of rows to sample. Must be larger than _sampling_start
        """
        pass

    @property
    def sampling_start(self):
        """
        Parameters
        ----------
        sample_number : int
            Number of rows required to begin sampling. Must be smaller or equal to _sampling_cap

        """
        pass

    @sampling_start.setter
    def sampling_start(self, sample_number: int) -> None:
        """
        Parameters
        ----------
        sample_number : int
            Number of rows required to begin sampling. Must be smaller or equal to _sampling_cap

        """
        pass

    @property
    def sampling(self):
        """
        Parameters
        ----------
        sample_flag : bool
            Whether or not sampling will occur.
        """
        pass

    @sampling.setter
    def sampling(self, sample_flag: bool) -> None:
        """
        Parameters
        ----------
        sample_flag : bool
            Whether or not sampling will occur.
        """
        pass

    @property
    def heatmap(self):
        """
        Parameters
        ----------
        heatmap_flag : bool
            Whether or not a heatmap will be used instead of a scatter plot.
        """
        pass

    @heatmap.setter
    def heatmap(self, heatmap_flag: bool) -> None:
        """
        Parameters
        ----------
        heatmap_flag : bool
            Whether or not a heatmap will be used instead of a scatter plot.
        """
        pass

    @property
    def default_display(self):
        """
        Set the widget display to show Pandas by default or Lux by default
        Parameters
        ----------
        type : str
            Default display type, can take either the string `lux` or `pandas` (regardless of capitalization)
        """
        pass

    @default_display.setter
    def default_display(self, type: str) -> None:
        """
        Set the widget display to show Pandas by default or Lux by default
        Parameters
        ----------
        type : str
            Default display type, can take either the string `lux` or `pandas` (regardless of capitalization)
        """
        pass

    @property
    def plotting_backend(self):
        pass

    @plotting_backend.setter
    def plotting_backend(self, type: str) -> None:
        """
        Set the widget display to show Vegalite by default or Matplotlib by default
        Parameters
        ----------
        type : str
                Default display type, can take either the string `vegalite` or `matplotlib` (regardless of capitalization)
        """
        pass

    @property
    def plotting_scale(self):
        pass

    @plotting_scale.setter
    def plotting_scale(self, scale: float) -> None:
        """
        Set the scale factor for charts displayed in Lux.
        ----------
        type : float (default = 1.0)
        """
        pass

    def _get_action(self, pat: str, silent: bool = False):
        pass

    def register_action(
        self,
        name: str = "",
        action: Callable[[Any], Any] = None,
        display_condition: Optional[Callable[[Any], Any]] = None,
        *args,
    ) -> None:
        """
        Registers the provided action globally in lux

        Parameters
        ----------
        name : str
                the name of the action
        action : Callable[[Any], Any]
                the function used to generate the recommendations
        display_condition : Callable[[Any], Any]
                the function to check whether or not the function should be applied
        args: Any
                any additional arguments the function may require
        """
        pass

    def remove_action(self, name: str = "") -> None:
        """
        Removes the provided action globally in lux

        Parameters
        ----------
        name : str
                the name of the action to remove
        """
        pass

    def set_SQL_connection(self, connection):
        """
        Sets SQL connection to a database

        Parameters:
            connection : SQLAlchemy connectable, str, or sqlite3 connection
                For more information, `see here <https://docs.sqlalchemy.org/en/13/core/connections.html>`__
        """
        pass

    def read_query_template(self, query_template):
        pass

    def set_executor_type(self, exe):
        pass


def warning_format(message, category, filename, lineno, file=None, line=None):
    pass
