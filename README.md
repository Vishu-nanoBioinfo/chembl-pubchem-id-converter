# chembl-pubchem-id-converter
This code is a Python script designed to convert a list of CHEMBL codes into PubChem CIDs by using the PubChemPy library.

CHEMBL to PubChem CID Converter

This script converts CHEMBL codes to PubChem CIDs using the PubChemPy library, allowing users to map CHEMBL IDs to PubChem database identifiers easily. The conversion results are saved to a new CSV file, making it a handy tool for chemical and bioinformatics research.
Features

    Reads CHEMBL codes from a CSV file.
    Converts each CHEMBL code to the corresponding PubChem CID.
    Provides real-time progress updates as each code is processed.
    Saves the results in a new CSV file with CHEMBL codes and their respective PubChem CIDs.

Requirements

    Python 3.x
    Libraries:
        pandas
        pubchempy

Installation

    Clone the repository:

git clone https://github.com/yourusername/chembl-to-pubchem-cid.git
cd chembl-to-pubchem-cid

Install the required packages:

    pip install pandas pubchempy

Usage

    Prepare your Input CSV:
        The input file (molecules.csv) should contain a column with CHEMBL codes.
        Update the chembl_column_name in the script if the CHEMBL code column in your file has a different name.

    Run the Script: python convert_chembl.py
    
Output:

    The script will create a new CSV file, chembl_to_pubchem_cids.csv, containing the original CHEMBL codes and their mapped PubChem CIDs.
    Progress updates will be printed in the console to monitor the conversion process.

Example
If your molecules.csv looks like this:
CHEMBL_Code

CHEMBL2414773

CHEMBL2063273

The output CSV (chembl_to_pubchem_cids.csv) will be:
CHEMBL_Code	PubChem_CID

CHEMBL2414773	123456

CHEMBL2063273	654321



Error Handling
The script handles errors gracefully, printing an error message if a CHEMBL code cannot be converted.


License
This project is licensed under the MIT License.


Acknowledgments
This script uses the PubChemPy library to interact with the PubChem database.
