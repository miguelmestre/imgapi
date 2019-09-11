# IMGAPI  

This API allow you to submit a JSON request with the text for the image you want to search and will return an JSON request with the links for images.
You can also download that image send a image link trough a HTML query parameters.

You must have Python 3 to use this API

## Install

Make sure you have Python 3 installed

```
python3 --v
```

Install pip

```
sudo apt install python3-pip
```

Install pipenv

```
pip install --user pipenv
```

Instal API dependencies

```
pipenv install
```

## Run API

```
python app.py
```

#API Functions

## Search Image

Send JSON POST requests to the API trough http://127.0.0.1:5000/imgapi/image_search

### Search Keywords

|Keywords   | Mandatory | Default |Function             |
|-----------|:---------:|:-------:|---------------------|
|search     |Yes        |         |Image to search      |
|number     |No         |1        |Number of images     |

*Example:*

{"search" : "cats","number" : 4}

## Download Image

Send a HTML GET request to the API trough http://127.0.0.1:5000/imgapi/image_download

### Query parameters

|Keywords   | Mandatory | Default |Function               |
|-----------|:---------:|:-------:|-----------------------|
|download   |Yes        |         |Image link to download |

*Example:*

http://127.0.0.1:5000/imgapi/image_download?download=https://upload.wikimedia.org/wikipedia/commons/6/66/An_up-close_picture_of_a_curious_male_domestic_shorthair_tabby_cat.jpg