from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Pratik Kumar! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    # Read the two values from the URL (after the ?)
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # The form was submitted: show the thank-you version
        return render_template('contact.html', form_submitted=True)
    else:
        # First visit: show the empty form
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(port=5001)