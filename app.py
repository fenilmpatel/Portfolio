from flask import Flask,render_template,url_for

app = Flask(__name__)
posts = [
{
    'author':"John Doe",
    'title' : 'Flask blog 1',
    'Date' : 'september 9,2020',
    'content': 'blog post 1'
},
{
       'author':"Jane Doe",
    'title' : 'Flask blog 2',
    'Date' : 'september 10,2020',
    'content': 'blog post  2'
}

]
@app.route('/')
@app.route('/home')

def home():

    return render_template('home.html',posts=posts,title='Home')

@app.route('/about')

def about():

    return render_template('about.html',title='About',posts=posts)


if __name__ == "__main__":

    app.run(debug=1 ) # or True



