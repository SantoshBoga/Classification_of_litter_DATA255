# Classification of Litter
An application which classifies the type of litter and helps in recycling purposes.

## Abstract

A streamlined process of classifying litter. This is done by modelling a Convolutional Neural Network 
which takes in images of size (300,300) and determines the litter class from the six labels/classes in the dataset. The dataset is obtained 
from Kaggle.
This model is exposed as an API using a flask server and for this React server acts as a front end component. The React component or the front-end
of the application displays the image along with classified label and prediction probability.


## Technology stack
*Programming languages & Libraries*: Python, keras, scikit-learn, tensorflow

*Technologies*: Machine Learning, Computer Vision, Deep Learning

*Web Technologies*: HTML5, CSS3, JavaScript, React, Redux, Node.JS, REST API

*Miscellaneous* : SOA, Agile, Git, Anaconda

## Steps to run the application
0. Clone the repository
1. Run GarbageClassification.ipynb to train and download the trained model.
2. Up the backend server by navigating to base_react_app/src/MLOutputs and running app.py python file 
	 *$python app.py*
3. Run the front-end React Server in the directory of base_react_app by executing the command 
	 *$npm i *
	to install the node modules
4. After installing the node modules run the following command to start the front-end server
	*$npm start*
5. The front-end server redirects to http://localhost:3000 there you can upload the image you want to classify which displays the 
image along with the classified label and prediction probability

## Sample Output
<img width="900" alt="sample output" src="https://github.com/SantoshBoga/Classification_of_litter_DATA255/blob/main/sample_output.JPG">

## Contributors
Sai Santosh Boga

Rashmi Gubby Prasad

Shravika Narayanam

Sukriti Mishra