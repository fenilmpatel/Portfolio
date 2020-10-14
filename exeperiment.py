from flask import Flask,render_template,url_for,flash,redirect

from forms import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '388d82b6eb075720aae93f9655d66bb5475153e04aeb5203ae'


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
    return render_template('home01.html',posts=posts,title='Home')

@app.route('/about')
def about():
    return render_template('about01.html',title='About',posts=posts)


@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created successfully for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Successfully!','success')
        return redirect(url_for('home'))
    
    return render_template('login.html',title='Login',form=form)



if __name__ == "__main__":

    app.run(debug=1 ) # or True



