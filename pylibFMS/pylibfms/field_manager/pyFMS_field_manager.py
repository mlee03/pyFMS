import dacite
from dataclasses import dataclass
from typing import List, Dict
import traceback

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
            print(f"ERROR FieldTable::__post_init__: Must specify {var} in field table")
            traceback.print_exc()

    @classmethod
    def from_dict(cls, config: Dict) -> "FieldTable":
        return dacite.from_dict(data_class=cls, data=config["field_table"][0])
    
    def add_to_varlist(self, var: Dict):
        try:
            self.varlist.append(var)
        except AttributeError:
            print("ERROR FieldTable::add_to_varlist: No varlist in field table, please define varlist")
            traceback.print_exc()

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
            print("ERROR FieldTable::get_var: No variable match")
            traceback.print_exc()
            
    def get_value(self, varname: str, key: str):
        try:
            var = self.get_var(varname)
            return var[key]
        except KeyError:
            print(f"ERROR FieldTable::get_value: No key '{key}' in {varname}")
            traceback.print_exc()
        except TypeError:
            print(f"ERROR FieldTable::get_value: No matching variable '{varname}")
            traceback.print_exc()
    
    def get_subparam_value(self, varname: str, listname: str, paramname: str):
        try:
            var = self.get_var(varname)
            subparamlist = var[listname]
            return subparamlist[0][paramname]
        except KeyError:
            print(f"ERROR FieldTable::get_subparam_value: No matching key in {varname} or {listname}")
            traceback.print_exc()
        except TypeError:
            print(f"ERROR FieldTable::get_subparam_value: No variable in variable list that matches '{varname}'")
            traceback.print_exc()
        except UnboundLocalError:
            print(f"ERROR FieldTable::get_subparam_value: No attribute '{listname}' key in {varname} dict")
            traceback.print_exc()
    
    
    def get_variable_list(self) -> List:
        variables = []
        for item in self.varlist:
            variables.append(item["variable"])
        return variables
    
    def get_subparam_list(self, varname: str) -> List[Dict]:
        subparamlist = []
        try:
            var = self.get_var(varname)
            for key in var:
                if type(var[key]) == list:
                    subparamlist.append(key)
            return subparamlist
        except TypeError:
            print(f"ERROR FieldType::get_subparam_list: No variable match")
            traceback.print_exc()
            
    def set_value(self, varname: str, key: str, value):
        try:
            changed_var = self.get_var(varname=varname)
            changed_var[key] = value
        except TypeError:
            print(f"ERROR FieldTable::set_value: No matching variable '{varname}' to set value of key '{key}'")
            traceback.print_exc()

    def set_subparam_value(self, varname: str, listname: str, subparamname: str, value):
        try:
            var = self.get_var(varname)
            paramlist = var[listname]
            paramlist[0][subparamname] = value
        except KeyError:
            print(f"ERROR FieldTable::set_subparam_value: No matching subparameter list '{listname}' or subparameter '{subparamname}'")
            traceback.print_exc()
        except TypeError:
            print(f"ERROR FieldTable::set_subparam_value: No matching variable '{varname}' or subparameter list '{listname}'")
            traceback.print_exc()

    def set_var_name(self, old_name: str, new_name: str):
        try:
            if self.get_var(new_name) is not None:
                raise FieldError
            changed_var = self.get_var(old_name)
            changed_var["variable"] = new_name
        except TypeError:
            print(f"ERROR FieldTable::set_var_name: No variable '{old_name}' in variable list")
            traceback.print_exc()
        except FieldError:
            print(f"ERROR FieldTable::set_var_name: Desired new variable name is already in variable list")
            traceback.print_exc()

    def set_var_attr_name(self, varname: str, oldname: str, newname: str):
        try:
            var = self.get_var(varname)
            if newname in var.keys():
                raise FieldError
            var[newname] = var.pop(oldname)
        except TypeError:
            print(f"ERROR FieldTable::set_var_attr_name: No variable '{varname}' or variable attribute '{oldname}'")
            traceback.print_exc()
        except FieldError:
            print(f"ERROR FieldTable::set_var_attr_name: variable attribute '{newname} already exists for '{varname}'")
            traceback.print_exc()
        except AttributeError:
            print(f"ERROR FieldTable::set_var_attr_name: No variable '{varname}' in variable list")
            traceback.print_exc()
        except KeyError:
            print(f"ERROR FieldTable::set_var_attr_name: No attribute '{oldname}' in '{varname}'")
            traceback.print_exc()

    def set_subparam_name(self, varname: str, listname: str, oldname: str, newname: str):
        try:
            var = self.get_var(varname)
            paramlist = var[listname]
            if newname in paramlist[0].keys():
                raise FieldError
            paramlist[0][newname] = paramlist[0].pop(oldname)
        except TypeError:
            print(f"ERROR FieldTable::set_subparam_name: No variable '{varname}' in variable list")
            print(f"Available variables: {self.get_variable_list()}")
            traceback.print_exc()
        except KeyError:
            print(f"ERROR FieldTable::set_subparam_name: No attribute '{listname}' in '{varname} or '{oldname}' in '{listname}'")
            traceback.print_exc()
        except FieldError:
            print(f"ERROR FieldTable::set_subparam_name: subparameter '{newname}' already in subparameter list")
            traceback.print_exc()