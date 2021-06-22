from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to SCS '


@app.route('/<part_of_system>/', methods=['GET', 'POST'])
def main_handler(part_of_system):
    print(part_of_system)
    print(request)


if __name__ == '__main__':
    app.run()
