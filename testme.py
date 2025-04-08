import pyfms

cfms_path, cfms = pyfms.cFMS.getlib()
cfms_path_in_do, cfms_in_do = pyfms.pyDataOverride.getlib()

assert(cfms_path == cfms_path_in_do)
assert(id(cfms)==id(cfms_in_do))

pyfms.pyDataOverride.init()
