from flask import Flask
app = Flask(__name__)

import os

@app.route('/')
def hello_fedora():
    return 'Hello from Fedora! NS: {0}'.format(os.getenv('OPENSHIFT_BUILD_NAMESPACE'))

if __name__ == '__main__':
    app.run("0.0.0.0")
