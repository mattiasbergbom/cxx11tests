#!/usr/bin/env python

import os
import sys
import subprocess

if __name__ == '__main__':
    retcode = subprocess.Popen( 'xcodebuild', shell=True, cwd = os.path.dirname( os.path.realpath( __file__ ) ) ).wait()
    sys.exit( retcode )
