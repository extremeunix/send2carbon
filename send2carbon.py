#!/usr/bin/env python
# Copyright 2012 Cyrus Dasadia [cyrus -a-t- extremeunix.com]
#
# send2carbon.py can be used to send metrics to carbon server 
# Example: 
#   send2carbon.py -H localhost -p 2003 -m localhost.foo.bar -v 234
# 
# TODO:
# - Add option of logging 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import time
try:
    from argparse import ArgumentParser
except:
    print "ERROR: Please install 'python-argparse'"
    sys.exit(1)
from socket import socket

parser = ArgumentParser()
parser.add_argument('-H','--host',help='Carbon server hostname',required=True,dest='carbon_server')
parser.add_argument('-p','--port',help='Carbon server port',type=int,required=True,dest='carbon_server_port')
parser.add_argument('-m','--metric',help='Metric name',required=True,dest='metric_name')
parser.add_argument('-v','--value',help='Metric value',required=True,dest='metric_value')
args = parser.parse_args()


def send2carbon(carbon_server,carbon_server_port,metric_name,metric_value):
    sock = socket()
    try:
        sock.connect( (carbon_server,carbon_server_port) )
    except:
        print "ERROR: Could not connect to carbon server %s on port %d\n" % (carbon_server,carbon_server_port)
        sys.exit(1)
    carbon_string = str("%s %s %d\n" % (metric_name, metric_value,  int(time.time())))
    try:
        sock.sendall(carbon_string)
    except:
        print "ERROR: could not send metric to carbon server"
        sys.exit(1)


send2carbon(args.carbon_server,args.carbon_server_port,args.metric_name,args.metric_value)

