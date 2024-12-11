import os
import yaml
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


@pytest.fixture(scope="session")
def temp_file(tmpdir_factory):
    file_path = tmpdir_factory.mktemp("data").join("test_fm.yaml")
    with open(file_path, 'w') as f:
        yaml.dump(test_config, f)
    yield file_path
    os.remove(file_path)

def test_fieldtable_init(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    assert isinstance(test_table, FieldTable)

def test_get_fieldtype(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    fieldtype = test_table.field_type
    assert fieldtype == 'tracer'

@pytest.mark.xfail(raises=FieldError)
def test_remove_varlist(temp_file):
    with open(temp_file, "r") as f:
        changed_config = yaml.safe_load(f)
    del changed_config["field_table"][0]["modlist"][0]["varlist"]
    FieldTable.from_dict(changed_config)

def test_add_to_varlist(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
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
def test_add_to_varlist_fail(temp_file):
    with open(temp_file, "r") as f:
        changed_config = yaml.safe_load(f)
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

def test_get_var(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    var = test_table.get_var('soa')
    assert var == test_table.modlist[0]["varlist"][1]

@pytest.mark.xfail(raises=FieldError)
def test_get_var_fail(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.get_var('sob')

def test_get_subparam(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    subparameter = test_table.get_subparam(varname="soa", subparam_name="chem_param")
    assert subparameter == test_table.modlist[0]["varlist"][1]["chem_param"]

def test_get_value(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    value = test_table.get_value(varname="soa", key="units")
    assert value == "mmr"

@pytest.mark.xfail(raises=KeyError)
def test_get_value_key_fail(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.get_value(varname="soa", key="unit")

def test_get_subparam_value(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    value = test_table.get_subparam_value(varname="soa", listname="chem_param", paramname="frac_pm1")
    assert value == 0.89

@pytest.mark.xfail(raises=KeyError)
def test_get_subparam_value_bad_key(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.get_subparam_value(varname="soa", listname="chem_param", paramname="frac_pms")

@pytest.mark.xfail(raises=TypeError)
def test_get_subparam_value_bad_var_name(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.get_subparam_value(varname="sob", listname="chem_param", paramname="frac_pm1")

def test_get_variable_list(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_list = test_table.get_variable_list()
    assert test_list == ["sphum", "soa"]

def test_get_num_variables(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    num_vars = test_table.get_num_variables()
    assert num_vars == 2

def test_get_subparam_list(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_list = test_table.get_subparam_list(varname="soa")
    assert test_list == ["chem_param", "profile_type"]

def test_get_num_subparam(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    num = test_table.get_num_subparam(varname="soa")
    assert num == 2

def test_set_value(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_value(varname="soa", key="units", value="m")
    assert test_table.varlist[1]["units"] == "m"

def test_set_subparam_value(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_subparam_value(varname="soa", listname="chem_param", subparamname="frac_pm1", value=1)
    assert test_table.varlist[1]["chem_param"][0]["frac_pm1"] == 1

def test_set_var_name(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_var_name(old_name="soa", new_name="soc")
    assert test_table.varlist[1]["variable"] == "soc"

def test_set_var_attr_name(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_var_attr_name(varname="soa", oldname="longname", newname="ln")
    assert test_table.varlist[1]["ln"]

@pytest.mark.xfail(raises=FieldError)
def test_set_var_attr_name_duplicate(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_var_attr_name(varname="soa", oldname="longname", newname="longname")

def test_set_subparam_name(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_subparam_name(varname="soa", listname="chem_param", oldname="frac_pm1", newname="frac_pm2")
    assert test_table.varlist[1]["chem_param"][0]["frac_pm2"]

@pytest.mark.xfail(raises=FieldError)
def test_set_subparam_name_duplicate(temp_file):
    with open(temp_file, "r") as f:
        config = yaml.safe_load(f)
        test_table = FieldTable.from_dict(config)
    test_table.set_subparam_name(varname="soa", listname="chem_param", oldname="frac_pm1", newname="frac_pm1")
