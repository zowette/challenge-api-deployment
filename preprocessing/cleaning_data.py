import pandas as pd
                
def preprocess(df):
    
    print(df)
    number_of_bedrooms = (int(df.loc[df[0] == "rooms_number"][1].values[0]))
    surface = (int(df.loc[df[0] == "area"][1].values[0]))
    fully_equipped_kitchen = (bool(df.loc[df[0] == "equipped_kitchen"][1].values[0]))
    open_fire = (bool(df.loc[df[0] == "open_fire"][1].values[0]))
    number_of_facades = (int(df.loc[df[0] == "facades_number"][1].values[0]))
    terrace = (bool(df.loc[df[0] == "terrace"][1].values[0]))
    terrace_surface = (int(df.loc[df[0] == "terrace_area"][1].values[0]))
    swimming_pool = (bool(df.loc[df[0] == "swimming_pool"][1].values[0]))
    state_of_the_building = (str(df.loc[df[0] == "building_state"][1].values[0]))
    zip_code_ratio = (int(df.loc[df[0] == "zip_code"][1].values[0]))
    property_type = (str(df.loc[df[0] == "property_type"][1].values[0]))
    
    print(property_type)
    
    
    if fully_equipped_kitchen == True:
        fully_equipped_kitchen = 1
    else:
        fully_equipped_kitchen = 0
            
    if open_fire == True:
        open_fire = 1
    else:
        open_fire = 0            
    
    if terrace == True:
        terrace = 1
    else:
        terrace = 0

    if swimming_pool == True:
        swimming_pool = 1
    else:
        swimming_pool = 0        
            
    if state_of_the_building == "NEW":
        state_of_the_building = 1
    elif state_of_the_building == "JUST RENOVATED" :
        state_of_the_building = 0.75
    elif state_of_the_building == "GOOD":
        state_of_the_building = 0.5
    elif state_of_the_building == "TO RENOVATE" or "TO REBUILD":
        state_of_the_building = 0.25

    zip_code_ratio = 'be_zip_'+str(zip_code_ratio)[:-1]
    df_zip_code = pd.read_csv("preprocessing/diczipcoderatio.csv", names=["zipcode", "score"], skipinitialspace=True)
    zip_code_ratio = (df_zip_code["zipcode"] == zip_code_ratio)
    zip_code_ratio = df_zip_code[zip_code_ratio]["score"].values[0]
        
        
    data = {'property_type' : property_type, 'number_of_bedrooms': number_of_bedrooms, 'surface' : surface, 'fully_equipped_kitchen' : fully_equipped_kitchen, 'open_fire' : open_fire, 'number_of_facades' : number_of_facades, 'terrace' : terrace, 'terrace_surface' : terrace_surface, 'swimming_pool' : swimming_pool, 'state_of_the_building' : state_of_the_building, "zip_code_ratio" :zip_code_ratio} 
    df_clean_for_prediction = pd.DataFrame([data])
    # df_clean_for_prediction.to_csv("predict/df_clean_for_prediction.csv")
    
    return df_clean_for_prediction
        
                

        


