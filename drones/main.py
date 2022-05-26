import socket
import sys
import keyboard
from time import sleep
import threading
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = socket.gethostname()
server_address = (server_name, 4000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)


# Press the green button in the gutter to run the script.
def connectClient():
    print(sys.stderr, 'waiting for a connection', threading.current_thread().name)
    connection, client_address = sock.accept()
    connection2, client_address2 = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
        print(sys.stderr, 'connection from', client_address2)

        # Receive the data in small chunks and retransmit it
        while True:
            data = True
            # print(sys.stderr, 'received ' + data.decode())
            if keyboard.is_pressed('w'):
                print("w is pressed")
                message = 'FORWARD'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('a'):
                print("a is pressed")
                message = 'LEFT'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('d'):
                print("d is pressed")
                message = 'RIGHT'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('t'):
                message = 'TAKEOFF'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('b'):
                message = 'LAND'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('s'):
                message = 'BACKWARD'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('q'):
                message = 'UP'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('e'):
                message = 'DOWN'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('c'):
                message = 'CLOCKWISE'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('v'):
                message = 'COUNTER_CLOCKWISE'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('o'):
                message = 'END'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            if keyboard.is_pressed('f'):
                message = 'FLIP'
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            sleep(0.5)
            if data:
                message = ''
                connection.sendall(bytearray(message, 'utf-8'))
                connection2.sendall(bytearray(message, 'utf-8'))

            else:
                print(sys.stderr, 'no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()


if __name__ == '__main__':

    while True:
        # Wait for a connection
        #t1 = threading.Thread(target=connectClient, args=())
        #t1.start()
        connectClient()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
