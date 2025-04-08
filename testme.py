import pyfms

cfms_path, cfms = pyfms.cFMS.getlib()
cfms_path_in_do, cfms_in_do = pyfms.pyDataOverride.getlib()

assert(cfms_path == cfms_path_in_do)
assert(id(cfms)==id(cfms_in_do))

fake_path = "None"
pyfms.cFMS.cfms_path = fake_path
assert(pyfms.cFMS.getlib()[0] is not fake_path)

pyfms.pyDataOverride.init()

