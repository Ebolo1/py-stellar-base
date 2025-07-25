# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
from __future__ import annotations

import base64
from enum import IntEnum

from xdrlib3 import Packer, Unpacker

__all__ = ["SCSpecEventParamLocationV0"]


class SCSpecEventParamLocationV0(IntEnum):
    """
    XDR Source Code::

        enum SCSpecEventParamLocationV0
        {
            SC_SPEC_EVENT_PARAM_LOCATION_DATA = 0,
            SC_SPEC_EVENT_PARAM_LOCATION_TOPIC_LIST = 1
        };
    """

    SC_SPEC_EVENT_PARAM_LOCATION_DATA = 0
    SC_SPEC_EVENT_PARAM_LOCATION_TOPIC_LIST = 1

    def pack(self, packer: Packer) -> None:
        packer.pack_int(self.value)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> SCSpecEventParamLocationV0:
        value = unpacker.unpack_int()
        return cls(value)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> SCSpecEventParamLocationV0:
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> SCSpecEventParamLocationV0:
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)
