using PyCall, Interpolations, ForwardDiff, ProgressMeter

function run_tests()
    roi_ts = rand(240)
    vox_tss = [rand(240) for x in 1:280000]
    ratios = derivative_ratios(roi_ts, vox_tss)
end

function fit_curve(roi_ts, vox_tss)
    println("fitting curves")
    f  = Interpolations.CubicSplineInterpolation
    roi_curve = f(1:length(roi_ts),roi_ts)
    vox_curves = Vector{Any}(undef, length(vox_tss))
    @showprogress for (idx, v) in enumerate(vox_tss)
        vox_curves[idx] = f(1:length(roi_ts),v)
    end
    return roi_curve, vox_curves
end

function derivative_ratios(roi_ts, vox_tss)
    println("calculating derivative ratios")
    (roi_curve, vox_curves) = fit_curve(roi_ts, vox_tss)
    ratios = zeros(length(vox_tss), length(roi_ts))
    roi_ders = [ForwardDiff.derivative(roi_curve, t) for t in 1:length(roi_ts)]
    @showprogress for (vidx, v) in enumerate(vox_curves)
        vox_ders = [ForwardDiff.derivative(v, t) for t in 1:length(roi_ts)]
        rat = roi_ders ./ vox_ders
        ratios[vidx,:] = rat
    end
    return ratios

end


