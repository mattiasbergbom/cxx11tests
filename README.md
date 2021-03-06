cxx11tests
==========

TL;DR
-----

Collection of tests to check which C++11 features are supported by a specific
(pre-installed) compiler.

*This is work in progress, so check again for new tests and bugfixes.*


Intent
------

The idea was to create a lightweight and easy to use test if one needs to know
wether a *specific, pre-installed* compiler supports certain features of C++11.
While most compiler vendors and open-source projects publish a list of features
that are supported, some of the lists are out of date, do not show the status
for Subversion/Git versions or are incomplete as far as the C++11 features go.

Especially in scientific computing, users are often stuck with whatever compiler
and compiler version the vendors of a supercomputer deem to be fit for their
machines. This can be very frustrating if a reasarch code is to be ported to
C++11, and it is tedious to find out which compilers will still be able to
compile the code. For that reason, this test suite was created to give users a
straightforward tool for the path to C++11.


Coverage
--------

The following C++11 features are checked (excerpt - for the full list, check out
the `src/` directory, as all files are named after the feature they are
checking):

*   C99 features: `long long`, vararg macros
*   `alignas`, `alignof`
*   `auto`
*   `constexpr`
*   `decltype`
*   `default`'d, `delete`'d (member) functions
*   `final`, `override`
*   `nullptr`
*   `std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`
*   alias templates and `using` as typedef
*   default member initialization
*   delegating constructors, inheriting constructors
*   enums (strongly typed, enum classes)
*   generalized functors, `std::function`, `std::bind`
*   initializer lists
*   inline namespaces
*   lambdas
*   local types as template arguments
*   nested template closer
*   range-based for
*   raw string literals
*   rvalue references, move support, perfect forwarding
*   static assertions
*   tuples
*   unicode character types
*   unicode string literals
*   uniform initialization syntax
*   variadic templates
*   new header files: `array`, `chrono`, `condition_variable`, `forward_list`, `functional`, `future`, `initializer_list`, `mutex`, `regex`, `thread`, `tuple`, `unordered_set`, `unordered_map`



Installation & Requirements
---------------------------

The following software packages are needed to run cxx11tests:

*   Python >= 2.7
*   GNU Make
*   any C++ compiler

There is no installation necessary, just obtain cxx11tests and you are good to
go.

### iOS


In order to run the iOS port of the tests, these requirements replace the above ones:

*   Python >= 2.5
*   Xcode >= 5
*   Xcode commandline tools
*   Xcode developer certificate (see https://developer.apple.com/support/technical/certificates/)

Usage
-----

After downloading (and unpacking, if necessary), enter the cxx11tests directory.
To prepare the tests, you need to run the `configure.py` script once to generate
the Makefile that will run the tests. The configure script respects three
environment variables that you may use to set the compiler command and any
necessary flags:

*   `CXX`: Set this variable to the compiler executable (default: 'g++').
*   `CPPFLAGS`: Use to specify additional preprocessor flags (default: '').
*   `CXXFLAGS`: Use to specify additional compiler flags (default: '').

If you want to check e.g. the currently installed GNU compiler, you could run
configure as

    CXX=g++ CXXFLAGS=-std=c++11 ./configure.py

You may also run the configure script from another directory (out-of-source
tests).

You can also provide the compiler name and flags via commandline
arguments. Simply replace the above by

    ./configure.py --cxx=g++ --cxxflags="-std=c++11"

After running the configure script, you can run the tests using `make`. By
default, all tests are run. To start them, just execute

    make

and and wait for the tests to finish. Make will not stop after failed tests, but
continue until all tests have been run. On subsequent calls to `make`, only
tests that previously failed will be run again. To override this behavior and
run all tests regardless of their previous status, run the 'force' target, i.e.

    make force

If you want to clean out all previously run tests, call `make clean`. `make
distclean` will also delete the Makefile, so you will have to run the configure
script again (it should leave you with a directory as you hadwhen obtaining
cxx11tests.). Note that you do not need to call `make distclean` if you want to
configure a new compiler - `configure.py` will do that for you. If you want to
get a list of all targets you can build, just call `make help`.

By default, the test results will be colored for easier recognition of failed
tests. You can switch of colors by setting the environment variable `COLORIZED`
to '0' (zero), or my calling make with

    make COLORIZED=0

### iOS

The iOS tests are launched like so:

    ios/test_ios.py

At present this simply executes xcodebuild in the 'ios' subdirectory, which holds a
mocked up Xcode project that references the same source files as the base test suite.
If the build succeeds all features are supported, otherwise the Xcode error output will
indicate which feature(s) is/are missing.

Contributions
-------------

Please feel free to add improvements to the test suite. I will be happy to
review and add your contributions if you send me a pull request or a patch.
