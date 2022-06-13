import random
from flask import Flask, render_template, request, url_for, flash, redirect

from main import app


def get_word():
    # wortliste holen
    word_list = ["hallo", "grüen", "prost", "fäldi", "wixxe", "chlei", "auäää", "liebi"]
    word = random.choice(word_list)
    return word

word = get_word()

