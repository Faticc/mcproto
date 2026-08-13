import grpc
from mcproto.mcproto.proto import (
    auth_pb2_grpc,
    client_pb2_grpc,
    update_pb2_grpc
)

SERVER = "launchernew.mcskill.ru:443"

CHANNEL = grpc.secure_channel(SERVER, grpc.ssl_channel_credentials())

AUTH_STUB = auth_pb2_grpc.AuthServiceStub(CHANNEL)
CLIENT_STUB = client_pb2_grpc.ClientServiceStub(CHANNEL)
UPDATE_STUB = update_pb2_grpc.UpdateServiceStub(CHANNEL)
