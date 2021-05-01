import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
  port = os.getenv('PORT', '5000')
  app.run(host="0.0.0.0", port=port, debug=True)