const http = require('http');

http.createServer(function(request, response){
  let writeHeadObject = {
    'Content-Type': 'text/html'
  }

  response.writeHead(200, writeHeadObject)
  response.end("byebye");


}).listen(8080);
