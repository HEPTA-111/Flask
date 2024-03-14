from flask import Flask
app = Flask(__name__)


@app.route ('/blog/<postID>')
def show_blog(postID):
    return 'The blog number %s ' %postID 



@app.route ('/rev/revNO')
def rvision(revNO):
    return 'The revision number is %f ' %revNO

if __name__ == '__main__':
    app.run()