# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faiss.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='faiss.proto',
  package='faiss',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x66\x61iss.proto\x12\x05\x66\x61iss\x1a\x1bgoogle/protobuf/empty.proto\"#\n\x06\x45ntity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t\"+\n\x08\x45ntities\x12\x1f\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\r.faiss.Entity\"F\n\x08Neighbor\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x1f\n\x08\x65ntities\x18\x03 \x03(\x0b\x32\r.faiss.Entity\"6\n\x10MultipleNeighbor\x12\"\n\tneighbors\x18\x01 \x03(\x0b\x32\x0f.faiss.Neighbor\"\x15\n\x06Vector\x12\x0b\n\x03val\x18\x01 \x03(\x02\"N\n\rSearchRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12\x1e\n\x07queries\x18\x02 \x03(\x0b\x32\r.faiss.Vector\x12\t\n\x01k\x18\x03 \x01(\x04\"B\n\x0eSearchResponse\x12\x30\n\x0fmulti_neighbors\x18\x01 \x03(\x0b\x32\x17.faiss.MultipleNeighbor\"*\n\x11SearchByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\t\n\x01k\x18\x02 \x01(\x04\"L\n\x12SearchByIdResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\x04\x12\"\n\tneighbors\x18\x02 \x03(\x0b\x32\x0f.faiss.Neighbor\"!\n\x0eSimpleResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"y\n\rInsertRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12\x1e\n\x07vectors\x18\x02 \x03(\x0b\x32\r.faiss.Vector\x12\x0b\n\x03ids\x18\x03 \x03(\x02\x12\'\n\x0emulti_entities\x18\x04 \x03(\x0b\x32\x0f.faiss.Entities\"-\n\x0eInsertResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x03(\x04\"0\n\rRemoveRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\x04\".\n\x0eRemoveResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\x04\"5\n\rCreateRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x0b\n\x03\x64im\x18\x02 \x01(\x04\x32\xf2\x02\n\x0c\x46\x61issService\x12\x39\n\x08Heatbeat\x12\x16.google.protobuf.Empty\x1a\x15.faiss.SimpleResponse\x12\x35\n\x06Search\x12\x14.faiss.SearchRequest\x1a\x15.faiss.SearchResponse\x12\x41\n\nSearchById\x12\x18.faiss.SearchByIdRequest\x1a\x19.faiss.SearchByIdResponse\x12\x35\n\x06Insert\x12\x14.faiss.InsertRequest\x1a\x15.faiss.InsertResponse\x12\x35\n\x06Remove\x12\x14.faiss.RemoveRequest\x1a\x15.faiss.RemoveResponse\x12?\n\x10\x43reateCollection\x12\x14.faiss.CreateRequest\x1a\x15.faiss.SimpleResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='faiss.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='faiss.Entity.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='val', full_name='faiss.Entity.val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=86,
)


_ENTITIES = _descriptor.Descriptor(
  name='Entities',
  full_name='faiss.Entities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='faiss.Entities.entities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=131,
)


_NEIGHBOR = _descriptor.Descriptor(
  name='Neighbor',
  full_name='faiss.Neighbor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='faiss.Neighbor.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='faiss.Neighbor.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='faiss.Neighbor.entities', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=203,
)


_MULTIPLENEIGHBOR = _descriptor.Descriptor(
  name='MultipleNeighbor',
  full_name='faiss.MultipleNeighbor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='neighbors', full_name='faiss.MultipleNeighbor.neighbors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=259,
)


_VECTOR = _descriptor.Descriptor(
  name='Vector',
  full_name='faiss.Vector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='faiss.Vector.val', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=282,
)


_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='faiss.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='faiss.SearchRequest.collection', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queries', full_name='faiss.SearchRequest.queries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k', full_name='faiss.SearchRequest.k', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=362,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='faiss.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='multi_neighbors', full_name='faiss.SearchResponse.multi_neighbors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=364,
  serialized_end=430,
)


_SEARCHBYIDREQUEST = _descriptor.Descriptor(
  name='SearchByIdRequest',
  full_name='faiss.SearchByIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='faiss.SearchByIdRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k', full_name='faiss.SearchByIdRequest.k', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=474,
)


_SEARCHBYIDRESPONSE = _descriptor.Descriptor(
  name='SearchByIdResponse',
  full_name='faiss.SearchByIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='faiss.SearchByIdResponse.request_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='neighbors', full_name='faiss.SearchByIdResponse.neighbors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=552,
)


_SIMPLERESPONSE = _descriptor.Descriptor(
  name='SimpleResponse',
  full_name='faiss.SimpleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='faiss.SimpleResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=587,
)


_INSERTREQUEST = _descriptor.Descriptor(
  name='InsertRequest',
  full_name='faiss.InsertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='faiss.InsertRequest.collection', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vectors', full_name='faiss.InsertRequest.vectors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='faiss.InsertRequest.ids', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi_entities', full_name='faiss.InsertRequest.multi_entities', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=710,
)


_INSERTRESPONSE = _descriptor.Descriptor(
  name='InsertResponse',
  full_name='faiss.InsertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='faiss.InsertResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='faiss.InsertResponse.id', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=757,
)


_REMOVEREQUEST = _descriptor.Descriptor(
  name='RemoveRequest',
  full_name='faiss.RemoveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='faiss.RemoveRequest.collection', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='faiss.RemoveRequest.ids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=759,
  serialized_end=807,
)


_REMOVERESPONSE = _descriptor.Descriptor(
  name='RemoveResponse',
  full_name='faiss.RemoveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='faiss.RemoveResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='faiss.RemoveResponse.ids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=855,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='faiss.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection_name', full_name='faiss.CreateRequest.collection_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dim', full_name='faiss.CreateRequest.dim', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=857,
  serialized_end=910,
)

_ENTITIES.fields_by_name['entities'].message_type = _ENTITY
_NEIGHBOR.fields_by_name['entities'].message_type = _ENTITY
_MULTIPLENEIGHBOR.fields_by_name['neighbors'].message_type = _NEIGHBOR
_SEARCHREQUEST.fields_by_name['queries'].message_type = _VECTOR
_SEARCHRESPONSE.fields_by_name['multi_neighbors'].message_type = _MULTIPLENEIGHBOR
_SEARCHBYIDRESPONSE.fields_by_name['neighbors'].message_type = _NEIGHBOR
_INSERTREQUEST.fields_by_name['vectors'].message_type = _VECTOR
_INSERTREQUEST.fields_by_name['multi_entities'].message_type = _ENTITIES
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Entities'] = _ENTITIES
DESCRIPTOR.message_types_by_name['Neighbor'] = _NEIGHBOR
DESCRIPTOR.message_types_by_name['MultipleNeighbor'] = _MULTIPLENEIGHBOR
DESCRIPTOR.message_types_by_name['Vector'] = _VECTOR
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['SearchByIdRequest'] = _SEARCHBYIDREQUEST
DESCRIPTOR.message_types_by_name['SearchByIdResponse'] = _SEARCHBYIDRESPONSE
DESCRIPTOR.message_types_by_name['SimpleResponse'] = _SIMPLERESPONSE
DESCRIPTOR.message_types_by_name['InsertRequest'] = _INSERTREQUEST
DESCRIPTOR.message_types_by_name['InsertResponse'] = _INSERTRESPONSE
DESCRIPTOR.message_types_by_name['RemoveRequest'] = _REMOVEREQUEST
DESCRIPTOR.message_types_by_name['RemoveResponse'] = _REMOVERESPONSE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.Entity)
  })
_sym_db.RegisterMessage(Entity)

Entities = _reflection.GeneratedProtocolMessageType('Entities', (_message.Message,), {
  'DESCRIPTOR' : _ENTITIES,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.Entities)
  })
_sym_db.RegisterMessage(Entities)

Neighbor = _reflection.GeneratedProtocolMessageType('Neighbor', (_message.Message,), {
  'DESCRIPTOR' : _NEIGHBOR,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.Neighbor)
  })
_sym_db.RegisterMessage(Neighbor)

MultipleNeighbor = _reflection.GeneratedProtocolMessageType('MultipleNeighbor', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLENEIGHBOR,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.MultipleNeighbor)
  })
_sym_db.RegisterMessage(MultipleNeighbor)

Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.Vector)
  })
_sym_db.RegisterMessage(Vector)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)

SearchByIdRequest = _reflection.GeneratedProtocolMessageType('SearchByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHBYIDREQUEST,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.SearchByIdRequest)
  })
_sym_db.RegisterMessage(SearchByIdRequest)

SearchByIdResponse = _reflection.GeneratedProtocolMessageType('SearchByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHBYIDRESPONSE,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.SearchByIdResponse)
  })
_sym_db.RegisterMessage(SearchByIdResponse)

SimpleResponse = _reflection.GeneratedProtocolMessageType('SimpleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESPONSE,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.SimpleResponse)
  })
_sym_db.RegisterMessage(SimpleResponse)

InsertRequest = _reflection.GeneratedProtocolMessageType('InsertRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSERTREQUEST,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.InsertRequest)
  })
_sym_db.RegisterMessage(InsertRequest)

InsertResponse = _reflection.GeneratedProtocolMessageType('InsertResponse', (_message.Message,), {
  'DESCRIPTOR' : _INSERTRESPONSE,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.InsertResponse)
  })
_sym_db.RegisterMessage(InsertResponse)

RemoveRequest = _reflection.GeneratedProtocolMessageType('RemoveRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEREQUEST,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.RemoveRequest)
  })
_sym_db.RegisterMessage(RemoveRequest)

RemoveResponse = _reflection.GeneratedProtocolMessageType('RemoveResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVERESPONSE,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.RemoveResponse)
  })
_sym_db.RegisterMessage(RemoveResponse)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'faiss_pb2'
  # @@protoc_insertion_point(class_scope:faiss.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)



_FAISSSERVICE = _descriptor.ServiceDescriptor(
  name='FaissService',
  full_name='faiss.FaissService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=913,
  serialized_end=1283,
  methods=[
  _descriptor.MethodDescriptor(
    name='Heatbeat',
    full_name='faiss.FaissService.Heatbeat',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SIMPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='faiss.FaissService.Search',
    index=1,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchById',
    full_name='faiss.FaissService.SearchById',
    index=2,
    containing_service=None,
    input_type=_SEARCHBYIDREQUEST,
    output_type=_SEARCHBYIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='faiss.FaissService.Insert',
    index=3,
    containing_service=None,
    input_type=_INSERTREQUEST,
    output_type=_INSERTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='faiss.FaissService.Remove',
    index=4,
    containing_service=None,
    input_type=_REMOVEREQUEST,
    output_type=_REMOVERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateCollection',
    full_name='faiss.FaissService.CreateCollection',
    index=5,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_SIMPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FAISSSERVICE)

DESCRIPTOR.services_by_name['FaissService'] = _FAISSSERVICE

# @@protoc_insertion_point(module_scope)