# How to run

Install deps:

    pip install -r requirements.txt

If you want to edit the service, with this command you generate stubs (be sure to be in /python):

    python3 -m grpc_tools.protoc --proto_path=../protos --python_out=. --grpc_python_out=. ../protos/multhetizer.proto