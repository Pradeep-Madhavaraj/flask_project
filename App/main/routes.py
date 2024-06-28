from flask import Blueprint, render_template, request, flash, redirect, url_for
from App.models import Post
from App.main.forms import FeedbackForm
from App.models import Feedback
from App import db

main = Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/announcements')
def announcements():
    return render_template('announcements.html')

@main.route('/feedback', methods=['GET', 'POST'])
def feedback_page():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(name=form.name.data , email=form.email.data , subject=form.subject.data , message=form.message.data)
        db.session.add(feedback)
        db.session.commit()
        flash(message=f"Thanks for your valueable Feedback!, We'll make sure to go through your feedback!.", category='success')
        return redirect(url_for('main.home'))
    return render_template('feedback.html', legend='Feedback', title = 'Feedback', form=form)

@main.route('/contactus')
def contact_us():
    return render_template('contactus.html')