import dacite
from dataclasses import dataclass
from typing import List, Dict

from pyfms.pyFMS_error import pyfms_error

class FieldError(Exception):
    pass

@dataclass
class FieldTable:
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
    def from_dict(cls, config: Dict) -> "FieldTable":
        return dacite.from_dict(data_class=cls, data=config["field_table"][0])
    
    def add_to_varlist(self, var: Dict):
        try:
            self.varlist.append(var)
        except AttributeError:
            pyfms_error("FieldTable", "add_to_varlist", "No varlist in field table, please define varlist")

    def get_var(self, varname: str) -> Dict:
        out = None
        try:
            for item in self.varlist:
                if varname == item["variable"]:
                    out = item
                    return out
            if out == None:
                raise FieldError
        except FieldError:
            pyfms_error("FieldTable", "get_var", "No variable match")

    def get_subparam(self, varname: str, subparam_name: str) -> List[Dict]:
        subparam = None
        try:
            var = self.get_var(varname)
            if var is not None:
                subparam = var[subparam_name]
                return subparam
            if subparam == None:
                raise FieldError
        except FieldError:
            pyfms_error("FieldTable", "get_subparam", "No subparam match")
            
    def get_value(self, varname: str, key: str):
        try:
            var = self.get_var(varname)
            return var[key]
        except KeyError:
            pyfms_error("FieldTable", "get_value", f"No key '{key}' in {varname}")
        except TypeError:
            pyfms_error("FieldTable", "get_value", f"No matching variable '{varname}")
    
    def get_subparam_value(self, varname: str, listname: str, paramname: str):
        try:
            var = self.get_var(varname)
            subparamlist = var[listname]
            return subparamlist[0][paramname]
        except KeyError:
            pyfms_error("FieldTable", "get_subparam_value", f"No matching key in {varname} or {listname}")
        except TypeError:
            pyfms_error("FieldTable", "get_subparam_value", f"No variable in variable list that matches '{varname}'")
    
    def get_variable_list(self) -> List:
        variables = []
        for item in self.varlist:
            variables.append(item["variable"])
        return variables
    
    def get_num_variables(self) -> int:
        num_var = len(self.varlist)
        return num_var
    
    def get_subparam_list(self, varname: str) -> List[Dict]:
        subparamlist = []
        try:
            var = self.get_var(varname)
            for key in var:
                if type(var[key]) == list:
                    subparamlist.append(key)
            return subparamlist
        except TypeError:
            pyfms_error("FieldTable", "get_subparam_list", "No variable match")

    def get_num_subparam(self, varname: str) -> int:
        subparamlist = []
        try:
            var = self.get_var(varname)
            for key in var:
                if type(var[key]) == list:
                    subparamlist.append(key)
            return len(subparamlist)
        except TypeError:
            pyfms_error("FieldTable", "get_num_subparam", "No variable match")
            
    def set_value(self, varname: str, key: str, value):
        try:
            changed_var = self.get_var(varname=varname)
            changed_var[key] = value
        except TypeError:
            pyfms_error("FieldTable", "set_value", f"No matching variable '{varname}' to set value of key '{key}'")

    def set_subparam_value(self, varname: str, listname: str, subparamname: str, value):
        try:
            var = self.get_var(varname)
            paramlist = var[listname]
            paramlist[0][subparamname] = value
        except KeyError:
            pyfms_error("FieldTable", "set_subparam_value", f"No matching subparameter list '{listname}' or subparameter '{subparamname}'")
        except TypeError:
            pyfms_error("FieldTable", "set_subparam_value", f"No matching variable '{varname}' or subparameter list '{listname}'")

    def set_var_name(self, old_name: str, new_name: str):
        try:
            if self.get_var(new_name) is not None:
                raise FieldError
            changed_var = self.get_var(old_name)
            changed_var["variable"] = new_name
        except TypeError:
            pyfms_error("FieldTable", "set_var_name", f"No variable '{old_name}' in variable list")
        except FieldError:
            pyfms_error("FieldTable", "set_var_name", "Desired new variable name is already in variable list")

    def set_var_attr_name(self, varname: str, oldname: str, newname: str):
        try:
            var = self.get_var(varname)
            if newname in var.keys():
                raise FieldError
            var[newname] = var.pop(oldname)
        except TypeError:
            pyfms_error("FieldTable", "set_var_attr_name", f"No variable '{varname}' or variable attribute '{oldname}'")
        except FieldError:
            pyfms_error("FieldTable", "set_var_attr_name", f"variable attribute '{newname} already exists for '{varname}'")
        except AttributeError:
            pyfms_error("FieldTable", "set_var_attr_name", f"No variable '{varname}' in variable list")
        except KeyError:
            pyfms_error("FieldTable", "set_var_attr_name", f"No attribute '{oldname}' in '{varname}'")

    def set_subparam_name(self, varname: str, listname: str, oldname: str, newname: str):
        try:
            var = self.get_var(varname)
            paramlist = var[listname]
            if newname in paramlist[0].keys():
                raise FieldError
            paramlist[0][newname] = paramlist[0].pop(oldname)
        except TypeError:
            pyfms_error("FieldTable", "set_subparam_name", f"No variable '{varname}' in variable list")
            print(f"Available variables: {self.get_variable_list()}")
        except KeyError:
            pyfms_error("FieldTable", "set_subparam_name", f"No attribute '{listname}' in '{varname} or '{oldname}' in '{listname}'")
        except FieldError:
            pyfms_error("FieldTable", "set_subparam_name", f"subparameter '{newname}' already in subparameter list")