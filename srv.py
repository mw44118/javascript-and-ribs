# vim: set expandtab ts=4 sw=4 filetype=python:

import logging
import mimetypes
import wsgiref.simple_server

logging.basicConfig(level=logging.DEBUG)

paths = dict({
    '/fundamentals': 'fundamentals.html',
    '/popup': 'popup.html',
    '/matt.css': 'matt.css',
    '/toc': 'toc.html',
    '/extract': 'extract.html',
})


def app(environ, start_response):

    file_to_read = paths.get(environ['PATH_INFO'])

    if file_to_read:
        mimetype, encoding = mimetypes.guess_type(file_to_read)
        start_response('200 OK', [('Content-Type', mimetype)])
        return [open(file_to_read).read()]

    else:
        start_response('404 OK', [('Content-Type', 'text/plain')])
        return ['404']

if __name__ == '__main__':
    srv =  wsgiref.simple_server.make_server('', 65432, app)
    srv.serve_forever()
