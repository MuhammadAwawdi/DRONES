# Graphics’ Lab  Report:
***Student1: Muhammad Awawdi ID:209319003	
Student2: Morsy Biadsy ID:318241221***
#### Introduction:
### Swarm Programming:
The Company who developed Tello is “Ryze Tech”, has several models of drones, such as Tello, Tello EDU's, Tello IronMan.
The Basic tello model is the only one that doesn't support *swarm. which was the model that we had during this project. 

 We created a solution to overcome the problem of drone swarm for the basic tello model using the Client-Server model.
 We used 3 PCs and 2 WLan adapters that were used so each PC can support 2 Wi-Fi connections.
 1 PC was used as a server and the other 2 were used as client PCs.
 the client PCs were connected to the same Wi-Fi. and each one of them had a second connection to a drone.

The language that was used in this project, for both of the client and the server is Python, as Python had DJI library that covers all aspects of controlling the drone.

*swarm: manipulating the movement of several drones simultaneously.


***Project Characterization:*** 
The server opens a connection and waits for the clients to connect, they open a communication network between them, which is a socket.
Then, each client connects with a drone and communicates with it.
Now, they're ready to recieve commands from the user.

Server can recieve commands from several inputs, the inputs that were used in this project were: 
1)GUI 
2)Keyboard
3)DS4 Controller
The system is based on multi-threading, so it supports using the three inputs at the same time, as we used a thread for each input

1)GUI:
We built a basic GUI that has buttons for each command that can be applied on the drone.
We built it using the Tkinter library.


![GUI](https://github.com/MorsyB/DRONES/blob/main/GUI.jpg)




2)Keyboard:
Sending commands to the clients using the keyboard buttons, then the clients communicates with the drone and activiates a command based on the button that is pressed.

When a particular button is pressed we send a specific message to each client that is connected with the server.
each button corresponds with a different message, therefore, it corresponds to a different command.

![Keyboard](https://github.com/MorsyB/DRONES/blob/main/key.jpeg)




3)DS4 Controller:
Sending commands to the drone based on what's pressed on the DS4 Controller.
created an enhanced movement as the drones feels so smooth when it's recieving commands from the DS4 Controller.


The connection between the DS4 Controller and the drone was created with the usage of PyGame library.

![DS4 Controller](https://github.com/MorsyB/DRONES/blob/main/ps4.jpeg)




***Video Stream***
When activated, each drone opens a video stream and starts recording, each one of the inputs had a button to open/close the stream.
The idea of the video stream was a basic plan for the Drones-VR.

![Stream](https://github.com/MorsyB/DRONES/blob/main/Video.jpeg)




***Client-Drone connection:***
Inorder to communicate between the client and the server, there must be a Wi-Fi connection.
several clients require that all clients are connected to the same Wi-Fi.
The connection between the client and the drone also uses Wi-Fi, so using Wi-Fi adapters is necessary.
Each client had a WLan adapter inorder to obtain 2 connection.
Wi-Fi 1: Communicates with the server.
Wi-Fi 2: Communicates with the drone.

![WLAN](https://github.com/MorsyB/DRONES/blob/main/tpLink.jpeg)




***Code Activation***
1.Run the main.py in the drones file (The server).
2.Run the main.py in the Client file (The Client).
Note: Client must be connected to the drones as explained above.


***Additional images:***




![2drones](https://github.com/MorsyB/DRONES/blob/main/2%20drones.jpeg)
![dr](https://github.com/MorsyB/DRONES/blob/main/dr.jpeg)
![drones](https://github.com/MorsyB/DRONES/blob/main/drones.jpeg)
![drones69](https://github.com/MorsyB/DRONES/blob/main/drones69.jpeg)
![indoor](https://github.com/MorsyB/DRONES/blob/main/indoor.jpeg)



*****
