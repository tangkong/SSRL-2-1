print('-------------------40-plans.py startup file')

from ssrltools.plans import meshcirc, nscan, level_stage_single

# For scanning over all sample locations, try bp.list_scan or bp.list_grid_scan
# eg: bp.list_scan([dets], HiTpStage.sample_loc_list(), md={'sample': 'sample name', ...})
