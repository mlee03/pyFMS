FC=mpif90

FMS_DIR=./FMS

NC_FLAGS=-I/opt/netcdf/4.9.2/GNU/12.4.0/include
NC_LIBS=-L/opt/netcdf/4.9.2/GNU/12.4.0/lib64 -lnetcdff -L/opt/netcdf/4.9.2/GNU/12.4.0/lib64 -lnetcdf -lnetcdf -ldl -lm

FCFLAGS=$(NC_FLAGS) -I$(FMS_DIR)/fortFMS/include -fopenmp
CFLAGS=$(NC_FLAGS) -I$(FMS_DIR)/fortFMS/include -fopenmp
LDFLAGS=$(NC_LIBS) -L/opt/libyaml/0.2.5/GNU/12.4.0/lib

PLATFORM=$(wildcard $(FMS_DIR)/platform/*.o)
MPP=$(wildcard $(FMS_DIR)/mpp/*.o)
TRIDIAGONAL=$(wildcard $(FMS_DIR)/tridiagonal/*.o)
CONSTANTS=$(wildcard $(FMS_DIR)/constants/*.o)
CONSTANTS4=$(wildcard $(FMS_DIR)/constants4/*.o)
MEMUTILS=$(wildcard $(FMS_DIR)/memutils/*.o)
STRING_UTILS=$(wildcard $(FMS_DIR)/string_utils/*.o)
FMS2_IO=$(wildcard $(FMS_DIR)/fms2_io/*.o)
MOSAIC2=$(wildcard $(FMS_DIR)/mosaic2/*.o)
FMS=$(wildcard $(FMS_DIR)/fms/*.o)
PARSER=$(wildcard $(FMS_DIR)/parser/*.o)
AFFINITY=$(wildcard $(FMS_DIR)/affinity/*.o)
MOSAIC=$(wildcard $(FMS_DIR)/mosaic/*.o)
TIME_MANAGER=$(wildcard $(FMS_DIR)/time_manager/*.o)
AXIS_UTILS=$(wildcard $(FMS_DIR)/axis_utils/*.o)
DIAG_MANAGER=$(wildcard $(FMS_DIR)/diag_manager/*.o)
DRIFTERS=$(wildcard $(FMS_DIR)/drifters/*.o)
HORIZ_INTERP=$(wildcard $(FMS_DIR)/horiz_interp/*.o)
TIME_INTERP=$(wildcard $(FMS_DIR)/time_interp/*.o)
COLUMN_DIAGNOSTICS=$(wildcard $(FMS_DIR)/column_diagnostics/*.o)
BLOCK_CONTROL=$(wildcard $(FMS_DIR)/block_control/*.o)
DATA_OVERRIDE=$(wildcard $(FMS_DIR)/data_override/*.o)
ASTRONOMY=$(wildcard $(FMS_DIR)/astronomy/*.o)
FIELD_MANAGER=$(wildcard $(FMS_DIR)/field_manager/*.o)
COUPLER=$(wildcard $(FMS_DIR)/coupler/*.o)
DIAG_INTEGRAL=$(wildcard $(FMS_DIR)/diag_integral/*.o)
MONIN_OBUKHOV=$(wildcard $(FMS_DIR)/monin_obukhov/*.o)
INTERPOLATOR=$(wildcard $(FMS_DIR)/interpolator/*.o)
AMIP_INTERP=$(wildcard $(FMS_DIR)/amip_interp/*.o)
EXCHANGE=$(wildcard $(FMS_DIR)/exchange/*.o)
TOPOGRAPHY=$(wildcard $(FMS_DIR)/topography/*.o)
TRACER_MANAGER=$(wildcard $(FMS_DIR)/tracer_manager/*.o)
SAT_VAPOR_PRES=$(wildcard $(FMS_DIR)/sat_vapor_pres/*.o)
RANDOM_NUMBERS=$(wildcard $(FMS_DIR)/random_numbers/*.o)

ALL=$(PLATFORM) $(MPP) $(TRIDIAGONAL) $(CONSTANTS) $(CONSTANTS4) \
    $(MEMUTILS) $(STRING_UTILS) $(FMS2_IO) $(MOSAIC2) $(FMS) $(PARSER) \
    $(AFFINITY) $(MOSAIC) $(TIME_MANAGER) $(AXIS_UTILS) $(DIAG_MANAGER) \
    $(DRIFTERS) $(HORIZ_INTERP) $(TIME_INTERP) $(COLUIMN_DIAGNOSTICS) \
    $(BLOCK_CONTROL) $(DATA_OVERRIDE) $(ASTRONOMY) $(FIELD_MANAGER) \
    $(COUPLER) $(DIAG_INTEGRAL) $(MONIN_OBUKHOV) $(INTERPOLATOR) \
    $(AMIP_INTERP) $(EXCHANGE) $(TOPOGRAPHY) $(TRACER_MANAGER) \
    $(SAT_VAPOR_PRES) $(RANDOM_NUMBERS)

all : pyFMS_diag_manager.F90 pyFMS_typing.F90 $(ALL)
        $(FC) $(FCFLAGS) -fPIC -c pyFMS_diag_manager.F90 -o pyFMS_diag_manager.o
        $(FC) $(FCFLAGS) -fPIC -c pyFMS_typing.F90 -o pyFMS_typing.o
        $(FC) $(FCFLAGS) $(LDFLAGS) -fPIC -shared $(ALL) pyFMS_diag_manager.o pyFMS_typing.o -o pyfms.so
