# generated by DipDup 8.0.0

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class MintParameter(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    to: str
    value: str
