#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from submit import app

if __name__ == '__main__':
  WSGIServer(application, bindAddress='/var/run/fcgi.sock').run()
