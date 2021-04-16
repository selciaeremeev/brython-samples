# coding: utf-8
from browser import document
from browser.widgets.dialog import InfoDialog


def hello(event):
    InfoDialog("Demo", "Hello world!", left=event.x, top=event.y)


document["button"].bind("click", hello)
