"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class HashPolicy(google.protobuf.message.Message):
    """[#protodoc-title: Hash Policy]

    Specifies the hash policy
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class SourceIp(google.protobuf.message.Message):
        """The source IP will be used to compute the hash used by hash-based load balancing
        algorithms.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    SOURCE_IP_FIELD_NUMBER: builtins.int
    @property
    def source_ip(self) -> global___HashPolicy.SourceIp: ...
    def __init__(self,
        *,
        source_ip : typing.Optional[global___HashPolicy.SourceIp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"policy_specifier",b"policy_specifier",u"source_ip",b"source_ip"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"policy_specifier",b"policy_specifier",u"source_ip",b"source_ip"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"policy_specifier",b"policy_specifier"]) -> typing.Optional[typing_extensions.Literal["source_ip"]]: ...
global___HashPolicy = HashPolicy
