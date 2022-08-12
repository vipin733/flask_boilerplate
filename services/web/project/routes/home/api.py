from flask import jsonify

from . import home
from ...controller.user import HomeController


@home.route('',  methods=['GET'])
def index():
    controller = HomeController()
    data = controller.index()
    return jsonify(data), 200

   
