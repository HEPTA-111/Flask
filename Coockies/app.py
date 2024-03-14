from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the 'nm' value from the form
        user = request.form['nm']

    # Create a response object and render the 'cookie.html' template
    resp = make_response(render_template('cookie.html'))
    # Set a cookie named 'userID' with the value from the form
    resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie')
def getcookie():
    # Retrieve the value of the 'userID' cookie
    name = request.cookies.get('userID')
    # Display a welcome message with the retrieved name
    return '<h1>Welcome ' + name + '</h1>'

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)