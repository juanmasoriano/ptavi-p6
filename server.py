#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        Metodos_sip = ['INVITE','BYE','ACK']

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

            if line.decode('utf-8') == "INVITE":
                self.wfile.write(b'SIP/2.0 100 Trying\r\n\r\n'
                                  'Sip/2.0 180 Ringing\r\n\r\n'
                                  'SIP/2.0 200 OK\r\n\r\n )
            elif line.decode('utf-8') == "BYE":
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            elif line.decode('utf-8') == "ACK":
                os.system('./mp32rtp -i 127.0.01 -p 23032 <' + fichero_audio)
            elif line.decode('utf8') not in Metodos_sip:
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n\r\n')
            else:
                self.wfile.write(b'SIP/2.0 400 Bad Request\r\n\r\n')

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((sys.argv[1], int(sys.argv[2])), EchoHandler)
    print("Listening...")
    serv.serve_forever()
