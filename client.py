#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
try:
# Dirección IP del servidor y método.
    METODO = sys.argv[1]
    SERVER = sys.argv[2].split('@')[-1].split(':')[0]
    PORT = int(sys.argv[2].split(':')[-1])
    print("Enviando: " + METODO + ' sip:' + SERVER + ' SIP/2.0')
except:
    sys.exit('Usage: python3 client.py method receiver@IP:SIPport')
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    LINE = ''

    if METODO == 'INVITE':
        LINEA = (METODO + ' sip:' + sys.argv[2].split(':')[0] + ' SIP/2.0')
        my_socket.send(bytes(LINEA, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido..\r\n\r\n', data.decode('utf-8'))
        
        if data.decode('utf8') == ('SIP/2.0 100 Trying\r\n\r\n'
                                   'Sip/2.0 180 Ringing\r\n\r\n'
                                   'SIP/2.0 200 OK\r\n\r\n'):
            LINEA = ('ACK' + ' sip:' + sys.argv[2].split(':')[0] + ' SIP/2.0')
            my_socket.send(bytes(LINEA, 'utf-8' ) + b'\r\n')
    elif METODO == 'BYE':
        LINEA = (METODO + ' sip:' + sys.argv[2].split(':')[0] + ' SIP/2.0')
        my_socket.send(bytes(LINEA, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido..\r\n\r\n', data.decode('utf-8'))

print("Fin.")

