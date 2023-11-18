from __future__ import print_function

import grpc
import users_pb2
import users_pb2_grpc

import time


def run():
    while True:
        with grpc.insecure_channel("server:50051") as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.GetUsersResponse()
            response = stub.GetUsers(request)
        print("GRPC received:\n", response.user)
        time.sleep(5)


if __name__ == "__main__":
    run()
