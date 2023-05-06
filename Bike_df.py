import pandas as pd

bike_place = pd.read_csv(r"C:\KMITL\2nd Year\2nd semester\AI Technology\Project\Biking1.csv")
result = pd.DataFrame(columns=bike_place.columns)
bike_place = bike_place.dropna()
bike_place["Features"] = bike_place["Features"].apply(eval)

def recommendation(bike_place, result, p, f, a):
    bike_place = bike_place.loc[bike_place["Province"] == p]
    bike_place = bike_place.loc[bike_place["Recommendation"] == a]
    bike_place = bike_place.reset_index(drop=True)

    for i in range(0, bike_place.shape[0]):
        if len(str(bike_place["Features"][i])) > 2:
            for j in range(0, len(bike_place["Features"][i])):
                if int(bike_place["Features"][i][j]) == f:
                    result = pd.concat([bike_place.iloc[[i]], result])
        else:
            if int(bike_place["Features"][i]) == f:
                result = pd.concat([bike_place.iloc[[i]], result])

    result = result.reset_index(drop=True)
    
    if result.empty:
        recommend_loc = "No Recommendation"
    else:
        recommend_loc = result["Name"].iloc[0]

    return recommend_loc