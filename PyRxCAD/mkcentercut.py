from typing import Any
from lib import *

#######################
class enumCenterCutType(Enum): # this enum is for tunnel face type of center cut, member of Tunnel class
    Parallel = "Parallel"
    Wedge = "Wedge"

    @classmethod
    def is_CenterCut(cls, centerCutType):
        if isinstance(centerCutType, cls):
            centerCutType = centerCutType.value
        if not centerCutType in cls.__members__:
            return False
        else:
            return True

class CenterCutTypeDict(dict): # dictionary of center cut enum types and their string literals
    def __setitem__(self, __key: Any, __value: Any) -> None:
        if enumCenterCutType.is_CenterCut(__key):
            super().__setitem__(enumCenterCutType(__key), __value)
        else:
            raise KeyError(f"setter::Invalid center cut type: {__key}")

    def __getitem__(self, __key: Any) -> Any:
        if isinstance(__key, Any):
            __key = enumCenterCutType(__key.upper())
        return super().__getitem__(__key)

#######################
    
class MkBaseCenterCut():
    def __init__(self) -> None:
        pass

    