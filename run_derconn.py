import argparse
import derconn as dc
from nilearn import input_data, datasets
import numpy as np
from scipy import interpolate
from nimlab import datasets as nimds
import os

def path(string):
    if os.path.exists(string):
        return string
    else:
        raise NotADirectoryError(string)

# For testing purposes! Change call to dc.extract_ts when ready
def extract_ts(roi, rs):
    mask_size = np.count_nonzero(nimds.get_img("MNI152_T1_1mm_brain_mask_dil").get_fdata())
    print("Mask size: " + str(mask_size))
    print("ROI file: " + roi)
    print("rs file: " + rs)
    return np.random.rand(240), [np.random.rand(240) for x in range(mask_size)]

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ROI",type=path)
    parser.add_argument("rsfile",type=path)
    parser.add_argument("outfile",type=str)
    masker = input_data.NiftiMasker(nimds.get_img("MNI152_T1_1mm_brain_mask_dil")).fit()
    args = parser.parse_args()
    roi_ts, vox_ts = extract_ts(args.ROI, args.rsfile)
    ratios = dc.derivative_ratios(roi_ts, vox_ts, interpolate.UnivariateSpline)
    avg_ratios = dc.avg_ratios(ratios)
    result_img = masker.inverse_transform(avg_ratios)
    result_img.to_filename(args.outfile)



