import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


class Prediction():
    
    df = pd.read_csv("predict/df_clean_for_prediction.csv")
    
    def __init__(self):
        self.number_of_bedrooms = self.df["number_of_bedrooms"].values[0]
        self.surface = self.df["surface"].values[0]
        self.fully_equipped_kitchen = self.df["fully_equipped_kitchen"].values[0]
        self.open_fire = self.df["open_fire"].values[0]
        self.number_of_facades = self.df["number_of_facades"].values[0]
        self.terrace = self.df["terrace"].values[0]
        self.terrace_surface = self.df["terrace_surface"].values[0]
        self.swimming_pool = self.df["swimming_pool"].values[0]
        self.state_of_the_building = self.df["state_of_the_building"].values[0]
        self.zip_code_ratio = self.df["zip_code_ratio"].values[0]
        
        self.property_type = self.df["property_type"].values[0]    
        
    
    def predict(self):
        if self.property_type == "HOUSE":
            scaler = pickle.load(open('model/house_scaler.pkl','rb'))
            poly_features = pickle.load(open('model/poly_features_model_house.pkl', 'rb'))
            model = pickle.load(open('model/finalized_model_house.pkl', 'rb'))
                        
            x_house = self.df
            
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
            print(x_house)  
            x_house = x_house.iloc[:,1:].values

            x_house = scaler.transform(x_house)        
            x_house_poly = poly_features.fit_transform(x_house)
            y_house_predict = model.predict(x_house_poly)
            price_predict = round((int(y_house_predict)), -3)
                        
            
        
        elif self.property_type == 'APARTMENT':
            scaler = pickle.load(open('model/apartment_scaler.pkl','rb'))
            poly_features = pickle.load(open('model/poly_features_model_apartment.pkl', 'rb'))
            model = pickle.load(open('model/finalized_model_apartment.pkl', 'rb'))
            
            x_apartment = self.df
                                    
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
            
            x_apartment = scaler.transform(x_apartment)        
            x_apartment_poly = poly_features.fit_transform(x_apartment)
            y_apartment_predict = model.predict(x_apartment_poly)
            price_predict = round((int(y_apartment_predict)), -3)
            
            
        return {price_predict}   
            
            
            
