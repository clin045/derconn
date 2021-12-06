import argparse
import derconn as dc
from nilearn import input_data, datasets
import numpy as np
from scipy import interpolate
import os

def dir_path(string):
    if os.path.exists(string):
        return string
    else:
        raise NotADirectoryError(string)

# For testing purposes! Change call to dc.extract_ts when ready
def extract_ts(roi, rs):
    print("ROI file: " + roi)
    print("rs file: " + rs)
    return np.random.rand(240), [np.random.rand(240) for x in range(5)]

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ROI",type=dir_path)
    parser.add_argument("rsfile",type=dir_path)
    args = parser.parse_args()
    roi_ts, vox_ts = extract_ts(args.ROI, args.rsfile)
    ratios = dc.derivative_ratios(roi_ts, vox_ts, interpolate.UnivariateSpline)
    avg_ratios = dc.avg_ratios(ratios)
    print(avg_ratios.shape)

    

