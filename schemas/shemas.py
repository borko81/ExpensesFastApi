from pydantic import BaseModel, constr
from typing import Optional

from db.models improt Kasa, Obj, Clients, Types


class KasaSchema(BaseModel):
	name: constr(min_length=2, max_length=32)
	is_valid: int


class ObjSchema(BaseModel):
	name: constr(min_length=2, max_length=32)
	is_valid: bool


class  ClientsSchema(BaseModel):
	name = constr(min_length=2, max_length=32)
	is_valid: bool


class TypesSchemas(BaseModel):
	name = constr(min_length=2, max_length=32)
	with_contragent: bool
	is_valid: bool