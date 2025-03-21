from RAscore import RAscore_NN #For tensorflow and keras based models
from RAscore import RAscore_XGB #For XGB based models
import pandas as pd

nn_scorer = RAscore_NN.RAScorerNN()
xgb_scorer = RAscore_XGB.RAScorerXGB()

#df = pd.read_csv('red_al_smiles_list_all.csv')
df = pd.read_csv('nitrile_list_emol_pub.csv')
print("reading done...")
print("generating score...")
df['rascore'] = df['smiles'].apply(lambda x: nn_scorer.predict(x))
print("writing file...")
new_df.to_csv('rascore_nitrile_emol_pub.csv', index=False)
