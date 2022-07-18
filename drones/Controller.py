import pygame
from djitellopy import Tello
import socket
import time


class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""
    drone = Tello()
    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""
        self.drone.connect()
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)
        curr = False
        prev = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value, 2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                # Insert your code on what you would like to happen for each event here!

                if self.button_data[11]:
                    self.drone.send_rc_control(0, 40, 0, 0)
                    curr = True
                    print(self.drone.get_battery())
                    # self.drone.move_forward(40)
                if self.button_data[12]:
                    self.drone.send_rc_control(0, -40, 0, 0)
                    curr = True
                    # self.drone.move_back(40)
                if self.button_data[13]:
                    self.drone.send_rc_control(40, 0, 0, 0)
                    curr = True
                    # self.drone.move_left(40)
                if self.button_data[14]:
                    self.drone.send_rc_control(-40, 0, 0, 0)
                    curr = True
                    # self.drone.move_right(40)
                if self.button_data[3]:
                    self.drone.send_rc_control(0, 0, 40, 0)
                    curr = True
                    # self.drone.move_up(40)
                if self.button_data[0]:
                    self.drone.send_rc_control(0, 0, -40, 0)
                    curr = True
                    # self.drone.move_down(40)
                if self.button_data[9]:
                    self.drone.takeoff()
                if self.button_data[10]:
                    self.drone.land()
                if self.button_data[1]:
                    self.drone.send_rc_control(0, 0, 0, 60)
                    curr = True
                    # self.drone.rotate_clockwise(30)
                if self.button_data[2]:
                    self.drone.send_rc_control(0, 0, 0, -60)
                    curr = True
                    # self.drone.rotate_counter_clockwise(30)
                if not curr and prev:
                    self.drone.send_rc_control(0, 0, 0, 0)
                prev = curr
                curr = False