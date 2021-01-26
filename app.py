from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')

    return render_template("index.html", name=name)

# @app.route('/method', methods=['GET', 'POST'])
# def method():
#     if request.method =='POST':
#         return 'You are using the post method'
#     else:
#         return 'You are Using the get method'


app.run()
