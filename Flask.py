from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello Flask is running =) !</h1>
    <ul>
        <li><a href='/about'>About Page</a></li>
        <li><a href='/user/Ahmed'>User Page</a></li>
        <li><a href='/square/5'>Square of 5</a></li>
    </ul>
    """

@app.route('/about')
def about():
    return "<h2>This is the about page</h2>"

@app.route('/user/<name>')
def user(name):
    return f"<h2>hello {name}</h2>"

@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"<h2>The square is: {result}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
