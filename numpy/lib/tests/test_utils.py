import warnings
import os
import pytest

import numpy as np
from numpy.utils import summary

class TestSummary:
    def test_basic(self):
        # assert_raises(ValueError, rot90, np.ones(4))
        # assert_raises(ValueError, rot90, np.ones((2,2,2)), axes=(0,1,2))
        # assert_raises(ValueError, rot90, np.ones((2,2)), axes=(0,2))
        # assert_raises(ValueError, rot90, np.ones((2,2)), axes=(1,1))
        # assert_raises(ValueError, rot90, np.ones((2,2,2)), axes=(-2,1))

        a = [[0, 1, 2],
             [3, 4, 5]]
        b1 = [[2, 5],
              [1, 4],
              [0, 3]]
        b2 = [[5, 4, 3],
              [2, 1, 0]]
        b3 = [[3, 0],
              [4, 1],
              [5, 2]]
        b4 = [[0, 1, 2],
              [3, 4, 5]]

        summ = summary(a)
        summ_lines = summ.split(os.linesep)

        assert len(summ_lines) == 2
        assert "min" in summ_lines[0]
        assert summ_lines[0].endswith("max")
