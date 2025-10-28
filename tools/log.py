# -*- coding: utf-8 -*-
from datetime import datetime

def print_logs_with_time(*args):
    """Prints logs with the current timestamp."""
    print(datetime.now(), *args)
