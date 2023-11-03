import numpy as np
import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

######## Step 1 : Load Data
    data = pd.read_csv(data_path,index_col=0)

    print("Size of actual dataset",len(data))

######## Step 2 : Clean,Prepare and manipulate data

    feature_name =['Whether','Temperature']

    print("Names of features",feature_name)

    weather =data.Whether
    Temperature =data.Temperature
    play =data.Play
    
    # Creating labelEncoder
    le= preprocessing.LabelEncoder()

    #Converting string label into number
    weather_encoded =le.fit_transform(weather)
    print(weather_encoded)

    #Converting string label into number
    temp_encoded = le.fit_transform(Temperature)
    label =le.fit_transform(play)

    print(temp_encoded)

   #Combining Weather and temp into single listof tuples
    features =list(zip(weather_encoded,temp_encoded))
 
 ######## Step 3 :Train data
    model =KNeighborsClassifier(n_neighbors=3)
   
    # Train data model using training sets 
    model.fit(features,label)

 ######## Step 4 :Test data
    predicted =model.predict([[0,2]]) #0: overcast, 2:Mid
    print(predicted)


def main():
    print("###################################")
    print("Play predictor application using K Nearest Knighbor algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")


if __name__=="__main__":
    main()