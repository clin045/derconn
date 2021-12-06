import numpy as np
from scipy import optimize
from scipy import misc

def test_function():
    print("This is a test!")

def fit_curve(roi_ts, vox_tss, f):
    roi_curve = f(np.arange(0,len(roi_ts)),roi_ts)
    vox_curves = []
    for v in vox_tss:
        vox_curve = f(np.arange(0,len(v),v))
        vox_curves.append(v)

    return roi_curve, vox_curves
