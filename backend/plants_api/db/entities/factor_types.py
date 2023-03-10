"""
Table which represent some plant factor are defined here.

Current list is: soil_acidity_types, soil_fertility_types, soil_types, humidity_types, light_types, limitation_factors
"""
from sqlalchemy import Column, Integer, Sequence, String, Table

from plants_api.db import metadata

soil_acidity_types_id_seq = Sequence("soil_acidity_types_id_seq")

soil_acidity_types = Table(
    "soil_acidity_types",
    metadata,
    Column("id", Integer, primary_key=True, server_default=soil_acidity_types_id_seq.next_value()),
    Column("name", String, nullable=False, unique=True),
)

soil_fertility_types_id_seq = Sequence("soil_fertility_types_id_seq")

soil_fertility_types = Table(
    "soil_fertility_types",
    metadata,
    Column("id", Integer, primary_key=True, server_default=soil_fertility_types_id_seq.next_value()),
    Column("name", String, nullable=False, unique=True),
)

soil_types_id_seq = Sequence("soil_types_id_seq")

soil_types = Table(
    "soil_types",
    metadata,
    Column("id", Integer, primary_key=True, server_default=soil_types_id_seq.next_value()),
    Column("name", String, nullable=False, unique=True),
)

humidity_types_id_seq = Sequence("humidity_types_id_seq")

humidity_types = Table(
    "humidity_types",
    metadata,
    Column("id", Integer, primary_key=True, server_default=humidity_types_id_seq.next_value()),
    Column("name", String, nullable=False, unique=True),
)

light_types_id_seq = Sequence("light_types_id_seq")

light_types = Table(
    "light_types",
    metadata,
    Column("id", Integer, primary_key=True, server_default=light_types_id_seq.next_value()),
    Column("name", String, nullable=False, unique=True),
)

limitation_factors_id_seq = Sequence("limitation_factors_id_seq")

limitation_factors = Table(
    "limitation_factors",
    metadata,
    Column("id", Integer, primary_key=True, server_default=limitation_factors_id_seq.next_value()),
    Column("name", String, nullable=False, unique=True),
    Column("explanation", String, nullable=False),
)
