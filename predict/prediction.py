import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression      

scaler_house = pickle.load(open('model/house_scaler.pkl','rb'))
poly_features_house = pickle.load(open('model/poly_features_model_house.pkl', 'rb'))
model_house = pickle.load(open('model/finalized_model_house.pkl', 'rb'))

scaler_apartment = pickle.load(open('model/apartment_scaler.pkl','rb'))
poly_features_apartment = pickle.load(open('model/poly_features_model_apartment.pkl', 'rb'))
model_apartment = pickle.load(open('model/finalized_model_apartment.pkl', 'rb'))     
            
def predict(cleaned_df):
    
    df = cleaned_df
    property_type = df["property_type"].values[0]     
      
    if property_type == "property_type.HOUSE":
        x_house = df
        
        atributes_house=['property_type',
                'number_of_bedrooms',
                'surface',
                'fully_equipped_kitchen',
                #'furnished',
                'open_fire',
                #'terrace',
                #'terrace_surface',
                #'garden',
                #'garden_surface',
                #'land_surface',
                'number_of_facades',
                'swimming_pool',
                'state_of_the_building',
                'zip_code_ratio']
        
        x_house = x_house[atributes_house]    
        x_house = x_house.iloc[:,1:].values

        x_house = scaler_house.transform(x_house)        
        x_house_poly = poly_features_house.fit_transform(x_house)
        y_house_predict = model_house.predict(x_house_poly)
        price_predict = round((int(y_house_predict)), -3)
        
        return price_predict                        
        
    
    elif property_type == 'property_type.APARTMENT':
        x_apartment = df
                                
        atributes_apartment=['property_type',
                'number_of_bedrooms',
                'surface',
                'fully_equipped_kitchen',
                #'furnished',
                #'open_fire',
                'terrace',
                'terrace_surface',
                #'garden',
                #'garden_surface',
                #'land_surface',
                #'number_of_facades',
                #'swimming_pool',
                'state_of_the_building',
                'zip_code_ratio']
        
        x_apartment = x_apartment[atributes_apartment]    
        x_apartment = x_apartment.iloc[:,1:].values
        
        x_apartment = scaler_apartment.transform(x_apartment)        
        x_apartment_poly = poly_features_apartment.fit_transform(x_apartment)
        y_apartment_predict = model_apartment.predict(x_apartment_poly)
        price_predict = round((int(y_apartment_predict)), -3)
                
        return price_predict
        
        
        
