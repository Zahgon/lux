import pandas as pd


class LuxGroupByMixin:
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
    ]

    def aggregate(self, *args, **kwargs):
        pass

    def _agg_general(self, *args, **kwargs):
        pass

    def _cython_agg_general(self, *args, **kwargs):
        pass

    def get_group(self, *args, **kwargs):
        pass

    def filter(self, *args, **kwargs):
        pass

    def apply(self, *args, **kwargs):
        pass

    def size(self, *args, **kwargs):
        pass

    def __getitem__(self, *args, **kwargs):
        ret_val = super().__getitem__(*args, **kwargs)
        for attr in self._metadata:
            ret_val.__dict__[attr] = getattr(self, attr, None)
        return ret_val

    agg = aggregate


class LuxDataFrameGroupBy(LuxGroupByMixin, pd.core.groupby.DataFrameGroupBy):
    pass


class LuxSeriesGroupBy(LuxGroupByMixin, pd.core.groupby.SeriesGroupBy):
    pass
