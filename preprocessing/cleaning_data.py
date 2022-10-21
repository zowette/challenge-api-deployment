import pandas as pd

class Cleaning():
    
    df = pd.read_json("informations.json")
    

    def __init__(self):
        self.number_of_bedrooms = (int(self.df.loc[self.df[0] == "rooms_number"][1].values[0]))
        self.surface = (int(self.df.loc[self.df[0] == "area"][1].values[0]))
        self.fully_equipped_kitchen = (bool(self.df.loc[self.df[0] == "equipped_kitchen"][1].values[0]))
        self.open_fire = (bool(self.df.loc[self.df[0] == "open_fire"][1].values[0]))
        self.number_of_facades = (int(self.df.loc[self.df[0] == "facades_number"][1].values[0]))
        self.terrace = (bool(self.df.loc[self.df[0] == "terrace"][1].values[0]))
        self.terrace_surface = (int(self.df.loc[self.df[0] == "terrace_area"][1].values[0]))
        self.swimming_pool = (bool(self.df.loc[self.df[0] == "swimming_pool"][1].values[0]))
        self.state_of_the_building = (str(self.df.loc[self.df[0] == "building_state"][1].values[0]))
        self.zip_code_ratio = (int(self.df.loc[self.df[0] == "zip_code"][1].values[0]))
        self.property_type = (str(self.df.loc[self.df[0] == "property_type"][1].values[0]))
                
    def preprocess(self):
        if self.fully_equipped_kitchen == True:
            self.fully_equipped_kitchen = 1
        else:
            self.fully_equipped_kitchen = 0
                
        if self.open_fire == True:
            self.open_fire = 1
        else:
            self.open_fire = 0            
        
        if self.terrace == True:
            self.terrace = 1
        else:
            self.terrace = 0
    
        if self.swimming_pool == True:
            self.swimming_pool = 1
        else:
            self.swimming_pool = 0        
                
        if self.state_of_the_building == "NEW":
            self.state_of_the_building = 1
        elif self.state_of_the_building == "JUST RENOVATED" :
            self.state_of_the_building = 0.75
        elif self.state_of_the_building == "GOOD":
            self.state_of_the_building = 0.5
        elif self.state_of_the_building == "TO RENOVATE" or "TO REBUILD":
            self.state_of_the_building = 0.25

        self.zip_code_ratio = 'be_zip_'+str(self.zip_code_ratio)[:-1]
        df_zip_code = pd.read_csv("preprocessing/diczipcoderatio.csv", names=["zipcode", "score"], skipinitialspace=True)
        self.zip_code_ratio = (df_zip_code["zipcode"] == self.zip_code_ratio)
        self.zip_code_ratio = df_zip_code[self.zip_code_ratio]["score"].values[0]
            
            
        data = {'property_type' : self.property_type, 'number_of_bedrooms': self.number_of_bedrooms, 'surface' : self.surface, 'fully_equipped_kitchen' : self.fully_equipped_kitchen, 'open_fire' : self.open_fire, 'number_of_facades' : self.number_of_facades, 'terrace' : self.terrace, 'terrace_surface' : self.terrace_surface, 'swimming_pool' : self.swimming_pool, 'state_of_the_building' : self.state_of_the_building, "zip_code_ratio" :self.zip_code_ratio} 
        self.df_clean_for_prediction = pd.DataFrame([data])
        # self.df_clean_for_prediction.to_csv("predict/df_clean_for_prediction.csv")
        
        return self.df_clean_for_prediction
        
                

        


