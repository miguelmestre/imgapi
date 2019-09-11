from flask import Flask, jsonify, request, send_file
from google_images_download import google_images_download
import urllib.request

app = Flask(__name__)

#Recieves JSON request to return image.

@app.route('/imgapi/image_search', methods=['POST'])
def image_search():
	
	#Recieves json request into req_data
	req_data = request.get_json()

	#Retrieve images to search
	search_argument = req_data['search']

	#Default number of images to search is 1
	number_images = 1
	if 'number' in req_data:
		number_images = req_data['number']

		
	response = google_images_download.googleimagesdownload()
	#Defines search arguments to search on google
	arguments = {"keywords":search_argument,"limit":number_images,"no_directory":True,"no_download":True}
	# Retrieves images to paths
	paths = response.download(arguments)

	return jsonify({"image":paths})

@app.route('/imgapi/image_download', methods=['GET'])
def image_download():
	download=request.args['download']
	print(download)
	urllib.request.urlretrieve(download,'imgdownload.jpg')

	return send_file('imgdownload.jpg',mimetype='image/gif')


if __name__ == '__main__':
	app.run(debug=True)