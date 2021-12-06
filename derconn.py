import numpy as np
from scipy import optimize
from scipy import misc

def test_function():
    print("This is a test!")

def fit_curve(roi_ts, vox_tss, f):
    roi_curve = f(np.arange(0,len(roi_ts)),roi_ts)
    vox_curves = []
    for v in vox_tss:
        vox_curve = f(np.arange(0,len(v)),v)
        vox_curves.append(vox_curve)

    return roi_curve, vox_curves

def derivative_ratios(roi_ts, vox_tss, f):
    if len(roi_ts) != len(vox_tss[0]):
        raise ValueError("ROI and voxel timeseries must have same len!")
    roi_curve, vox_curves = fit_curve(roi_ts, vox_tss, f)
    ratios = np.zeros((len(vox_curves), len(roi_ts)))
    for i in range(len(roi_ts)):
        for vidx, v in enumerate(vox_curves):
            ratios[vidx, i] = roi_curve(i) / v(i)
    return ratios

def avg_ratios(ratios):
    avg_vec = np.mean(ratios, axis=0)
    return avg_vec