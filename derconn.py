import numpy as np
import nibabel as nib


def test_function():
    print("This is a test!")

def extract_ts(roi_path, rs_path):
    roi_msk_img = nib.load(roi_path)
    roi_msk_dat = roi_msk_img.get_fdata()
    rs = np.load('rs_path')

    roi_msk_dat[roi_msk_dat != 0] = 1
    rs[roi_msk_dat]

    nilearn niftimasker.transform()
