from flask import Flask
from flask import render_template
from flask import request

from amzallscrp import Amzallscrp
from predictor import Predictor
from productname import Productname
from pieResult import PieResult
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
		return '<h1>productname Connection Error</h1> <br/> <h3>Unstable Connection</h3>'

	imageLink = ImgLink(product_url)
	if not imageLink:
		return '<h1>imagelink Connection Error</h1> <br/> <h3>Unstable Connection</h3>'
	
	reviews = Amzallscrp(product_url)


	'''
	while number_of_reviews != len(reviews):
		reviews, number_of_reviews = Amzallscrp(product_url)'''

	if reviews is None:
		return '<h1>error: please provide a valid link of a product from amazon.in <br/>or, there are no reviews for this product</h1>'

	list_result = Predictor(reviews)

	result_pie_src = PieResult(list_result)

	positive_logo = '../static/images/positive.png'
	neutral_logo = '../static/images/neutral.png'
	negative_logo = '../static/images/negative.png'
	#result_pie_src = '../static/images/result_pie.png'

	#check condition
	result_logo_src = negative_logo
	result_text = "purchase it"
	
	return render_template('decision.html', productName = productName, product_url=product_url,
							rev = str(len(reviews)),
							pos = list_result[0], neg = list_result[1], neu = list_result[2],
							product_image_src=imageLink, result_logo_src=result_logo_src,
							result_pie_src=result_pie_src, result_text=result_text)
	

if __name__ == '__main__':
	app.run(debug = True)


