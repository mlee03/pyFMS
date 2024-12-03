import dacite
from dataclasses import dataclass
from typing import List, Dict

from pyfms.pyFMS_error import pyfms_error
from pyfms.field_manager.pyFMS_field_manager import FieldTable, FieldError

@dataclass
class TracerTable(FieldTable):
    field_type: str
    modlist: List[Dict]

    def __post_init__(self):
        try:
            if "model_type" in self.modlist[0]:
                self.model_type = self.modlist[0]["model_type"]
            else:
                var = "model_type"
                raise FieldError
            if "varlist" in self.modlist[0]:
                self.varlist = self.modlist[0]["varlist"]
            else:
                var = "varlist"
                raise FieldError
        except FieldError:
            pyfms_error("FieldTable", "__post_init__", f"Must specify {var} in field table")

    @classmethod
    def from_dict(cls, config: Dict) -> "TracerTable":
        return dacite.from_dict(data_class=cls, data=config["field_table"][0])
    
    def check_if_prognostic(self, tracername: str)-> bool:
        tracer = self.get_var(varname=tracername)
        try:
            if "tracer_type" in tracer:
                tracer_type = tracer["tracer_type"]
                if tracer_type == "prognostic":
                    return True
                elif tracer_type == "diagnostic":
                    return False
                else:
                    raise FieldError
            else:
                return True
        except FieldError:
            pyfms_error("TracerTable", "check_if_prognostic", "tracer_type is unknown")

        except KeyError:
            pyfms_error("TracerTable", "check_if_prognostic", f"{tracername} not found in TracerTable")

    def adjust_mass(self):
        model = self.model_type
        # TODO: Get list of models which need mass adjustment

    def adjust_positive_def(self):
        model = self.model_type
        # TODO: Get list of models which need to be adjusted to remain positive definite