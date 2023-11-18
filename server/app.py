from concurrent import futures

import grpc
import users_pb2
import users_pb2_grpc

import time

class Users(users_pb2_grpc.UsersServicer):
    def GetUsers(self, request, context):
        
        seconds = time.time()
        date = time.ctime(seconds)
        
        return users_pb2.GetUsersResponse(user=[
            users_pb2.User(
                id='1',
                name='Jonh Doe',
                email='mahes@gmail.com',
                date=date
            )
        ])


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("GRPC Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
