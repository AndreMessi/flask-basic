from flask import Flask, render_template, request

app = Flask(__name__)

#membuat basic routing pada flask
@app.route('/')

#membuat fungsi untuk halaman index
def index():
    return render_template('index.html')
    #return 'hallo kamu sedang belajar python menggunakan framework flask'

#membuat fungsi static untuk halaman setting
#@app.route('/settings')
#def show_settings():
    #return 'hallo kamu sedang berada di halaman settings'

#membuat fungsi dinamis untuk halaman profile
@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', nama_baru=username)
    #return 'hallo kamu sedang berada di halaman profile %s ' % username

#membuat fungsi dinamis untuk mengambil id
#@app.route('/blog/<int:blog_id>')
#def show_blog(blog_id):
    #return 'hallo kamu sedang berada di halaman blog %d ' % blog_id

#membuat fungsi loginm
@app.route('/login', methods=['GET','POST'])
def show_login():
    if request.method == 'POST':
        return 'Email kamu adalah' + request.form['email']
        
    return render_template('login.html')