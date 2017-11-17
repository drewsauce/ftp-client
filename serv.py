#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :serv.py
# description     :Server side operations of local FTP server
# author          :Andrew Ruppel
# date            :11/26/2017
# version         :0.1
# usage           :python serv.py <port>
# notes           :
# python_version  :2.7.12
##############################

# Import modules
import socket
import sys
import commands


def run(cli_args):
    """Start our FTP server and
    Listen for client connections.
    :type cli_args user input arguments
    """
    port = check_input(cli_args)
    ftp_socket = initialize(port)
    listen(ftp_socket)


def check_input(cli_args):
    """Check user input to start the server for correct
    number of parameters.
    :type cli_args user input
    :rtype cli_args[port]
    """
    arg_length = len(cli_args)
    if arg_length == 2:
        return cli_args[1]
    else:
        if arg_length == 1:
            sys.exit("Argument Exception: You are missing the socket parameter.\n")
        if arg_length > 2:
            sys.exit("Argument Exception: Your arguments exceed the the required parameters.\n")
        initialization_prompt()


def initialize(port):
    """Server initialization
    :type port string
    :rtype ftp_socket socket._socketobject
    """
    try:
        server_port = int(port)
        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.bind(('', server_port))
        ftp_socket.listen(1)
        print "Server has been initialized, listening on port %s" % str(server_port)
    except socket.error as socket_error:
        print "Socket Error: %s" % socket_error
        sys.exit()
    return ftp_socket


def listen(ftp_socket):
    """Listen for clients
    :type ftp_socket socket.socket
    """
    while 1:
        connection, address = ftp_socket.accept()
        print "Accepted connection from %s" % str(address)
        connection.send("Thanks for connection. Bye.")
        connection.close()
        break

    # close our host socket
    ftp_socket.close()


def print_help():
    """Print instructions"""
    help = "###############################\n" \
           "#         FTP COMMANDS        #\n" \
           "###############################\n" \
           "help: print help\n" \
           "get <filename>: downloads a file <file_name>\n" \
           "put <filename>: uploads a file <file_name>\n" \
           "ls: lists directory\n" \
           "quit: disconnects from the server\n"
    print help


def initialization_prompt():
    """Print initialization prompt in case too few arguments passed"""
    print "Example usage: python serv.py <port number>"


# Run
if __name__ == '__main__':
    run(sys.argv)
