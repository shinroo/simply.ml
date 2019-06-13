#!/usr/bin/env python

import sys
import fire

from plugin_manifest import plugin_manifest

__author__ = "Robert Focke"
__copyright__ = "Copyright 2018-2019, Robert Focke"
__credits__ = ["Robert Focke"]
__license__ = "Apache 2.0"
__version__ = "0.1"
__maintainer__ = "Robert Focke"
__email__ = "robert.focke@member.fsf.org"
__status__ = "Alpha"

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('please specify the job type: python3 cli.py <job-type> <args>')
	else:
		fire.Fire(plugin_manifest[str(sys.argv[1])]['cli'])
