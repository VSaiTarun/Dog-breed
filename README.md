# Dog-breed prediction web site
this is a web application that predict the breed of the given dog that uploaded using Convolutional Neural Network(CNN) model.
### Basic applications you need to know to develop this project are 
> python,
> flask API or framework,
> Tensorflow
### Need to make sure to have following libraries in your pc
* python
* numpy,pandas
* Tensorflow
* pillow

# Running the application
*This flask framework will provie you a mini web server to give inputs to your model from a web site and to run this first you need to create an enviroment and should run flask in that.*

# Building a Model
The data set is taken from kaggle and trained with over more than 30,000 images having more than 1,000 different dog breeds.

Building a CNN architecture using keras and tensorflow modules for imgae classification consisting of several hidden layers and dropout layers 
with specified dropout to avoid overfitting.

# Training the model
The model was trained using appropriate loss function,optimizers and learning rate and has achieved over a 96.5% of accuracy level on the test data set.

This trained model has been stored 'dog_breed_model.h5' file using save.model() in the project library.

# How to open
upon creating the environment we need to create a html file for the web site and also create a python file named app.py 

Note that we have to create a folder called template and have to put this HTML file for flask applications.

Activating our flask environment and setting the flask app(app.py) variable to our flask app.

run the flask app by using 'flask run' command,this will start the flask development server and make our web site accessible at localhost:5000.

By reaching to that site and giving inputs in .png format we will get desired ouputs.

### Refrence
https://www.section.io/engineering-education/deploying-machine-learning-models-using-flask/



## Sample Input and Output

>input
<img width="600" alt="image" src="https://github.com/VSaiTarun/Dog-breed/assets/132877695/ce395fa7-af9f-4a54-920c-ca2bd3ba5c30">


>ouput
<img width="600" alt="image" src="https://github.com/VSaiTarun/Dog-breed/assets/132877695/7a4cb14b-6df9-4f9b-80ca-13b073971bd2">




