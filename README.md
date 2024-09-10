CER Calculation and Data Comparison

This repository contains a Python script for calculating the Character Error Rate (CER) between reference data and hypothesis data. The script utilizes two methods to calculate the Levenshtein distance: one based on dynamic programming and another using Python's difflib.ndiff. The calculated CER values are then stored in an Excel sheet.
Repository Structure

bash

├── 데이터(네이버)_유니바api저장_ver1.1.xlsx  # Input Excel file with original and hypothesis data  

├── cer_calculation.py                        # Main script for CER calculation  

└── output_데이터(네이버)_유니바api저장_ver1.1.xlsx  # Output Excel file with calculated CER values  


Requirements

    Python 3.x
    Pandas (pip install pandas)
    NumPy (pip install numpy)
    openpyxl (pip install openpyxl)

How the Script Works
1. Levenshtein Distance

The script provides two methods to calculate the Levenshtein distance between two text sequences:

    levenshtein_distance_ndiff: Uses Python's difflib.ndiff to calculate the number of insertions, deletions, and substitutions.
    levenshtein_distance_dp: Uses a dynamic programming approach to calculate the minimal number of edits required to transform one string into another.

2. Character Error Rate (CER) Calculation

The calculate_cer function computes the Character Error Rate (CER), which is the ratio of the Levenshtein distance between the reference and hypothesis texts to the total number of characters in the reference text.
3. Excel File Processing

The script:

    Reads an Excel file (데이터(네이버)_유니바api저장_ver1.1.xlsx), specifically the sheet named WEB&CER(115).
    Compares two different sets of hypothesis data against the reference data (columns univaResult and univaResult(2024)).
    Calculates the CER for both comparisons and stores the results in columns P and Q of the same sheet.
    Saves the output to a new Excel file.

How to Run the Script

    Install the required Python libraries:

    bash

pip install pandas numpy openpyxl

Place the input Excel file (데이터(네이버)_유니바api저장_ver1.1.xlsx) in the same directory as the script.

Run the script:

bash

    python cer_calculation.py

    The script will:
        Read data from the WEB&CER(115) sheet of the Excel file.
        Calculate the CER between the "Origin Data" column and two different hypothesis columns: univaResult and univaResult(2024).
        Write the CER values to columns P and Q, respectively.
        Save the result to output_데이터(네이버)_유니바api저장_ver1.1.xlsx.

Input/Output Data

    Input File: 데이터(네이버)_유니바api저장_ver1.1.xlsx
        Origin Data: The reference text data.
        univaResult: Hypothesis data for comparison in 2023.
        univaResult(2024): Hypothesis data for comparison in 2024.

    Output File: output_데이터(네이버)_유니바api저장_ver1.1.xlsx
        P column: CER between Origin Data and univaResult.
        Q column: CER between Origin Data and univaResult(2024).

License

This project is licensed under the MIT License - see the LICENSE file for details.
