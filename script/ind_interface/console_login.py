import unittest
import warnings

import requests


class ConsoleLogin(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.url = "https://console.bitasset.cc/proxy/login"
        self.userinfo = {"username": "albert", "password": "orghans211", "googleCode": "888888"}
        self.Headers = {"Server": "nginx", "content-type": "application/json;charset=UTF-8",
                        "date": "Wed, 09 Feb 2022 07:59:50 GMT", "Transfer-Encoding": "chunked",
                        "Connection": "keep-alive",
                        "Set-Cookie": "rememberMe=deleteMe; Path=/; HttpOnly; SameSite=Strict; Max-Age=0; Expires=Tue, 08-Feb-2022 07:59:50 GMT",
                        "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload", "Content-Encoding": "gzip"}

    def test_login(self):
        s = requests.Session()
        response = s.post(self.url, headers=self.Headers, data=self.userinfo).text
        print(response)
        print(self.Headers)


if __name__ == '__main__':
    unittest.main()
