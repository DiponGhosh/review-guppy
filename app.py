from flask import Flask
from flask import render_template
from flask import request

from amzallscrp import Amzallscrp
from predictor import Predictor
from productname import Productname
from imgLink import ImgLink

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

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
	if not productName:
		return '<h1>Connection Error</h1> <br/> <h3>Unstable Connection</h3>'

	imageLink = ImgLink(product_url)
	if not productName:
		return '<h1>Connection Error</h1> <br/> <h3>Unstable Connection</h3>'
	
	reviews = Amzallscrp(product_url)


	'''
	while number_of_reviews != len(reviews):
		reviews, number_of_reviews = Amzallscrp(product_url)'''

	if reviews is None:
		return '<h1>error: please provide a valid link of a product from amazon.in <br/>or, there are no reviews for this product</h1>'

	list_result = Predictor(reviews)

	positive_logo = '../static/images/positive.png'
	neutral_logo = '../static/images/neutral.png'
	negative_logo = '../static/images/negative.png'

	#check condition
	result_logo_src = positive_logo
	
	return render_template('result.html', productName = productName, rev = str(len(reviews)), pos = list_result[0], neg = list_result[1], neu = list_result[2])
	

if __name__ == '__main__':
	app.run(debug = True)


