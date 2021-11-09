import pytest
import unittest

from pyCascadingCondition import CascadingCondition


def test_c_is_instance_of_CascadingCondition():
    c = CascadingCondition()
    assert isinstance(c, CascadingCondition)


def test_raise_exception_if_be_passed_scalare():
    c = CascadingCondition()
    with pytest.raises(Exception) as _:
        c(1, 1)
