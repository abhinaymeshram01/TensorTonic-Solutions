def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_val = min(values)
    max_val = max(values)
    bin_width = (max_val - min_val)/num_bins
    bins = []
    for i in values:
        if bin_width == 0:
            bins.append(0)
        else:
            index = int((i-min_val)/bin_width)
            if index >= num_bins:
                index = num_bins -1

            bins.append(index)
    return bins