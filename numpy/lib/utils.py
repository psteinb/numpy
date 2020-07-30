import functools
import

import numpy as np
from numpy.core import overrides

array_function_dispatch = functools.partial(
    overrides.array_function_dispatch, module='numpy')


__all__ = [
    'summary'
    ]



def _summary_dispatcher(a, axis=None):
    return ""


@array_function_dispatch(_summary_dispatcher)
def summary(a, axis=None):
    """
    Provide a concise list of summary statistics of the provided array

    Returns a string that contains the summary

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : {int, sequence of int, None}, optional
        Axis or axes along which the statistics are computed. The default
        is to compute the median along a flattened version of the array.

    Returns
    -------
    summary : str
        A summary string that lists the minimum, the 25% percentile, the mean,
        the standard deviation, the median, the 75% percentile and the
        maximum of the provided array

    Notes
    -----
    Given a vector ``a`` of length ``N``, the summary function prints summary
    statistics of the provided array

    Examples
    --------
    >>> a = np.random.normal(size=20)
    >>> print(summary(a))
                min     25perc       mean      stdev     median     75perc        max
          -2.289870  -2.265757  -0.083213   1.115033  -0.162885  -2.217532   1.639802
    >>> a = np.reshape(a, newshape=(4,5))
    >>> print(summary(a,axis=1))
                min     25perc       mean      stdev     median     75perc        max
       0  -0.976279  -0.974090   0.293003   1.009383   0.466814  -0.969712   1.519695
       1  -0.468854  -0.467739   0.184139   0.649378  -0.036762  -0.465510   1.303144
       2  -2.289870  -2.276455  -0.324450   1.230031  -0.289008  -2.249625   1.111107
       3  -1.782239  -1.777304  -0.485546   1.259598  -1.236190  -1.767434   1.639802
    """
    hfmt = "{0:4s} {1:>10s} {2:>10s} {3:>10s} {4:>10s} {5:>10s} {6:>10s} {7:>10s}"
    header = hfmt.format(" ", "min", "25perc", "mean", "stdev", "median", "75perc", "max")

    value = header
    value += os.linesep
    if axis is not None:
        rfmt = "{0:4s} {1:10f} {2:10f} {3:10f} {4:10f} {5:10f} {6:10f} {7:10f}"
        value += rfmt.format(" ", np.min(a), np.percentile(a, q=.25), np.mean(a),
                             np.std(a), np.median(a), np.percentile(a, q=.75),
                             np.max(a)
        )
    else:
        vals_min = np.min(a, axis=axis)
        vals_percentile25 = np.percentile(a, q=.25, axis=axis)
        vals_mean = np.mean(a, axis=axis)
        vals_std = np.std(a, axis=axis)
        vals_median = np.median(a, axis=axis)
        vals_percentile75 = np.percentile(a, q=.75, axis=axis)
        vals_max = np.max(a, axis=axis)
        rfmt = "{0:4d} {1:10f} {2:10f} {3:10f} {4:10f} {5:10f} {6:10f} {7:10f}"

        for i in range(len(vals_min)):
            value += rfmt.format(i, vals_min[i], vals_percentile25[i], vals_mean[i],
                                 vals_std[i], vals_median[i], vals_percentile75[i],
                                 vals_max[i])
            if i != (len(vals_min) - 1):
                value += os.linesep

    return value
