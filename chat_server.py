from websocket_server import WebsocketServer
 
# Callback functions
 
def new_client(client, server):
	pass

def client_left(client, server):
	pass
 
def message_received(client, server, message):
	print(message)
	server.send_message_to_all(message)
 
# Main
if __name__ == "__main__":
	server = WebsocketServer(port=12345, host='172.28.32.133', )
	server.set_fn_new_client(new_client)
	server.set_fn_client_left(client_left)
	server.set_fn_message_received(message_received)
	server.run_forever()
