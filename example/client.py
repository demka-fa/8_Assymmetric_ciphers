import socket
import pickle
from diffie_hellman import DiffieHellman
HOST = '127.0.0.1'
PORT = 8081


def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))

    p = 100
    g = 463
    a = 603 # это можно хранить в txt

    diffie_hellman = DiffieHellman(a=a, p=p, g=g)
    client_mixed_key = diffie_hellman.mixed_key
    private_key = diffie_hellman.generate_key(client_mixed_key)
    print(client_mixed_key)
    print(private_key)

    sock.send(pickle.dumps((p, g, client_mixed_key)))
    B = pickle.loads(sock.recv(4096))
    #Получаем B от сервера
    K = B ** a % p
    print(f"Вычисленный K на клиенте: {K}")

    sock.close()


if __name__ == "__main__":
    main()
