import os
from flask import (Flask, render_template, request, make_response, url_for, 
session, redirect, flash, abort)
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key='randomstringapapun'


#membuat fungsi errorhendler
@app.errorhandler(401)
def not_autorized(e):
  return render_template('401.html'), 401
#membuat basic routing pada flask
@app.route('/')

#membuat fungsi untuk halaman index
def index():
  #mengakses parameter get
  search = request.args.get('search')
  #menggunakan templating url jinja
  return render_template('index.html', search=search)
  #video = request.args.get('video')
  #cek parameter search
  #if not search:
      #return render_template('index.html')

  
  #return 'hasil search adalah :'+ search + 'no video adalah :'+ video
  #return 'hallo kamu sedang belajar python menggunakan framework flask'

#membuat fungsi static untuk halaman setting
#@app.route('/settings')
#def show_settings():
  #return 'hallo kamu sedang berada di halaman settings'


#membuat funhgsi upload gambar
ALLOWED_EXTENSION=set(['png','jpg','jpeg'])
app.config['UPLOAD_FOLDER']='uploads'

#fungsi untuk allow nama file
def allowwed_file(filename):
  return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

@app.route('/uploadfile', methods=['GET','POST'])
def uploadfile():
  if request.method == 'POST':
    file =request.files['file']

    if 'file' not in request.files:
      return redirect(request.url)

    if file.filename == '':
      return redirect(request.url)


    if file and allowwed_file(file.filename):
      filename=secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER']+filename))
      return 'file berhail disimpan di....'+ filename

  return render_template('upload.html')


#membuat fungsi dinamis untuk halaman profile
@app.route('/profile/<username>')
def show_profile(username):
  return render_template('profile.html', nama_baru=username)
  #return 'hallo kamu sedang berada di halaman profile %s ' % username

#membuat fungsi dinamis untuk mengambil id
#@app.route('/blog/<int:blog_id>')
#def show_blog(blog_id):
  #return 'hallo kamu sedang berada di halaman blog %d ' % blog_id

#membuat fungsi login dan mengambil nilai post
@app.route('/login', methods=['GET','POST'])
def show_login():
  if request.method == 'POST':
    # resp =make_response('Email kamu adalah' + request.form['email'])
    # resp.set_cookie('email_user',request.form['email'])

    #membuat abourt error 
    if request.form['password'] == '':
      abort(401)

    session['username']=request.form['email']
    flash('kamu berhasil login', 'success')
    return redirect(url_for('show_profile', username=session['username']))
    return 
  
  if 'username' in session:
    username=session['username']
    return redirect(url_for('show_profile', username=username))
  return render_template('login.html')


@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('show_login'))


@app.route('/getcookie')
def getCookie():
  email = request.cookies.get('email_user')
  return 'email yang tersimpan di cookie adalah :'+ email