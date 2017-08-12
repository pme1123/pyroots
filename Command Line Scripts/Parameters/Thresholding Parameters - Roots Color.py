colors = {'dark_on_light': [False, True], 'band': [0, 2], 'colorspace': 'rgb'}
contrast_kernel_size = 500
threshold_args = [{'offset': -3, 'block_size': 151, 'param': 25.0}, {'offset': 3, 'block_size': 151, 'param': 25.0}]
mask_args = {'offset_y': 2, 'offset_x': 1.5, 'percentage_y': 89.5, 'rotation': 0, 'percentage_x': 94, 'rectangle': True}
noise_removal_args = {'radius_2': 2, 'radius_1': 0, 'median_iterations': 3}
morphology_filter_args = {'min_size': 0, 'strict_eccentricity': 0.95, 'loose_eccentricity': 0.5, 'strict_solidity': 0.6, 'min_length': 0, 'loose_solidity': 0.8}
fill_gaps_args = {'closing_radius': 3, 'median_radius': 1.6, 'min_hole_size': 100}
lw_filter_args = {'threshold': 5}
diam_filter_args = 'skip'
diameter_bins = 'skip'
