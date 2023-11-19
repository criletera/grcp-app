from __future__ import print_function
from fastapi import FastAPI

import grpc
import users_pb2
import users_pb2_grpc

from google.protobuf.json_format import MessageToDict

app = FastAPI()

@app.get("/")
async def healthcheck():
    return {"status": "OK"}

@app.get("/message")
async def getMessage():
    print("Sending request to GRPC server")
    with grpc.insecure_channel("grpc-server-service:50051") as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        request = users_pb2.GetUsersResponse()
        response = stub.GetUsers(request)
    print("Message received from GRPC server:")
    print(str(response.user))
    return str(response.user)



