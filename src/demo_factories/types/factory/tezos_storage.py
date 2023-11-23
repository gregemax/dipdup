# generated by datamodel-codegen:
#   filename:  tezos_storage.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class Ledger(BaseModel):
    class Config:
        extra = Extra.forbid

    allowances: list[str]
    balance: str
    frozen_balance: str


class TokenList(BaseModel):
    class Config:
        extra = Extra.forbid

    address: str
    nat: str


class Key(BaseModel):
    class Config:
        extra = Extra.forbid

    address: str
    nat: str


class TokenToExchangeItem(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Key
    value: str


class UserRewards(BaseModel):
    class Config:
        extra = Extra.forbid

    reward: str
    reward_paid: str


class Voters(BaseModel):
    class Config:
        extra = Extra.forbid

    candidate: str | None
    last_veto: str
    veto: str
    vote: str


class FactoryStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    baker_validator: str
    counter: str
    dex_lambdas: dict[str, str]
    ledger: dict[str, Ledger]
    metadata: dict[str, str]
    token_lambdas: dict[str, str]
    token_list: dict[str, TokenList]
    token_to_exchange: list[TokenToExchangeItem]
    user_rewards: dict[str, UserRewards]
    vetos: dict[str, str]
    voters: dict[str, Voters]
    votes: dict[str, str]