import derconn as dc
import numpy as np
from scipy import interpolate


def test_fit_curve():
    roi_ts = np.random.rand(240)
    vox_tss = [np.random.rand(240) for x in range(5)]
    func = interpolate.UnivariateSpline
    dc.fit_curve(roi_ts, vox_tss, func)


if __name__=="__main__":
    test_fit_curve()