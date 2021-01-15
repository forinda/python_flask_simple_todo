from flask import jsonify
config = {
    "SQLALCHEMY_DATABASE_URI":"sqlite:///app/app.db",
    "SQLALCHEMY_TRACK_MODIFICATIONS": True,
    "SECRET_KEY":"2D3333K-0KJF-F22#@@@@@@@@",
    "DEBUG": False,
}

conf = jsonify(config)