from __future__ import print_function

import logging

import grpc
import multhetizer_pb2
import multhetizer_pb2_grpc

def run():
    print('abrindo o multhetizer gRPC...')
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = multhetizer_pb2_grpc.PlayStub(channel)
        response = stub.SendNote(multhetizer_pb2.Note(pitch="C4"))

if __name__ == "__main__":
    logging.basicConfig()
    run()