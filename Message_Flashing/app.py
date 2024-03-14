from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for flashing messages

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('login.html', error=error)

# Placeholder for the index route
@app.route('/index')
def index():
    return 'This is the index page.'

if __name__ == '__main__':
    app.run(debug=True)
