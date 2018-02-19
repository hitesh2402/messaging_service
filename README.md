#### messaging_service

## INTRODUCTION
Messaging service is simple instant text messaging service written in python. It works on simple client server model, client can
send messages to other client which goes through a server sitting in middle. Server takes the responsibility to keep track of the
message till it is delivered.

## Features
1) Client can send message to single user.
2) Client can same message to multiple users.
3) If destination client is not online messages are delivered once he comes online.
4) Group chat

## Usage
1) Initiate the server giving port number as command line argument.
   ./server.py 6666
   
2) Execute ./client.py $SERVER_ADDRESS $SERVER_PORT
3) Server askes to ener your name
   Name entered by client is used as identifier by the client
4) ** Sending message ** to single user for eg Alice is sending a message to Bob. Message is seperated from recipient using colon(":")
  Bob:It is a message from Alice
  
5)  ** Sending message to multiple ** receipients
  Bob,Charlie: Message sent to multiple users.
