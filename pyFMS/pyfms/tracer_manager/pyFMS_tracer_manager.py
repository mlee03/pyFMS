import sys
import dataclasses
import ctypes as ct
from mpi4py import MPI
import numpy as np

from pyFMS import lowercase, write_version_number

import pyFMS_file_version

from pylibFMS.field_manager.pyFMS_field_manager import(
    pyFMS_Field_Manager,
    get_field_info,
    get_field_methods,
    MODEL_ATMOS,
    MODEL_LAND,
    MODEL_OCEAN,
    MODEL_ICE,
    MODEL_COUPLER,
    NUM_MODELS,
    method_type,
    default_method,
    parse,
    fm_copy_list,
    fm_change_list,
    fm_modify_name,
    fm_query_method,
    fm_new_value,
    fm_exists,
    MODEL_NAMES,
)

@dataclasses.dataclass
class tracer_type:
    tracer_name: str
    tracer_units: str
    tracer_longname: str
    num_methods: int
    model: int
    instances: int
    is_prognostic: bool
    instances_set: bool
    needs_init: bool
    needs_mass_adjust: bool = True
    needs_positive_adjust: bool = True

@dataclasses.dataclass
class tracer_name_type:
    model_name: str
    tracer_name: str
    tracer_units: str
    tracer_longname: str

@dataclasses.dataclass
class inst_type:
    name: str
    instances: int


class pyFMS_Tracer_Manager:
    NUM_TRACER_FIELDS = 0
    MAX_TRACER_FIELDS = 250
    MAX_TRACER_METHOD = 20
    NO_TRACER = 1 - sys.maxsize
    NOTRACER = -sys.maxsize
    TRACERS = []
    INSTANTIATIONS = []
    TOTAL_TRACERS = np.empty(shape=(NUM_MODELS), dtype=int)
    PROG_TRACERS = np.empty(shape=(NUM_MODELS), dtype=int)
    DIAG_TRACERS = np.empty(shape=(NUM_MODELS), dtype=int)
    MODEL_REGISTERED = np.full(shape=(NUM_MODELS), fill_value=False)
    
    MODULE_IS_INITIALIZED = False
    VERBOSE_LOCAL = False
    TRACER_ARRAY = np.empty(shape=(NUM_MODELS,MAX_TRACER_FIELDS), dtype=int)

    def __init__(self):
        self.MODULE_IS_INITIALIZED = True
        self.field_manager = pyFMS_Field_Manager()
        self.TRACER_ARRAY = self.NOTRACER

    def get_tracer_meta_data(self, model: int):
        
        assert (model == MODEL_ATMOS or model == MODEL_LAND or 
                model == MODEL_OCEAN or model == MODEL_ICE or 
                model == MODEL_COUPLER), "tracer_manager_init : invalid model type"
        
        if self.MODEL_REGISTERED[model]:
            num_tracers = self.TOTAL_TRACERS[model]
            num_prog = self.PROG_TRACERS[model]
            num_diag = self.DIAG_TRACERS[model]
            return num_tracers, num_prog, num_diag
        
        num_tracers = 0
        num_prog = 0
        num_diag = 0

        nfields = self.field_manager.nfields
        

