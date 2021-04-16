# coding: utf-8
from browser import document, alert


def echo(event):
    alert("Hello World!")


document["button"].bind("click", echo)
