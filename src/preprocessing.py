import pandas as pd

def clean_data(df):
    df = df.drop(columns=["Product ID","UDI","TWF","HDF","PWF","OSF","RNF"])
    df.rename(columns={"Air temperature [K]":"Air_temperature","Process temperature [K]":"Process_temperature",
                  "Rotational speed [rpm]":"Rotational_speed","Torque [Nm]":"Torque","Tool wear [min]":"Tool_wear"},inplace=True)
    
    types = pd.get_dummies(df['Type'],drop_first=True)
    df.drop('Type',axis='columns',inplace=True)
    df = pd.concat([df,types],axis='columns')  
    
    return df

print("HI from preprocessing.py")
