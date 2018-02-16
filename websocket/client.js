var connection = new WebSocket("ws://127.0.0.1:12345");

connection.onopen = function()
{
	console.log("open");
};

connection.onerror = function(error)
{
	console.log("error");
};

connection.onmessage = function(e)
{
	document.getElementById("talk_box").innerHTML+=e.data+"<br>"
};
function send_message()
{
	var message = document.getElementById("msg_box").value;
	connection.send(message);

}
