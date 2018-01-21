from flask import Flask, request
import account.service


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return 'up'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login2'


@app.route('/user/account/register', methods=['POST'])
def user_account_register():
    return account.service.register(request.form)


if __name__ == '__main__':
    app.run(debug=True)
