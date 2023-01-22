import socket

HOST, PORT = "192.168.0.245", 5007
data = input("Enter authentication: ")

# Much of this is from the documentation for socketserver. I have changed only a little bit.
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down. Increased byte size to just over 2KB because the history can get large.
    received = str(sock.recv(2048), "utf-8")

# Print the data sent and received to the terminal.
print("Sent:     {}".format(data))
print("Received: {}".format(received))