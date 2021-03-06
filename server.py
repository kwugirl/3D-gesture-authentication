from flask import Flask, flash, render_template, redirect, request, session, url_for
import urllib  # used for URL encoding
import random
import model
import dtw_algorithm
import decode_vector
import struct


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route("/")
def index():

    gif_url = None
    if "email" in session:
        gif_name = str(random.randint(1, 8)) + ".gif"
        gif_url = url_for('static', filename='images/rewards/'+gif_name)

    user = request.args.get('user', '')

    return render_template("index.html", gif_src=gif_url, user=user)


@app.route("/create_user")
def create_user():
    return render_template("create_user.html")


@app.route("/save_user", methods=["POST"])
def save_user():
    form_email = urllib.quote(request.form['email'])

    # checking that username was entered
    if form_email:
        # checking that username doesn't already exist in DB
        user = model.session.query(model.User).filter_by(email=form_email).first()

        if user:
            flash('Username already taken, please choose a different username.')
            return redirect(url_for('create_user'))

    else:
        flash('Please enter a username.')
        return redirect(url_for('create_user'))

    try:
        # get gestures back into lists of xyz vector lists
        form_password1 = decode_vector.decode(request.form['password1'])
        form_password2 = decode_vector.decode(request.form['password2'])
        form_password3 = decode_vector.decode(request.form['password3'])
    except (TypeError, struct.error):
        flash('Password samples must be motion gestures, please try again.')
        return redirect(url_for('create_user'))

    gesture1 = dtw_algorithm.create_gesture(form_password1)
    gesture2 = dtw_algorithm.create_gesture(form_password2)
    gesture3 = dtw_algorithm.create_gesture(form_password3)

    gestures = [gesture1, gesture2, gesture3]

    # TODO: better way to do this combinatorics?
    # run DTW on all pairs of samples (3 choose 2 combinatorics), store greatest difference as user's personal threshold
    threshold = max(gesture1 - gesture2, gesture1 - gesture3, gesture2 - gesture3)

    new_user = model.User(email=form_email, password=gestures, threshold=threshold)
    model.session.add(new_user)
    model.session.commit()

    flash('New user ' + request.form['email'] + ' created!')
    return redirect(url_for('index'))


@app.route("/validate_login", methods=["POST"])
def validate_login():
    form_email = urllib.quote(request.form['email'])

    try:
        form_password = decode_vector.decode(request.form['password'])
    except (TypeError, struct.error):
        flash('Password must be a motion gesture, please try again.')
        return redirect(url_for('index'))

    gesture = dtw_algorithm.create_gesture(form_password)

    authentication = False

    user = model.session.query(model.User).filter_by(email=form_email).first()

    if user:
        for password in user.password:
            # form password must be within user's own threshold for variability for at least one of 3 initial training samples
            if gesture - password <= user.threshold:
                authentication = True
                break

    if authentication is True:
        session['email'] = request.form['email']
        session['user_id'] = user.id

    else:
        flash('Please enter a valid username and password.')
        user = request.form['email']

    return redirect(url_for('index', user=user))


@app.route("/logout")
def logout():
    session.pop('email', None)
    session.pop('user_id', None)
    flash('You have logged out.')

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
