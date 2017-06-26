#!/usr/bin/env python

# All stuff related to connection with university network
# 
# Copyright 2017, Krzysztof Kutt

import sys

import requests
import webbrowser
import http.cookiejar
import urllib.parse
import urllib.request

if __name__ == '__main__':
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPRedirectHandler(),
        urllib.request.HTTPHandler(debuglevel=0),
        urllib.request.HTTPSHandler(debuglevel=0),
        urllib.request.HTTPCookieProcessor(cj)
    )
    opener.addheaders = [
        ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                        'Windows NT 5.2; .NET CLR 1.1.4322)'))
    ]

    # firstly open the website to go through HTTP Redirection (maybe we
    # should do this in a loop as long as url is changing)
    response = opener.open(
        "http://wbg2.bg.agh.edu.pl/han/science-direct-elsevier/"
    )

    # show login page to the user and gather the login data
    import ghost
    import time
    g = ghost.Ghost()
    with g.start(display=True) as gsess:
        gsess.open("http://wbg2.bg.agh.edu.pl/han/science-direct-elsevier/")
        gsess.show()
        time.sleep(10)



    # # tkinker HtmlFrame test
    # try:
    #     import tkinter as tk
    # except ImportError:
    #     import Tkinter as tk
    #
    # from tkinterhtml import HtmlFrame
    #
    # root = tk.Tk()
    #
    # frame = HtmlFrame(root, horizontal_scrollbar="auto")
    # frame.grid(sticky=tk.NSEW)
    #
    # frame.set_content("""
    # <html>
    # <body>
    # <h1>Hello world!</h1>
    # <p>First para</p>
    # <ul>
    #     <li>first list item</li>
    #     <li>second list item</li>
    # </ul>
    # <img src="http://findicons.com/files/icons/638/magic_people/128/magic_ball.png"/>
    # </body>
    # </html>
    # """)
    #
    # # print(frame.html.cget("zoom"))
    #
    # root.columnconfigure(0, weight=1)
    # root.rowconfigure(0, weight=1)
    # root.mainloop()




    # login_data = urllib.parse.urlencode(
    #     {'plainuser': '',
    #      'password': '',
    #      'auth': 'auto',
    #      'user': ''}
    # ).encode()
    #
    # # then, do the request with login data firstly open the website to go
    # # through HTTP Redirections
    # response = opener.open(
    #     "https://login.wbg2.bg.agh.edu.pl/hhauth/login",
    #     login_data
    # )
    #
    # for line in response.readlines():
    #     line = line.decode()
    #     print(line, end="")
    #
    # # s = requests.Session()
    # # r = s.post("http://wbg2.bg.agh.edu.pl/han/science-direct-elsevier/",
    # #            login_data)
    # #
    # # print(r)
    # # c = r.cookies
    # # i = c.items()
    # #
    # # for name, value in c:
    # #     print(name, value)
    # #
    # # webbrowser.get()
