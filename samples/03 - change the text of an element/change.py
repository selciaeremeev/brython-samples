# coding: utf-8
from browser import document


def change(event):
    document["zone1"].textContent = "New content"


document["button"].bind("click", change)
