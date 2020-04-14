from flask import Blueprint, Response
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello, world!"
