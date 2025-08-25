## Como rodar

Gerar os stubs:

    python3 -m grpc_tools.protoc --proto_path=../protos --python_out=. --grpc_python_out=. ../protos/multhetizer.proto