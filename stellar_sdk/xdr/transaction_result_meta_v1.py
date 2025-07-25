# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
from __future__ import annotations

import base64

from xdrlib3 import Packer, Unpacker

from .extension_point import ExtensionPoint
from .ledger_entry_changes import LedgerEntryChanges
from .transaction_meta import TransactionMeta
from .transaction_result_pair import TransactionResultPair

__all__ = ["TransactionResultMetaV1"]


class TransactionResultMetaV1:
    """
    XDR Source Code::

        struct TransactionResultMetaV1
        {
            ExtensionPoint ext;

            TransactionResultPair result;
            LedgerEntryChanges feeProcessing;
            TransactionMeta txApplyProcessing;

            LedgerEntryChanges postTxApplyFeeProcessing;
        };
    """

    def __init__(
        self,
        ext: ExtensionPoint,
        result: TransactionResultPair,
        fee_processing: LedgerEntryChanges,
        tx_apply_processing: TransactionMeta,
        post_tx_apply_fee_processing: LedgerEntryChanges,
    ) -> None:
        self.ext = ext
        self.result = result
        self.fee_processing = fee_processing
        self.tx_apply_processing = tx_apply_processing
        self.post_tx_apply_fee_processing = post_tx_apply_fee_processing

    def pack(self, packer: Packer) -> None:
        self.ext.pack(packer)
        self.result.pack(packer)
        self.fee_processing.pack(packer)
        self.tx_apply_processing.pack(packer)
        self.post_tx_apply_fee_processing.pack(packer)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> TransactionResultMetaV1:
        ext = ExtensionPoint.unpack(unpacker)
        result = TransactionResultPair.unpack(unpacker)
        fee_processing = LedgerEntryChanges.unpack(unpacker)
        tx_apply_processing = TransactionMeta.unpack(unpacker)
        post_tx_apply_fee_processing = LedgerEntryChanges.unpack(unpacker)
        return cls(
            ext=ext,
            result=result,
            fee_processing=fee_processing,
            tx_apply_processing=tx_apply_processing,
            post_tx_apply_fee_processing=post_tx_apply_fee_processing,
        )

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> TransactionResultMetaV1:
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> TransactionResultMetaV1:
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    def __hash__(self):
        return hash(
            (
                self.ext,
                self.result,
                self.fee_processing,
                self.tx_apply_processing,
                self.post_tx_apply_fee_processing,
            )
        )

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            self.ext == other.ext
            and self.result == other.result
            and self.fee_processing == other.fee_processing
            and self.tx_apply_processing == other.tx_apply_processing
            and self.post_tx_apply_fee_processing == other.post_tx_apply_fee_processing
        )

    def __repr__(self):
        out = [
            f"ext={self.ext}",
            f"result={self.result}",
            f"fee_processing={self.fee_processing}",
            f"tx_apply_processing={self.tx_apply_processing}",
            f"post_tx_apply_fee_processing={self.post_tx_apply_fee_processing}",
        ]
        return f"<TransactionResultMetaV1 [{', '.join(out)}]>"
