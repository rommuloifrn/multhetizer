import logging
from concurrent import futures
import grpc
import multhetizer_pb2, multhetizer_pb2_grpc

class Play(multhetizer_pb2_grpc.PlayServicer):
    def SendNote(self, request, context):
        print(request.pitch)
        return multhetizer_pb2.Confirmation(message="nota %s recebida com sucesso" % request.pitch)
    
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    multhetizer_pb2_grpc.add_PlayServicer_to_server(Play(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()