import socketserver
import datetime

class maintain():
    """This class deals with the server history file. It also contains the passwords to access the server, the url of the repo, and the available operations.
    
    Maintain can update, get, and delete the server history.
    
    Attributes:
        _history -> Data about the current client's connection to be stored in history.txt.
        _users -> Essentially just a list of valid usernames the client can use.
        _url -> Instructions on how to get the server code.
        _operations -> Instructions on how to interact with the server.
    """

    def __init__(self):
        self._history = {}
        self._users = ["1111","kaedon","bagelforever","password","brick","byui"]
        self._url = "To download this server code, download Git and run 'git clone 'https://github.com/ocramoa/simpleserver'"
        self._operations = "\nOperations: \n To delete history after a certain point, enter 1 after your password followed by an integer. \n To receive server access history, enter 2 after your password. \n To delete all history, enter 3 after your password."

    def update_history(self, client, password_and_time):
        """Updates the server history."""
        self._history.update({client:password_and_time})
        # After updating the _history attribute, opens the file and appends it.
        with open(r"C:\Users\eyeba\web_server\server_script\history.txt", "a") as h:
            h.write(f"{self._history}\n")

    def get_history(self):
        """Gets the server access history."""
        with open(r"C:\Users\eyeba\web_server\server_script\history.txt", "r") as h:
            # Simply reads and returns the contents of the entire file. In a larger project, this would be unwise.
            record = h.read()
        
        return record

    def delete_history(self, n):
        """Deletes the server's history at n. Copied from https://pynative.com/python-delete-lines-from-file, with minor changes."""
        with open(r"C:\Users\eyeba\web_server\server_script\history.txt", "r+", encoding="utf-8") as h:
            
            # read an store all lines into list
            lines = h.readlines()
            # move file pointer to the beginning of a file
            h.seek(0)
            # truncate the file
            h.truncate()

            # start writing lines
            # iterate line and line number
            for number, line in enumerate(lines):
                # delete line number
                if number != (n - 1):
                    h.write(line)

    def delete_all(self, user):
        """Deletes all server access history and replaces it with a deleted notice."""
        with open(r"C:\Users\eyeba\web_server\server_script\history.txt", "w+") as h:
            # Because we open the file in write+ mode, it deletes everything there and writes who deleted it and when.
            h.write(f"delete_all by {user} at {datetime.datetime.now()}\n")

class conductor(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.

    The above is in the default documentation for the base request handler.
    """

    def handle(self):
        # Instantiate the maintain class.
        maintainer = maintain()
        # self.request is the TCP socket connected to the client. 
        self.data = self.request.recv(2048).strip()
        # Decode bytelike data to utf-8.
        decoded = self.data.decode("utf-8")
        # Split whitespace to store the user and their operations into a list.
        user_args = decoded.split()
        print(f"{self.client_address[0]} wrote:")
        print(user_args)
        print(f"at {datetime.datetime.now()}")
        #After printing to terminal, update the history.txt file with request data.
        maintainer.update_history(self.client_address[0],(user_args[0] + " " + str(datetime.datetime.now())))
        print(maintainer._history)
        # If the user is valid, accept their argument if it exists and perform the associated action.
        if user_args[0] in maintainer._users:
            print()
            response = ""
            if len(user_args) > 1:
                if user_args[1] == "1":
                    maintainer.delete_history(int(user_args[2]))
                    maintainer.update_history(f"{user_args[0]}", f"Deleted at: {user_args[2]}")
                    response = f"\nHistory at {user_args[2]} deleted by {user_args[0]}."
                elif user_args[1] == "2":
                    hehe_gottem = maintainer.get_history()
                    response = f"{hehe_gottem}"
                    maintainer.update_history(self.client_address[0],(user_args[0] + " got history at " + str(datetime.datetime.now())))
                elif user_args[1] == "3":
                    maintainer.delete_all(user_args[0])
                    response = "All history deleted."
                else:
                    response = "Either no operation or operation is invalid."
            else:
                pass
            # Send back a response. First is the GitHub url, next the available operations, and finally the result of the operation the user entered. Use sendall instead of send so nothing gets lost.
            self.request.sendall(bytes(f"{maintainer._url}\n{maintainer._operations}\n{response}", "utf-8"))               
        # There was some kind of error (authentication, maybe?)
        else:
            self.request.sendall(bytes("Authentication error.", "utf-8"))

if __name__ == "__main__":
    # Replace this host and port with a different one if you'd like. The host should be the IP address of the machine running the server code.
    HOST, PORT = "192.168.0.245", 5007

    # Create the server, binding to the host and port.
    with socketserver.TCPServer((HOST, PORT), conductor) as server:
        # Activate the server; this will keep running until you interrupt the program with Ctrl-C
        server.serve_forever()