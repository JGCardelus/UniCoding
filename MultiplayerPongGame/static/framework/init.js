const DEBUG = true;

//CONNECT TO SERVER
let socket = null;
function connectServer()
{
  socket = io.connect('http://192.168.2.62:5050');
  socket.on('connect', function()
  {
      socket.emit('connection', 'New connection');
  })
}

function startEnvironment()
{
  if(!DEBUG)
  {
    connectServer();
  }
  //scrollBottom();
}

startEnvironment();