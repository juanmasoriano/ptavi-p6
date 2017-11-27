#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socketserver
import sys
import os

class EchoHandler(socketserver.DatagramRequestHandler):


    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        Metodos_sip = ['INVITE','BYE','ACK']

            # Leyendo línea a línea lo que nos envía el cliente
        line = self.rfile.read().decode('utf-8')
        line_string = line.split()

        print("El cliente nos manda " + line)

        if line_string[0] == "INVITE":
            self.wfile.write(bytes('SIP/2.0 100 Trying\r\n\r\n'
                                   'Sip/2.0 180 Ringing\r\n\r\n'
                                   'SIP/2.0 200 OK\r\n\r\n', 'utf-8'))
        elif line_string[0] == "BYE":
            self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
        elif line_string[0] == "ACK":
            aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 <' + fichero_audio
            os.system(aEjecutar)
        elif line_string[0]!= 'INVITE':
            self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n\r\n')
        elif line_string[0]!= 'BYE':
            self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n\r\n')
        elif line_string[0]!= 'ACK':
            self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n\r\n')
        else:
            self.wfile.write(b'SIP/2.0 400 Bad Request\r\n\r\n')


if __name__ == "__main__":
    try:
        serv = socketserver.UDPServer((sys.argv[1], int(sys.argv[2])),EchoHandler)
        fichero_audio = sys.argv[3]
        print("Listening...\r\n")
        if not os.path.isfile(fichero_audio):
            sys.exit('File error: ' + fichero_audio + ' does not exist')
            print('Listening...\r\n')
    except IndexError:
        sys.exit('Usage: python3 server.py IP port audio_file')
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('Fin')
