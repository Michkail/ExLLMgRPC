import sys
import os
import grpc
import gen_pb2 as pb2
import gen_pb2_grpc as pb2_grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
from model.gen_text import generate_text
from model.gen_image import generate_image_base64

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "proto"))

class TextGenService(pb2_grpc.TextGeneratorServicer):
    def Generate(self, request, context):
        result = generate_text(request.prompt, request.max_length)

        return pb2.TextResponse(result=result)


class ImageGenService(pb2_grpc.ImageGeneratorServicer):
    def Generate(self, request, context):
        base64_img = generate_image_base64(request.prompt)

        return pb2.ImageResponse(image_base64=base64_img)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    pb2_grpc.add_TextGeneratorServicer_to_server(TextGenService(), server)
    pb2_grpc.add_ImageGeneratorServicer_to_server(ImageGenService(), server)

    SERVICE_NAMES = (pb2.DESCRIPTOR.services_by_name['TextGenerator'].full_name,
                     pb2.DESCRIPTOR.services_by_name['ImageGenerator'].full_name,
                     reflection.SERVICE_NAME)
    
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC GenAI Server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
