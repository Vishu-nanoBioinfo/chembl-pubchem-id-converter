import pandas as pd
import pubchempy as pcp

# Load the CSV file containing CHEMBL codes
file_path = 'molecules.csv'
data = pd.read_csv(file_path)

# Specify the column name that contains the CHEMBL codes
chembl_column_name = 'CHEMBL_Code'  

# Prepare an empty list to store results
results = []

# Function to convert CHEMBL ID to PubChem CID using PubChemPy
def get_pubchem_cid(chembl_code):
    try:
        # Use PubChemPy to search by name
        compound = pcp.get_compounds(chembl_code, 'name')
        
        # If a compound is found, return the CID
        if compound:
            return compound[0].cid
        else:
            return None
    except Exception as e:
        print(f"Error fetching PubChem CID for {chembl_code}: {e}")
        return None

# Loop through each CHEMBL code, convert to PubChem CID, and store results
for index, chembl_code in enumerate(data[chembl_column_name], start=1):
    pubchem_cid = get_pubchem_cid(chembl_code)
    results.append({
        "CHEMBL_Code": chembl_code,
        "PubChem_CID": pubchem_cid
    })
    
    # Print progress update
    print(f"Processed {index}/{len(data)}: CHEMBL_Code={chembl_code}, PubChem_CID={pubchem_cid}")

# Convert the results to a DataFrame and save to a new CSV file
output_df = pd.DataFrame(results)
output_path = 'chembl_to_pubchem_cids.csv'
output_df.to_csv(output_path, index=False)

print(f"Conversion complete. Data has been saved to {output_path}")
