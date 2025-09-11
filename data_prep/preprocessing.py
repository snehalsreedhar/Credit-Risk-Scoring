from credit_risk_scoring.data_prep import data_loader
import pandas as pd
import numpy as np

def preprocessor() -> pd.DataFrame:
    """Preprocess the loan data for modeling."""
    df = data_loader.load_loan_data()
    columns_to_keep = ['loan_amnt', 'int_rate', 'installment', 'grade', 'emp_length', 'home_ownership', 'annual_inc',
                        'loan_status', 'purpose']
    loan_df = df[columns_to_keep]

    # Calculating loan amount as a percentage of income
    loan_df['loan_percent_income'] = loan_df['loan_amnt'] / loan_df['annual_inc']

    # Renaming columns for better readability
    loan_df.columns = ['loan_amnt', 'loan_int_rate', 'installment', 'loan_grade', 'person_emp_length', 
                    'person_home_ownership', 'person_income', 'loan_status', 'loan_intent', 'loan_percent_income']

    # Creating a new column for age based on random values
    loan_df['person_age'] = np.random.randint(18, 110, loan_df.shape[0])

    # Coverting the loan status to a binary variable
    loan_df['loan_status'] = loan_df['loan_status'].map({'Current': 1,'Fully Paid': 1, 'Late (31-120 days)' : 0, 
                                                        'Charged Off': 0, 'In Grace Period': 0,
                                                          'Does not meet the credit policy. Status:Fully Paid': 1, 
                                                        'Does not meet the credit policy. Status:Charged Off': 0, 'Default': 0})

    loan_df.dropna(subset=['loan_status', 'loan_int_rate', 'person_emp_length', 'person_income'], inplace=True)

    loan_df['cb_person_cred_hist_length'] = np.random.randint(0, 30, loan_df.shape[0])

    # Extracting the number of years from the employment length column
    loan_df['person_emp_length'] = loan_df['person_emp_length'].str.extract(r'(\d+)')
    loan_df.dropna(subset=['person_emp_length'], inplace=True)
    loan_df['person_emp_length'] = loan_df['person_emp_length'].astype(int)

    # Use Pandas to drop the record from the data frame and create a new one
    loan_df_new = loan_df.drop(loan_df[loan_df['person_income'] > 6*10**8].index)


    print(loan_df_new.head())    
    return loan_df_new




