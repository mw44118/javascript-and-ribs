# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import wsgiref.simple_server

logging.basicConfig(level=logging.DEBUG)

def app(environ, start_response):

    logging.debug('%(REQUEST_METHOD)s %(PATH_INFO)s' % environ)

    if environ['PATH_INFO'] == '/fundamentals':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [open('./fundamentals.html').read()]

    elif environ['PATH_INFO'] == '/popup':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [open('./popup.html').read()]

    else:
        start_response('404 OK', [('Content-Type', 'text/plain')])
        return ['404']

    # if environ['PATH_INFO'] == '/fundamentals':


if __name__ == '__main__':
    srv =  wsgiref.simple_server.make_server('', 65432, app)
    srv.serve_forever()
