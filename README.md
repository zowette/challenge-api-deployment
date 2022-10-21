# Challenge-api-deployment

This API provides predictions from a machine learning model for the real estates in Belgium, scrapped on Immoweb in September 2022. Once the app runs the model returns the predicted price based on given features.

The program was written in Python 3.10 and deployed in Render in order to be used by web-devolopers to create website around it.

# Project Guidelines

Repository: challenge-api-deployment

Type of Challenge: Learning

Duration: 5 days

Team challenge : Solo

# Project Division:

3 main components of this project:

*preprocessing --> cleaning_data.py* : It clean the data to fit to the model pre-saved in an other challenge.

*predict --> prediction.py* : It runs our presaved model and provides a prediction for the user input.

*app.py* : Contains 2 routes. This file creates a FastAPI for providing price prediction. It containes 2 routes. Once its run, it receives the user input as JSON data. After that, this data goes through the preprocessing process and finally it fits the preprocessed data in the presaved model and displays the prediction.

# Running API

pip install -r requirements.txt

python app.py

# End Points

/(GET):
GET request and returns a status of the API.

/predict(GET):
GET request returning a JSON file which shows the expected user input format.

/predict/data(POST):
POST request that receives the data of a house in JSON format.

