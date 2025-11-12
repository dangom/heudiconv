#!/usr/bin/env python
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the Heudiconv package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

# This file is kept for backwards compatibility only.
# All configuration has been moved to pyproject.toml

if __name__ == "__main__":
    import sys
    from setuptools import setup
    
    sys.stderr.write(
        "WARNING: setup.py is deprecated. "
        "Please use 'pip install .' instead of 'python setup.py install'.\n"
    )
    setup()
