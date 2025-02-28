from typing import Optional
import ctypes


class pyDomainData:
    def __init__(self):
        self._xbegin = None
        self._xend = None
        self._ybegin = None
        self._yend = None
        self._xsize = None
        self._xmax_size = None
        self._ysize = None
        self._ymax_size = None
        self._x_is_global = None
        self._y_is_global = None
        self._tile_count = None

    def xbeginnger(self, val, get):
        if get:
            self.xbegin=val

    def setup_get(
        self, 
        xbegin: Optional[bool]=False,
        xend: Optional[bool]=False,
        ybegin: Optional[bool]=False,
        yend: Optional[bool]=False,
        xsize: Optional[bool]=False,
        xmax_size: Optional[bool]=False,
        ysize: Optional[bool]=False,
        ymax_size: Optional[bool]=False,
        x_is_global: Optional[bool]=False,
        y_is_global: Optional[bool]=False,
        tile_count: Optional[bool]=False,
    ):
        if xbegin:
            self.xbegin = 0
        if xend:
            self.xend = 0
        if ybegin:
            self.ybegin = 0
        if yend:
            self.yend = 0
        if xsize:
            self.xsize = 0
        if xmax_size:
            self.xmax_size = 0
        if ysize:
            self.ysize = 0
        if ymax_size:
            self.ymax_size = 0
        if x_is_global:
            self.x_is_global = True
        if y_is_global:
            self.y_is_global = True
        if tile_count:
            self.tile_count = 0

    
    def setup_set(
        self,
        xbegin: Optional[int]=None,
        xend: Optional[int]=None,
        ybegin: Optional[int]=None,
        yend: Optional[int]=None,
        xsize: Optional[int]=None,
        xmax_size: Optional[int]=None,
        ysize: Optional[int]=None,
        ymax_size: Optional[int]=None,
        x_is_global: Optional[bool]=None,
        y_is_global: Optional[bool]=None,
        tile_count: Optional[int]=None,
    ):
        self.xbegin=xbegin
        self.xend=xend
        self.ybegin=ybegin
        self.yend=yend
        self.xsize=xsize
        self.xmax_size=xmax_size
        self.ysize=ysize
        self.ymax_size=ymax_size
        self.x_is_global=x_is_global
        self.y_is_global=y_is_global
        self.tile_count=tile_count

    @property
    def xbegin(self):
        return self._xbegin

    @xbegin.setter
    def xbegin(self, val):
        if val is None:
            self._xbegin = val
        else:
            self._xbegin = ctypes.c_int(val)

    @property
    def xend(self):
        return self._xend

    @xend.setter
    def xend(self, val: int | None):
        if val is None:
            self._xend = val
        else:
            self._xend = ctypes.c_int(val)

    @property
    def ybegin(self):
        return self._ybegin

    @ybegin.setter
    def ybegin(self, val: int | None):
        if val is None:
            self._ybegin = val
        else:
            self._ybegin = ctypes.c_int(val)

    @property
    def yend(self):
        return self._yend

    @yend.setter
    def yend(self, val: int | None):
        if val is None:
            self._yend = val
        else:
            self._yend = ctypes.c_int(val)

    @property
    def xsize(self):
        return self._xsize

    @xsize.setter
    def xsize(self, val: int | None):
        if val is None:
            self._xsize = val
        else:
            self._xsize = ctypes.c_int(val)

    @property
    def xmax_size(self):
        return self._xmax_size

    @xmax_size.setter
    def xmax_size(self, val: int | None):
        if val is None:
            self._xmax_size = val
        else:
            self._xmax_size = ctypes.c_int(val)

    @property
    def ysize(self):
        return self._ysize

    @ysize.setter
    def ysize(self, val: int | None):
        if val is None:
            self._ysize = val
        else:
            self._ysize = ctypes.c_int(val)

    @property
    def ymax_size(self):
        return self._ymax_size

    @ymax_size.setter
    def ymax_size(self, val: int | None):
        if val is None:
            self._ymax_size = val
        else:
            self._ymax_size = ctypes.c_int(val)

    @property
    def x_is_global(self):
        return self._x_is_global

    @x_is_global.setter
    def x_is_global(self, val: bool | None):
        if val is None:
            self._x_is_global = val
        else:
            self._x_is_global = ctypes.c_bool(val)

    @property
    def y_is_global(self):
        return self._y_is_global

    @y_is_global.setter
    def y_is_global(self, val: bool | None):
        if val is None:
            self._y_is_global = val
        else:
            self._y_is_global = ctypes.c_bool(val)

    @property
    def tile_count(self):
        return self._tile_count

    @tile_count.setter
    def tile_count(self, val: int | None):
        if val is None:
            self._tile_count = val
        else:
            self._tile_count = ctypes.c_int(val)
