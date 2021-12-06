import numpy as np
from scipy import optimize

def test_function():
    print("This is a test!")

def fit_curve(roi_ts, vox_tss, f):
    roi_curve = f(np.arange(0,len(roi_ts)),roi_ts)
    print(roi_curve)
    return
