"""
This is a dummy module that creates global caches so that we can test
the behavior of sims_clean_up()
"""
from rubin_sim.utils.CodeUtilities import sims_clean_up

__all__ = ["a_dict_cache", "a_list_cache"]

a_dict_cache = {}

a_list_cache = []

sims_clean_up.targets.append(a_dict_cache)
sims_clean_up.targets.append(a_list_cache)
