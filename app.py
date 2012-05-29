from flask import Flask, render_template, url_for, flash, redirect

from flask.ext.wtf import Form, TextField, Optional

SECRET_KEY = "asdfhjgfdsyuhgfcxdsrethgf"
DEBUG = True

class BookNewForm(Form):
        name = TextField('Name')

book = Flask(__name__)
book.config.from_object(__name__)

@book.route('/book/new', methods=['GET', 'POST'])
def customers_new():
    form = BookNewForm()
    print form.errors
    if form.is_submitted():
        print "submitted"
    if form.validate():
        print "valid"
    if form.validate_on_submit():
        flash("Successfully created a new book")
        return redirect(url_for('.books_show'))
    return render_template('books_new.html', form=form)

@book.route('/book/new_no_csrf', methods=['GET', 'POST'])
def customers_new_no_csrf():
    form = BookNewForm(csrf_enabled=False)
    print form.errors
    if form.is_submitted():
        print "submitted"
    if form.validate():
        print "valid"
    if form.validate_on_submit():
        flash("Successfully created a new book")
        return redirect(url_for('.books_show'))
    return render_template('books_new_no_csrf.html', form=form)


@book.route('/books/')
def books_show():
    return render_template('message.html', message = "BookShow")

if __name__ == "__main__":
    book.run()
