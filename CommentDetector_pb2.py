# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommentDetector.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x43ommentDetector.proto\x12\'com.edu.greenwich.managementsystem.grpc\"\x1d\n\nMsgRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0bMsgResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\x96\x01\n\x18\x42ullyingDetectionService\x12z\n\rdetectComment\x12\x33.com.edu.greenwich.managementsystem.grpc.MsgRequest\x1a\x34.com.edu.greenwich.managementsystem.grpc.MsgResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CommentDetector_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MSGREQUEST._serialized_start=66
  _MSGREQUEST._serialized_end=95
  _MSGRESPONSE._serialized_start=97
  _MSGRESPONSE._serialized_end=128
  _BULLYINGDETECTIONSERVICE._serialized_start=131
  _BULLYINGDETECTIONSERVICE._serialized_end=281
# @@protoc_insertion_point(module_scope)
