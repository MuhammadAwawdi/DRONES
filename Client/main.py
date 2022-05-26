import socket
import sys
from djitellopy import Tello
from time import sleep


def myFunc(str):
    if str == "UP":
        drone.send_rc_control(0, 0, 60, 0)  # self.drone.move_up(40)
    if str == "DOWN":
        drone.send_rc_control(0, 0, -40, 0)  # self.drone.move_down(40)
    if str == "RIGHT":
        drone.send_rc_control(-40, 0, 0, 0)  # self.drone.move_right(40)
    if str == "LEFT":
        drone.send_rc_control(40, 0, 0, 0)  # self.drone.move_left(40)
    if str == "FORWARD":
        drone.send_rc_control(0, -40, 0, 0)  # self.drone.move_forward(40)
    if str == "BACKWARD":
        drone.send_rc_control(0, 40, 0, 0)  # self.drone.move_backward(40)
    if str == "TAKEOFF":
        drone.takeoff()  # takeoff command
    if str == "LAND":
        drone.land()  # land command
    if str == "CLOCKWISE":
        drone.send_rc_control(0, 0, 0, 60)  # self.drone.rotate_clockwise(60)
    if str == "COUNTER_CLOCKWISE":
        drone.send_rc_control(0, 0, 0, -60)  # self.drone.rotate_counter_clockwise(60)
    sleep(0.5)
    drone.send_rc_control(0, 0, 0, 0)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('DESKTOP-P0S5QFN', 4000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
print('connected')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    drone = Tello()
    drone.connect()
    print(drone.get_battery())
    try:
        # Send data
        message = 'TAKEOFF'
        print(sys.stderr, 'sending ' + message)
        sock.sendall(bytearray(message, 'utf-8'))

        # Look for the response
        amount_received = 0
        amount_expected = 500

        while amount_received < amount_expected:
            data = sock.recv(16)
            sock.sendall(bytearray(message, 'utf-8'))
            amount_received += 1
            print(sys.stderr, 'received "%s"' % data)
            print(data.decode("utf-8"))
            myFunc(data.decode("utf-8"))

    finally:
        print(sys.stderr, 'closing socket')
        sock.close()
