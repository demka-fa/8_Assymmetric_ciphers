import socket
import pickle
from diffie_hellman import DiffieHellman

HOST = '127.0.0.1'
PORT = 8081

# https://github.com/fa-python-network/8_Assymmetric_ciphers/pull/1/files#diff-9f2b3464f3ecfc62edd0364835343bbc8c3bfcec8c6434bf98ef76bdbc6710aa
def main():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()

    msg = conn.recv(4096)
    #Получаем данные от клиента
    data = pickle.loads(msg)
    p, g, A = data

    #Сгенерированное число b
    a = 884
    diffie_hellman = DiffieHellman(a=A, p=p, g=g)
    server_mixed_key = diffie_hellman.mixed_key
    private_key = diffie_hellman.generate_key(server_mixed_key)

    #TODO: Возврат server_mixed_key клиенту
    print(server_mixed_key)
    print(private_key)




if __name__ == "__main__":
    main()
