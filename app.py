from flask import Flask
from flask import render_template
from flask import request

from amzallscrp import Amzallscrp
from predictor import Predictor
from productname import Productname

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/how')
def how():
	return render_template('index.html')

@app.route('/contact')
def contact():
	return render_template('index.html')

@app.route('/result', methods = ['GET'])
def make_decision():
	product_url = request.args.get('product_url')

	productName = Productname(product_url)
	
	reviews = Amzallscrp(product_url)
	list_result = Predictor(reviews)

	number_of_reviews = str(len(reviews))
	
	if reviews is None:
		return '<h1>error: please provide a valid link of a product from amazon.in</h1>'

	else:
		return render_template('result.html', productName = productName, rev = number_of_reviews, pos = list_result[0], neg = list_result[1], neu = list_result[2])
	

if __name__ == '__main__':
	app.run(debug = True)


