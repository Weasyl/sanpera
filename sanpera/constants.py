from enum import IntEnum

from sanpera._api import ffi


_ChannelType = ffi.typeof('ChannelType').relements

class Channel(IntEnum):
    red = _ChannelType['RedChannel']
    blue = _ChannelType['BlueChannel']
    green = _ChannelType['GreenChannel']
