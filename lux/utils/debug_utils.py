import json
from pathlib import Path
import re
import subprocess
import typing as tp

import re
import subprocess
from typing import Optional


def show_versions(return_string: bool = False) -> Optional[str]:
    """
    Prints the versions of the principal packages used by Lux for debugging purposes.
    Parameters
    ----------
    return_string: Whether to return the versions as a string or print them.
    Returns
    -------
    If return_string is True, returns a string with the versions else the versions
    are printed and None is returned.
    """
    pass


def debug_info(return_string: bool = False) -> Optional[str]:
    """
    Prints all the informatation that could be useful for debugging purposes.
    Currently, this includes:

    * The versions of the packages used by Lux
    * Info about the current state of luxwidget

    Parameters
    ----------
    return_string: Whether to return the versions as a string or print them.

    Returns
    -------
    If return_string is True, returns a string with the debug info else the
    string will be printed and None is returned.
    """
    pass


def notebook_enabled() -> tp.Tuple[bool, str]:
    pass


def lab_enabled() -> tp.Tuple[bool, str]:
    pass


def is_lab_notebook():
    pass


def check_luxwidget_enabled(return_string: bool = False) -> Optional[str]:
    # get the ipython shell
    import IPython

    ip = IPython.get_ipython()

    # return if the shell is not available
    if ip is None:
        return "❌ IPython shell note available.\nPlease note that Lux must be used within a notebook interface (e.g., Jupyter notebook, Jupyter Lab, JupyterHub, or VSCode)\n"
    is_lab = is_lab_notebook()

    if is_lab:
        msg = "✅ Jupyter Lab Running\n"
        enabled, emsg = lab_enabled()
        msg = msg + emsg
        if not enabled:
            msg += f"❌ WARNING: luxwidget is not enabled in Jupyter Lab."
            msg += "You may need to run the following code in your command line:\n"
            msg += "  jupyter labextension install @jupyter-widgets/jupyterlab-manager\n"
            msg += "  jupyter labextension install luxwidget"
        else:
            msg += "✅ luxwidget is enabled"

    else:
        msg = "✅ Jupyter Notebook Running\n"
        enabled, emsg = notebook_enabled()
        msg = msg + emsg
        if not enabled:
            msg += "❌ WARNING: luxwidget is not enabled in Jupyter Notebook.\n"
            msg += "You may need to run the following code in your command line:\n"
            msg += "  jupyter nbextension install --py luxwidget\n"
            msg += "  jupyter nbextension enable --py luxwidget"
        else:
            msg += "✅ luxwidget is enabled"

    if return_string:
        return msg


def _strip_ansi(source):
    pass


if __name__ == "__main__":
    check_luxwidget_enabled()
