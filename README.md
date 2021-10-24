# API Prediction
## Content:
* EDA
* Training model
* Deployment
* How to use

### EDA
* Exploratory data analysis for the dataset from Kaggle 'Bike Sharing Demand'

  Bike sharing systems are a means of renting bicycles where the process of obtaining membership, rental, and bike return is automated via a network of kiosk locations throughout a city. Using these systems, people are able rent a bike from a one location and return it to a different place on an as-needed basis. Currently, there are over 500 bike-sharing programs around the world.

    ![image](https://user-images.githubusercontent.com/64044526/138588068-e9131214-1a46-4833-a5bd-96f7cab7deac.png)
    
    To take an overview on the dataset and the datafield:
    https://www.kaggle.com/c/bike-sharing-demand/overview
    
### Train Model
 * Fitting the model ( LinearRegression from Sklearn )

  I did preprocessing the data something like: Handling missing values, Outlier removal, Normalize the feature before fitting phase, and after that I have evaluated the model using some metrics from Sklearn ( 'Mean_Squared_Error' ).

### Deployment the application using Flask
I have craeted two endpoints to handle the requests, 
* The first one was for make a single prediction for new sample, 
* and the other one was for make a prediction for a new file contains new data


### How you can use the API?
* first you need to clone the repo to your device
* make sure that you have installed docker
* run this command in your shell
    `Docker-compose up` : for build the image and run a container from that image
    `Docker-compose down` : down the server
    
