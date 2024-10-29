import copy
import pytest
from pyfms import FieldTable, FieldError

test_config = {
    'field_table': [{
        'field_type': 'tracer', 
        'modlist': [{
            'model_type': 'atmos_mod', 
            'varlist': [{
                'variable': 'sphum', 
                'longname': 'specific humidity', 
                'units': 'kg/kg', 
                'profile_type': [{
                    'value': 'fixed', 
                    'surface_value': 3e-06
                    }]}, 
                {
                'variable': 'soa', 
                'longname': 'SOA tracer', 
                'units': 'mmr', 
                'convection': 'all', 
                'chem_param': [{
                    'value': 'aerosol', 
                    'frac_pm1': 0.89, 
                    'frac_pm25': 0.96, 
                    'frac_pm10': 1.0
                    }], 
                'profile_type': [{
                    'value': 'fixed', 
                    'surface_value': 1e-32
                    }]
                }]
            }]
        }]
    }



def test_fieldtable_init(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    assert isinstance(test_table, FieldTable)

def test_get_fieldtype(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    fieldtype = test_table.field_type
    assert fieldtype == 'tracer'

@pytest.mark.xfail(raises=FieldError)
def test_remove_varlist(test_config=test_config):
    changed_config = copy.deepcopy(test_config)
    del changed_config["field_table"][0]["modlist"][0]["varlist"]
    FieldTable.from_dict(changed_config)

def test_add_to_varlist(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    new_var = {
        "variable":"test", 
        "longname":"longtest", 
        "units": "m", 
        "profile_type":"fixed", 
        "subparams":[{"surface_value":1}]
        }
    test_table.add_to_varlist(new_var)
    assert new_var in test_table.varlist

@pytest.mark.xfail(raises=(AttributeError,FieldError))
def test_add_to_varlist_fail(test_config=test_config):
    changed_config = copy.deepcopy(test_config)
    del changed_config["field_table"][0]["modlist"][0]["varlist"]
    test_table = FieldTable.from_dict(changed_config)
    new_var = {
        "variable":"test", 
        "longname":"longtest", 
        "units": "m", 
        "profile_type":"fixed", 
        "subparams":[{"surface_value":1}]
        }
    test_table.add_to_varlist(new_var)

def test_get_var(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    var = test_table.get_var('soa')
    assert var == test_table.modlist[0]["varlist"][1]

@pytest.mark.xfail(raises=FieldError)
def test_get_var_fail(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    test_table.get_var('sob')

def test_get_value(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    value = test_table.get_value(varname="soa", key="units")
    assert value == "mmr"

@pytest.mark.xfail(raises=KeyError)
def test_get_value_key_fail(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    test_table.get_value(varname="soa", key="unit")

def test_get_subparam_value(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    value = test_table.get_subparam_value(varname="soa", listname="chem_param", paramname="frac_pm1")
    assert value == 0.89

@pytest.mark.xfail(raises=KeyError)
def test_get_subparam_value_bad_key(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    test_table.get_subparam_value(varname="soa", listname="chem_param", paramname="frac_pms")

@pytest.mark.xfail(raises=TypeError)
def test_get_subparam_value_bad_var_name(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    test_table.get_subparam_value(varname="sob", listname="chem_param", paramname="frac_pm1")

def test_get_variable_list(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    test_list = test_table.get_variable_list()
    assert test_list == ["sphum", "soa"]

def test_get_num_variables(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    num_vars = test_table.get_num_variables()
    assert num_vars == 2

def test_get_subparam_list(test_config=test_config):
    test_table = FieldTable.from_dict(test_config)
    test_list = test_table.get_subparam_list(varname="soa")
    assert test_list == ["chem_param", "profile_type"]

def test_set_value(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_value(varname="soa", key="units", value="m")
    assert test_table.varlist[1]["units"] == "m"

def test_set_subparam_value(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_subparam_value(varname="soa", listname="chem_param", subparamname="frac_pm1", value=1)
    assert test_table.varlist[1]["chem_param"][0]["frac_pm1"] == 1

def test_set_var_name(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_var_name(old_name="soa", new_name="soc")
    assert test_table.varlist[1]["variable"] == "soc"

def test_set_var_attr_name(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_var_attr_name(varname="soa", oldname="longname", newname="ln")
    assert test_table.varlist[1]["ln"]

@pytest.mark.xfail(raises=FieldError)
def test_set_var_attr_name_duplicate(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_var_attr_name(varname="soa", oldname="longname", newname="longname")

def test_set_subparam_name(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_subparam_name(varname="soa", listname="chem_param", oldname="frac_pm1", newname="frac_pm2")
    assert test_table.varlist[1]["chem_param"][0]["frac_pm2"]

@pytest.mark.xfail(raises=FieldError)
def test_set_subparam_name_duplicate(test_config=test_config):
    new_config = copy.deepcopy(test_config)
    test_table = FieldTable.from_dict(new_config)
    test_table.set_subparam_name(varname="soa", listname="chem_param", oldname="frac_pm1", newname="frac_pm1")