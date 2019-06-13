#!/usr/bin/env python

import fire

from core import JobHandler

__author__ = "Robert Focke"
__copyright__ = "Copyright 2018-2019, Robert Focke"
__credits__ = ["Robert Focke"]
__license__ = "Apache 2.0"
__version__ = "0.1"
__maintainer__ = "Robert Focke"
__email__ = "robert.focke@member.fsf.org"
__status__ = "Alpha"

if __name__ == '__main__':
	fire.Fire(JobHandler)
