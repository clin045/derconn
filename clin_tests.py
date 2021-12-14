import derconn as dc
import numpy as np
from scipy import interpolate


def test_fit_curve():
    roi_ts = np.random.rand(240)
    vox_tss = [np.random.rand(240) for x in range(5)]
    func = interpolate.UnivariateSpline
    result = dc.fit_curve(roi_ts, vox_tss, func)

def test_derivtive_ratios():    
    roi_ts = np.random.rand(240)
    vox_tss = [np.random.rand(240) for x in range(5)]
    func = interpolate.UnivariateSpline
    result = dc.derivative_ratios(roi_ts, vox_tss, func)
    return result

def test_avg_ratios(ratios):
    return dc.avg_ratios(ratios)

if __name__=="__main__":
    test_fit_curve()
    ratios = test_derivtive_ratios()
    avg_vec = test_avg_ratios(ratios)
    print(avg_vec)