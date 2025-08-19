import pandas as pd
import os

print(os.getcwd())

Models = ['Claude','Gem_2.5_F','Gem_2.5_P','GPT_4.1_mini','GPT_4o','GPT_o3']

for model in Models:
    input_path=f'Data/Input_Data/RIR/RIR_{model}.xlsx'
    output_dir = 'Data/Intermediate_Data/Cleaned_RIR'
    output_path = f"{output_dir}/Cleaned_RIR_{model}.xlsx"

    df = pd.read_excel(input_path)
    df.replace(r'\bDruz\b', 'Druze', regex=True, inplace=True)
    df['Cleaned_Response']=df.apply(lambda r:r['Response'][len(r['Prompt']):].strip() if r['Response'].startswith(r['Prompt']) else r['Response'],axis=1)

    df.to_excel(output_path, index=False)
    df.head()