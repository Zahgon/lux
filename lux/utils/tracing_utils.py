import inspect
import sys
import pickle as pkl
import lux
import autopep8
import math
import os


class LuxTracer:
    def profile_func(self, frame, event, arg):
        # Profile functions should have three arguments: frame, event, and arg.
        # frame is the current stack frame.
        # event is a string: 'call', 'return', 'c_call', 'c_return', or 'c_exception'.
        # arg depends on the event type.
        # See: https://docs.python.org/3/library/sys.html#sys.settrace
        pass

    def start_tracing(self):
        # print ("-----------start_tracing-----------")
        # Implement python source debugger: https://docs.python.org/3/library/sys.html#sys.settrace
        # setprofile faster than settrace (only go through I/O)
        pass

    def stop_tracing(self):
        # print ("-----------stop_tracing-----------")
        pass

    def process_executor_code(self, executor_lines):
        pass
