const express = require('express')
const fstat  = require('fs')
const app = express()
const path = require('path')
const { createWebSocketStream } = require('ws')
const WebSocket = require('ws')
const port = 3000

var imageData

//const server = http.createServer(app)
//const wss = new WebSocket.Server({server})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'))
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

const socketServer = new WebSocket.Server({port: 3030})

socketServer.on('connection', (socketClient) => {
  console.log('connected')
  console.log('client set length: ', socketServer.clients.size)

  socketClient.on('message', function incoming(data) {
    console.log(data)
    imageData = Buffer.from(data, 'binary')
    fstat.writeFile('image.jpg', imageData, {encoding: 'binary'}, function(err) {
      console.log('File created');
    });
    console.log(imageData)
    //console.log("this function is running")
    socketClient.send("response")
  })

  socketClient.on('close', (socketClient) => {
    console.log('closed')
    console.log('number of clients: ', socketServer.clients.size)
  })
})
