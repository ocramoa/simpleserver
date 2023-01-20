import socketserver
import datetime

class maintain():

    def __init__(self):
        self._history = {}
        self._passwords = ["1111","kaedon","bagelforever","password","brick"]
        self._url = "To download this server code, run 'git clone 'https://github.com/ocramoa/simpleserver'"

    def update_history(self, client, password_and_time):
        self._history.update({client:password_and_time})

class conductor(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        maintainer = maintain()
        self.data = self.request.recv(1024).strip()
        decoded = self.data.decode("utf-8")
        print(f"{self.client_address[0]} wrote:")
        print(decoded)
        print(f"at {datetime.datetime.now()}")
        maintainer.update_history(self.client_address[0],decoded)
        print(maintainer._history)
        if decoded in maintainer._passwords:
        # just send back the same data, but upper-cased
            self.request.sendall(bytes(f"{maintainer._url}", "utf-8"))
        else:
            self.request.sendall(bytes("There was an error.", "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "192.168.0.245", 5007

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), conductor) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()