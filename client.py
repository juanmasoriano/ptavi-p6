#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
METODO = sys.argv[2]
SERVER = sys.argv[3]split(':')[0]
PORT = sys.argv[3].split(':')[-1]

# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))
    if METODO == INVITE:
        print("Enviando: " + METODO + ' sip:' + SERVER + ' SIP/2.0')
        my_socket.send(bytes(METODO, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        if data.decode('utf8') == ('SIP/2.0 100 Trying\r\n\r\n'
                                   'Sip/2.0 180 Ringing\r\n\r\n'
                                   'SIP/2.0 200 OK\r\n\r\n')
            my_socket.send(bytes("ACK" + 'sip' + SERVER + 'SIP/2.0' ))

    elif METODO == BYE:
        print("Enviando: " + METODO + ' sip:' + SERVER + ' SIP/2.0')
        my_socket.send(bytes(METODO, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
