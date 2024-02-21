from flask import flash, redirect, render_template, url_for

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route("/", methods=["GET", "POST"])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        message = Message(name=form.name.data, body=form.body.data)
        db.session.add(message)
        db.session.commit()
        flash("Your message have been sent to the world!")
        return redirect(url_for("index"))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template("index.html", form=form, messages=messages)
