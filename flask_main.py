from flask import Flask, render_template, url_for
app = Flask(__name__)

mypost = [
    {
        'author': 'Sri M',
        'title': 'Shunya',
        'content': 'A Novel in the content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Sadhguru',
        'title': 'Mystic',
        'content': 'Read the content',
        'date_posted': 'May 23, 2016'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = mypost)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True)