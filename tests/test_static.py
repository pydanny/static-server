import random
import threading
import unittest
from wsgiref.simple_server import make_server
from wsgiref.validate import validator

import requests

from static import StringMagic, Shock


def serve_requests(port):
    # Fire up static as a serve
    magics = [StringMagic(title="String Test"), ]
    app = Shock('testdata/pub', magics=magics)
    make_server('localhost', port, validator(app)).serve_forever()


def serve_one_request(count):
    # Start webserver in new thread
    t = threading.Thread(target=serve_requests, args=[count])
    t.daemon = True
    t.start()


class TestMakeServer(unittest.TestCase):

    def setUp(self):
        self.port = random.randrange(10000, 65535)
        serve_one_request(self.port)

    def test_serve_basic(self):
        r = requests.get("http://localhost:{}".format(self.port))
        self.assertEqual(r.status_code, 200)
        self.assertTrue("mixed content test" in str(r.content))

    def test_serve_image(self):
        r = requests.get("http://localhost:{}/682px-Oscypki.jpg".format(self.port))
        self.assertEqual(r.status_code, 200)
        with open("testdata/pub/682px-Oscypki.jpg", "rb") as f:
            image = f.read()
        self.assertEqual(len(r.content), len(image))

