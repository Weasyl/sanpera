"""py.test configuration for this module.

Every Usage test function defines a `ctx` argument (short for 'context'), which
is a little helper object.  This file contains the py.test hook for creating
that helper object.
"""

import pytest

from sanpera.tests.im_usage.common import UsageContext


@pytest.fixture(scope="module")
def module_ctx(request):
    ctx = UsageContext()
    yield ctx
    ctx.destroy()


@pytest.fixture
def ctx(request, module_ctx):
    module_ctx.do_convert(request.function)
    return module_ctx
