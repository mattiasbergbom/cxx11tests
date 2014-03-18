#!/usr/bin/env python

import os
import subprocess

if __name__ == '__main__':
    subprocess.Popen( 'xcodebuild', shell=True, cwd = os.path.dirname( os.path.realpath( __file__ ) ) ).wait()
