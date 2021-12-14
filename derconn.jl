using PyCall, Interpolations, ForwardDiff, ProgressMeter, Statistics

function run_tests()
    roi_ts = rand(240)
    vox_tss = [rand(240) for x in 1:280000]
    ratios = derivative_ratios(roi_ts, vox_tss)
end

function main()
    pushfirst!(PyVector(pyimport("sys")."path"), "")
    dc = pyimport("derconn")
    (roi_ts, vox_tss) = dc.extract_ts("/PHShome/cl20/software_env/python_modules/tests/standards/lesions/01.nii.gz",
                "/data/nimlab/connectome_npy/yeo1000_dil/081108_KY89TK.npy")
    
    ratios = derivative_ratios(roi_ts, convert(Matrix{Float32}, vox_tss))
    #display(ratios)
    mean_ratios = mean(ratios, dims=2)
    display(vec(mean_ratios))
    dc.write_vec_to_file(vec(mean_ratios),"test_output.nii.gz")
end

function fit_curve(roi_ts, vox_tss)
    println("fitting curves")
    f  = Interpolations.CubicSplineInterpolation
    roi_curve = f(1:length(roi_ts),roi_ts)
    vox_curves = Vector{Any}(undef, size(vox_tss)[2])
    
    @showprogress for i in 1:size(vox_tss)[2]
        vox_curves[i] = f(1:length(roi_ts),vox_tss[:,i])
    end
    return roi_curve, vox_curves
end

function derivative_ratios(roi_ts, vox_tss)
    println(typeof(roi_ts))
    println(size(roi_ts))
    println(typeof(vox_tss))
    println(size(vox_tss))
    println("calculating derivative ratios")
    (roi_curve, vox_curves) = fit_curve(roi_ts, vox_tss)
    ratios = zeros(size(vox_tss)[2], length(roi_ts))
    println("Take roi derivative")
    roi_ders = [ForwardDiff.derivative(roi_curve, t) for t in 1:length(roi_ts)]
    println("Take voxel derivatives")
    @showprogress for (vidx, v) in enumerate(vox_curves)
        vox_ders = [ForwardDiff.derivative(v, t) for t in 1:length(roi_ts)]
        #display(vox_ders)
        rat = roi_ders ./ vox_ders
        ratios[vidx,:] = rat
    end
    return ratios

end

main()

