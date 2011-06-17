# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import wsgiref.simple_server

logging.basicConfig(level=logging.DEBUG)

def app(environ, start_response):

    if environ['PATH_INFO'] == '/fundamentals':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [open('./fundamentals.html').read()]

    elif environ['PATH_INFO'] == '/popup':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [open('./popup.html').read()]

    elif environ['PATH_INFO'] == '/matt.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        return [open('./matt.css').read()]

    else:
        start_response('404 OK', [('Content-Type', 'text/plain')])
        return ['404']

if __name__ == '__main__':
    srv =  wsgiref.simple_server.make_server('', 65432, app)
    srv.serve_forever()
