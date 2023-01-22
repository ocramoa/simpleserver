# Overview

This is a project for simple server and client scripts.

When run (via entering "python3 server_script/server.py" into the terminal), the server will run forever until it is manually stopped via Ctrl+C. It listens continuously for a request from the client (start by entering python3 client_script/client.py) in the form of a username and one or more numbers.  Upon receiving a request, the server immediately logs the client's request in the history.txt file and prints it to the server terminal. The server always sends back a link to the GitHub repo and a list of operations it can perform, and can also send a response based on what the user decides to do with the history.txt file.

I've always been curious about how networking actually works, so I wrote this software as an experiment and as a way of gaining "hands-on" experience.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

I used client-server architecture. The server receives requests from clients, services them, and sends back data. However, this simple server can only service one request at a time.

This is a TCP server as UDP is not necessary for something this small and slow. I used port 5007, but any other random unused port will do.

Both the client and server communicate with byte-like messages. They convert a string message to byte-like before sending data and do the reverse after receiving data. The client should always use this format -- "user N" or "user 1 N" with "user" being a username and N being a number corresponding to an operation or a file line. You will easily break the program if you type something different.

# Development Environment

I developed this program with Visual Studio Code and the command line on a Windows PC and a Chromebook running Linux.

For the code itself, I used Python 3.11 and the socket, socketserver and datetime libraries.

# Useful Websites

* [Python 3 socket](https://docs.python.org/3.11/library/socket.html)
* [Python 3 socketserver](https://docs.python.org/3/library/socketserver.html)
* [StackOverflow: Difference between modes a, a+, w, w+, and r+ in built-in open function? by flybywire](https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function)
* [Delete Lines from a File in Python](https://pynative.com/python-delete-lines-from-file/)

# Future Work

* This is a simple server, so it shouldn't get too complicated. However, one could use the threading module to enable the server to service multiple clients at once.
* A GUI could make this more accessible and interesting.
* I actually could not figure out how to get the server to sendall multiple times when variables in f-strings were involved. Although I like the way it looks now, if I wanted to spend more time on this I'd dig deeper and find out why.
* It would be nice if the client could do more with the server. Perhaps the server could generate and store a unique username for the client to use in operations.