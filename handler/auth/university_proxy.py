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

import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser


class MyBrowser(QWebPage):
    ''' Settings for the browser.'''

    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


class Browser(QWebView):
    def __init__(self):
        # QWebView
        self.view = QWebView.__init__(self)
        # self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        # super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.adjustTitle)

    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Browser()
    view.show()
    view.load("http://wbg2.bg.agh.edu.pl/han/science-direct-elsevier/")
    app.exec_()

    # cj = http.cookiejar.CookieJar()
    # opener = urllib.request.build_opener(
    #     urllib.request.HTTPRedirectHandler(),
    #     urllib.request.HTTPHandler(debuglevel=0),
    #     urllib.request.HTTPSHandler(debuglevel=0),
    #     urllib.request.HTTPCookieProcessor(cj)
    # )
    # opener.addheaders = [
    #     ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
    #                     'Windows NT 5.2; .NET CLR 1.1.4322)'))
    # ]
    #
    # # firstly open the website to go through HTTP Redirection (maybe we
    # # should do this in a loop as long as url is changing)
    # response = opener.open(
    #     "http://wbg2.bg.agh.edu.pl/han/science-direct-elsevier/"
    # )

    # # Ghost.py -- nice and simple, but not usable as a part of bigger app
    # # (dependencies problems...)
    #
    # # show login page to the user and gather the login data
    # import ghost
    # import time
    # g = ghost.Ghost()
    # with g.start(display=False) as gsess:
    #     #gsess.open("http://wbg2.bg.agh.edu.pl/han/science-direct-elsevier/")
    #
    #     # open login page
    #     page1, res1 = gsess.open("http://ghost-py.readthedocs.io/en/latest/")
    #
    #     # wait for page loaded and then show it
    #     page2, res2 = gsess.wait_for_page_loaded()
    #
    #     print(page1.url)
    #     if page2 is not None:
    #         print(page2.url)
    #
    #     gsess.show()
    #
    #     # page is visible as long as it does not change the URL
    #     # (user do some action, e.g. login by clicking on OK)
    #     gsess.wait_for(condition=lambda:
    #                    gsess.page.mainFrame().requestedUrl().toString() !=
    #                    page1.url,
    #                    timeout_message="You have 2 minutes to login",
    #                    timeout=120)
    #
    #     print(gsess.page.mainFrame().requestedUrl().toString())





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
