from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    companies = ['apple', 'uber', 'tesco', 'mcdonalds', 'tfl', 'sainsburys', 'waitrose', 'boots']
    sum = ['£20.05', '£18.90', '£15.50', '£2.09', '£1.99', '£1.05', '£0.75', '£0.02']
    total_donated = "65.09"
    return render_template("home.html", zipped_data=zip(companies, sum), total_donated=total_donated)


if __name__ == "__main__":
    app.run(debug=True)
