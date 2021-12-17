# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

import rosmodex

###############################################################################
# Tests
###############################################################################


def test_import_was_ok():
    assert True


def test_pkg_has_version():
    assert hasattr(rosmodex, '__version__')
    assert isinstance(rosmodex.__version__, str)
    assert rosmodex.__version__ != ''
