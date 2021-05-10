from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
from db import initialize_db, db
from model import Img

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imagerepo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
initialize_db(app)

@app.route('/')
def main_page():
    pictures = Img.query.all()
    picurls = []
    for imgs in pictures:
        picurls.append(imgs.id)
    return render_template('mainpage.html', pictures=picurls)


@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']

    if not pic:
        return render_template('fail.html')

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    img = Img(img=pic.read(), mimetype=mimetype, name=filename)
    db.session.add(img)
    db.session.commit()

    return render_template('upload.html')


@app.route('/delete')
def delete():
    pictures = Img.query.all()
    picurls = []
    for imgs in pictures:
        picurls.append(imgs.id)
    return render_template('delete.html', num=picurls)


@app.route('/deleted', methods=['POST'])
def deleted():
    num = request.form['number']

    ans = Img.query.filter_by(id=num).first()

    if not ans:
        return render_template('fail.html')

    db.session.query(Img).filter(Img.id == num).delete()
    db.session.commit()

    return render_template('deleted.html')


@app.route('/<int:id>')
def get_image(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'No picture with ID', 404

    return Response(img.img, mimetype=img.mimetype)


if __name__ == '__main__':
    app.run()
