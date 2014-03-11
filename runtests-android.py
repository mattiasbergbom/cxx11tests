#!/usr/bin/env python

LINEWIDTH = 80
COLORIZED = True

import os
import shlex
import subprocess
import sys
try:
    from shlex import quote
except ImportError:
    from pipes import quote

android_mk_header = """
LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_CFLAGS += -std=c++11

LOCAL_MODULE    := cxx11tests
LOCAL_SRC_FILES := """

android_mk_tail = "\n\ninclude $(BUILD_SHARED_LIBRARY)\n"

def main():
    cpp_filenames = [f for f in os.listdir('jni') if f.endswith(".cpp")]
    for cpp_filename in cpp_filenames:
        android_mk_content = "".join((android_mk_header, cpp_filename, android_mk_tail))
        with open("jni/Android.mk", 'w') as android_mk:
            android_mk.write(android_mk_content)
        testname = cpp_filename
        logfile = cpp_filename + ".log"
        cmds = ["/Users/rj/android/android-ndk-r9c/ndk-build"]

        # Run test and save results
        with open(logfile, 'w') as f:
            cmd = ' '.join(map(quote, cmds))
            f.write("# Command executed: ")
            f.write(cmd)
            f.write('\n')
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 universal_newlines=True, shell=True)
            out, _ = p.communicate()
            f.write(out)
            returncode = p.returncode

            # Check returncode to set status
            if returncode == 0:
                status = True
                statustext = 'PASS'
            else:
                status = False
                statustext = 'FAIL'

            # Add coloring if desired
            use_colors = COLORIZED
            if 'COLORIZED' in os.environ:
                use_colors = True if os.environ['COLORIZED'] == '1' else False
            if use_colors and sys.stdout.isatty():
                if status:
                    statustext = '\033[32m' + statustext + '\033[0m'
            else:
                statustext = '\033[31m' + statustext + '\033[0m'

        # Print status
        print("{t} {d} {s}".format(t=testname,
                                   d=(LINEWIDTH-len(testname)-4-2)*'.',
                                   s=statustext))

if __name__ == '__main__':
    sys.exit(main())
