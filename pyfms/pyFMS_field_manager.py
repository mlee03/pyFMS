from dataclasses import dataclass
from typing import Any, Dict, List

import dacite
import yaml

from pyfms.pyFMS_error import pyfms_error


class FieldError(Exception):
    pass


@dataclass
class FieldTable:
    field_type: str
    modlist: List[Dict]

    @classmethod
    def from_file(cls, file_path: str) -> "FieldTable":
        """
        FieldTable class method for creating an instance from a yaml file

        Returns: instance of FieldTable
        """
        with open(file_path, "r") as f:
            config = yaml.safe_load(f)
        return FieldTable.from_dict(config)

    @classmethod
    def from_dict(cls, config: Dict) -> "FieldTable":
        """
        FieldTable class method for creating an instance from a dictionary.

        Returns: instance of FieldTable
        """
        return dacite.from_dict(data_class=cls, data=config["field_table"][0])

    def add_to_varlist(self, module: str, var: Dict):
        """
        Adds a variable to the varlist of module of
        calling FieldTable instance.

        Returns: Nothing to return, modifies calling instance
        """
        try:
            varlist = [mod for mod in self.modlist if mod["model_type"] == module][0][
                "varlist"
            ]
            varlist.append(var)
        except AttributeError:
            pyfms_error(
                "FieldTable",
                "add_to_varlist",
                "No varlist in field table, please define varlist",
            )

    def get_var(self, module: str, varname: str) -> Dict:
        """
        When called will return dictionary related to variable matching `varname`
        within module 'module', containg all current key:value pairs of the variable

        Returns: Dictionary
        """
        out = None
        try:
            for item in [mod for mod in self.modlist if mod["model_type"] == module][0][
                "varlist"
            ]:
                if varname == item["variable"]:
                    out = item
            if out is None:
                raise FieldError
        except FieldError:
            pyfms_error("FieldTable", "get_var", "No variable match")

        return out

    def get_subparam(self, module: str, varname: str, subparam_name: str) -> List[Dict]:
        """
        When called will return subparameter matching `subparam_name` of variable
        matching `varname` in module matching 'module'.

        Returns: List containing subparameter dictionary
        """
        subparam = None
        try:
            var = self.get_var(module=module, varname=varname)
            if var is not None:
                subparam = var[subparam_name]
            if subparam is None:
                raise FieldError
        except FieldError:
            pyfms_error("FieldTable", "get_subparam", "No subparam match")
        return subparam

    def get_value(self, module: str, varname: str, key: str) -> Any:
        """
        When called will return value of key matching 'key' in variable matching
        `varname` in module 'module'

        Returns: Any data type as values can be string or numeric
        """
        try:
            var = self.get_var(module=module, varname=varname)
            return var[key]
        except KeyError:
            pyfms_error("FieldTable", "get_value", f"No key '{key}' in {varname}")
        except TypeError:
            pyfms_error("FieldTable", "get_value", f"No matching variable '{varname}")

    def get_subparam_value(
        self, module: str, varname: str, listname: str, paramname: str
    ) -> Any:
        """
        When called will return value of parameter matching `paramname` contained within
        subparameter list matching `listname`, for variable matching `varname` within
        module 'module'.

        Returns: Any data type as values can be string or numeric
        """
        try:
            var = self.get_var(module=module, varname=varname)
            subparamlist = var[listname]
            return subparamlist[0][paramname]
        except KeyError:
            pyfms_error(
                "FieldTable",
                "get_subparam_value",
                f"No matching key in {varname} or {listname}",
            )
        except TypeError:
            pyfms_error(
                "FieldTable",
                "get_subparam_value",
                f"No variable in variable list that matches '{varname}'",
            )

    def get_variable_list(self, module: str) -> List:
        """
        When called will return list of variables contained within calling FieldTable
        instance specified module

        Returns: List of variables
        """
        variables = []
        varlist = [mod for mod in self.modlist if mod["model_type"] == module][0][
            "varlist"
        ]
        for item in varlist:
            variables.append(item["variable"])
        return variables

    def get_num_variables(self, module: str) -> int:
        """
        When called will return total number of variables associated with calling
        FieldTable instance specified module

        Returns: integer number of variables
        """
        varlist = [mod for mod in self.modlist if mod["model_type"] == module][0][
            "varlist"
        ]
        num_var = len(varlist)
        return num_var

    def get_subparam_list(self, module: str, varname: str) -> List[Dict]:
        """
        When called will return List of dictionary subparameters associated with
        variable matching `varname` of FieldTable instance specified module.

        Returns: List of dictionary objects
        """
        subparamlist = []
        try:
            var = self.get_var(module=module, varname=varname)
            for key in var:
                if type(var[key]) == list:
                    subparamlist.append(key)
        except TypeError:
            pyfms_error("FieldTable", "get_subparam_list", "No variable match")
        return subparamlist

    def get_num_subparam(self, module: str, varname: str) -> int:
        """
        When called will return number of subparameters associated with variable
        matching `varname` in calling FieldTable instance specified module.

        Returns: integer number of subparameters
        """
        subparamlist = []
        try:
            var = self.get_var(module=module, varname=varname)
            for key in var:
                if type(var[key]) == list:
                    subparamlist.append(key)
        except TypeError:
            pyfms_error("FieldTable", "get_num_subparam", "No variable match")
        return len(subparamlist)

    def set_value(self, module: str, varname: str, key: str, value):
        """
        This method sets the value associated with the key matching 'key' of the
        variable matching `varname` withing the calling FieldTable instance specified
        module.

        Returns: Nothing to return, modifies calling instance
        """
        try:
            changed_var = self.get_var(module=module, varname=varname)
            changed_var[key] = value
        except TypeError:
            pyfms_error(
                "FieldTable",
                "set_value",
                f"No matching variable '{varname}' to set value of key '{key}'",
            )

    def set_subparam_value(
        self, module: str, varname: str, listname: str, subparamname: str, value
    ):
        """
        This method sets the value associated with the key matching 'subparamname`
        within the subparameter list of the variable matching `varname` withing the
        calling FieldTable instance specified module.

        Returns: Nothing to return, modifies calling instance
        """
        try:
            var = self.get_var(module=module, varname=varname)
            paramlist = var[listname]
            paramlist[0][subparamname] = value
        except KeyError:
            pyfms_error(
                "FieldTable",
                "set_subparam_value",
                f"No matching subparameter list '{listname}' or subparameter '{subparamname}'",
            )
        except TypeError:
            pyfms_error(
                "FieldTable",
                "set_subparam_value",
                f"No matching variable '{varname}' or subparameter list '{listname}'",
            )

    def set_var_name(self, module: str, old_name: str, new_name: str):
        """
        This method changes the name of a currently existing variable matching `old_name`
        in the calling instance of FieldTable to `new_name` within specified module.

        Returns: Nothing to return, modifies calling instance
        """
        try:
            if self.get_var(module=module, varname=new_name) is not None:
                raise FieldError
            changed_var = self.get_var(module=module, varname=old_name)
            changed_var["variable"] = new_name
        except TypeError:
            pyfms_error(
                "FieldTable",
                "set_var_name",
                f"No variable '{old_name}' in variable list",
            )
        except FieldError:
            pyfms_error(
                "FieldTable",
                "set_var_name",
                "Desired new variable name is already in variable list",
            )

    def set_var_attr_name(self, module: str, varname: str, oldname: str, newname: str):
        """
        This method changes the name of a currently existing variable attribute matching
        `oldname` to `newname` in the variable matching `varname` of the calling instance
        of FieldTable of the specified module.

        Returns: Nothing to return, modifies calling instance
        """
        try:
            var = self.get_var(module=module, varname=varname)
            if newname in var.keys():
                raise FieldError
            var[newname] = var.pop(oldname)
        except TypeError:
            pyfms_error(
                "FieldTable",
                "set_var_attr_name",
                f"No variable '{varname}' or variable attribute '{oldname}'",
            )
        except FieldError:
            pyfms_error(
                "FieldTable",
                "set_var_attr_name",
                f"variable attribute '{newname} already exists for '{varname}'",
            )
        except AttributeError:
            pyfms_error(
                "FieldTable",
                "set_var_attr_name",
                f"No variable '{varname}' in variable list",
            )
        except KeyError:
            pyfms_error(
                "FieldTable",
                "set_var_attr_name",
                f"No attribute '{oldname}' in '{varname}'",
            )

    def set_subparam_name(
        self, module: str, varname: str, listname: str, oldname: str, newname: str
    ):
        """
        This method sets the subparameter name of subparameter in the variable matching
        `varname`, changing it `oldname` to `newname` in the calling instance of FieldTable's
        specified module.

        Returns: Nothing to return, modifies calling instance
        """
        try:
            var = self.get_var(module=module, varname=varname)
            paramlist = var[listname]
            if newname in paramlist[0].keys():
                raise FieldError
            paramlist[0][newname] = paramlist[0].pop(oldname)
        except TypeError:
            pyfms_error(
                "FieldTable",
                "set_subparam_name",
                f"No variable '{varname}' in variable list",
            )
            print(f"Available variables: {self.get_variable_list(module=module)}")
        except KeyError:
            pyfms_error(
                "FieldTable",
                "set_subparam_name",
                f"No attribute '{listname}' in '{varname} or '{oldname}' in '{listname}'",
            )
        except FieldError:
            pyfms_error(
                "FieldTable",
                "set_subparam_name",
                f"subparameter '{newname}' already in subparameter list",
            )

    # Tracer method
    def check_if_prognostic(self, module: str, tracername: str) -> bool:
        """
        This method checks if the tracer matching `tracername` is prognostic or
        diagnostic of the specified. This is done by checking the value of the
        `tracer_type` key of the tracer.

        Returns: True if prognostic, False otherwise
        """
        tracer = self.get_var(module=module, varname=tracername)
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
                return False
        except FieldError:
            pyfms_error("TracerTable", "check_if_prognostic", "tracer_type is unknown")

        except KeyError:
            pyfms_error(
                "TracerTable",
                "check_if_prognostic",
                f"{tracername} not found in TracerTable",
            )

        return None

    # Tracer method
    def adjust_mass(self):
        model = self.model_type
        # TODO: Get list of models which need mass adjustment

    # Tracer method
    def adjust_positive_def(self):
        model = self.model_type
        # TODO: Get list of models which need to be adjusted to remain positive definite
