import pandas as pd
import json

df = pd.read_csv(r'C:\Users\anmol\OneDrive\Desktop\Work\EV_FLEET\fleet_complete_v2.csv')  

sample = df.sample(1).iloc[0]

exclude = ['SOH', 'Battery_RUL_Cycles', 'Thermal_Runaway_Risk_Score', 
           'Lithium_Plating_Risk', 'Maintenance_Type']

sample_dict = sample.drop(exclude, errors='ignore').to_dict()

sample_dict = {k: float(v) if isinstance(v, (int, float)) else str(v) 
               for k, v in sample_dict.items()}

print(json.dumps(sample_dict, indent=2))

with open('sample_request.json', 'w') as f:
    json.dump(sample_dict, f, indent=2)

print("\n Saved to sample_request.json")

