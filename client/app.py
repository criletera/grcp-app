from __future__ import print_function

import grpc
import users_pb2
import users_pb2_grpc

import time


def run():
    print("GRPC Client started")
    while True:
        print("GRPC Client waiting 10 second")
        time.sleep(10)
        print("GRPC Client sending request to server")
        with grpc.insecure_channel("grpc-server-service:50051") as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.GetUsersResponse()
            response = stub.GetUsers(request)
        print("GRPC Client message received:\n", response.user)


if __name__ == "__main__":
    run()
