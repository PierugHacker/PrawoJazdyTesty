from flask import Blueprint, send_from_directory

media = Blueprint('media', __name__)

@media.route('/<path:path>')
def sendMedia(path):
    return send_from_directory('base/media/', path)