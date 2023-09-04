from models.airpolution import Airpolution
import pandas as pd
import joblib
import sklearn
# 1.0.2 
print("Scikit-Learn version:", sklearn.__version__) # 1.3.0

# Load the model from the saved file
loaded_model = joblib.load('DecisionTreeClassifierModel.pickle')

def sourece_detect(activity: Airpolution):
    print("<===== Detect Source Airpolution =====>", activity)
    
    s2 = [[activity.nox], [activity.co], [activity.so2]]
    df = pd.DataFrame({'NOx': s2[0], 'CO': s2[1], 'SO2': s2[2]})
    print(df)

    sample = df.iloc[:, :].values 

    predict_res = loaded_model.predict(sample)

    print('predict', predict_res)
    
    if predict_res[0] == 0:
        res = "Mobile"
    elif predict_res[0] == 1:
        res = "Stationary"
    elif predict_res[0] == 2:
        res = "Area"
    elif predict_res[0] == 3:
        res = "Good"
    else:
        res = "Unknown"
        
    return {"status_code": 200, "result": res}
