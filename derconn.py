import numpy as np
import nibabel as nib
from nilearn import image, input_data
from nimlab import datasets as nimds

def test_function():
    print("This is a test!")

def extract_ts(roi_path, rs_path):
    roi_img = nib.load(roi_path)
    roi_dat = roi_img.get_fdata()
    rs = np.load(rs_path)

    MNI_brain_mask = nimds.get_img("MNI152_T1_2mm_brain_mask")
    brain_masker = input_data.NiftiMasker(MNI_brain_mask)
    roi_msk = brain_masker.fit_transform(roi_img)
    roi_msk = np.repeat(roi_msk, rs.shape[0], axis = 0)

    rs_mskd = rs * roi_msk
    roi_ts = np.mean(rs_mskd, 1)
    vox_tss = rs

    return roi_ts, vox_tss
