# generated by datamodel-codegen:
#   filename:  transfer.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class Transfer(BaseModel):
    class Config:
        extra = Extra.forbid

    to: str
    value: int