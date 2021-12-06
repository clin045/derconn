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

    MNI_brain_mask = nimds.get_img("MNI152_T1_2mm_brain_mask_dil")
    brain_masker = input_data.NiftiMasker(MNI_brain_mask)
    roi_msk = brain_masker.fit_transform(roi_img)
    roi_msk = np.repeat(roi_msk, rs.shape[0], axis = 0)

    rs_mskd = rs * roi_msk
    roi_ts = np.mean(rs_mskd, 1)
    vox_tss = rs

    return roi_ts, vox_tss

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
