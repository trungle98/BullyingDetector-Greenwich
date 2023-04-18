import logging
from concurrent import futures
 
import grpc
 
# import settings
from BullytingDetector import Detector
from CommentDetector_pb2_grpc import add_BullyingDetectionServiceServicer_to_server
 
 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BullyingDetectionServiceServicer_to_server(Detector(), server)
    server.add_insecure_port('localhost:9091')
    server.start()
    server.wait_for_termination()
 
 
if __name__ == '__main__':
    logging.basicConfig()
    serve()