# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gen_pb2 as gen__pb2

GRPC_GENERATED_VERSION = '1.73.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gen_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TextGeneratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/TextGenerator/Generate',
                request_serializer=gen__pb2.TextRequest.SerializeToString,
                response_deserializer=gen__pb2.TextResponse.FromString,
                _registered_method=True)


class TextGeneratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextGeneratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=gen__pb2.TextRequest.FromString,
                    response_serializer=gen__pb2.TextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextGenerator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TextGenerator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TextGenerator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TextGenerator/Generate',
            gen__pb2.TextRequest.SerializeToString,
            gen__pb2.TextResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ImageGeneratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/ImageGenerator/Generate',
                request_serializer=gen__pb2.TextRequest.SerializeToString,
                response_deserializer=gen__pb2.ImageResponse.FromString,
                _registered_method=True)


class ImageGeneratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageGeneratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=gen__pb2.TextRequest.FromString,
                    response_serializer=gen__pb2.ImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageGenerator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ImageGenerator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ImageGenerator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ImageGenerator/Generate',
            gen__pb2.TextRequest.SerializeToString,
            gen__pb2.ImageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
