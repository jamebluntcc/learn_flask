from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


app = Flask(__name__, template_folder='../templates')
app.secret_key = 'haha'


@app.route('/', methods=["GET", "POST"])
def submit():
    form = MyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = form.name.data
            return '<h2>hi,%s</h2>' % user
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
