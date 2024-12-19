import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates
    unique_salaries = employee['salary'].drop_duplicates()

    # Sort the unique salaries in descending order and obtain the second highest value
    if len(unique_salaries) >= 2:
        second_highest = unique_salaries.nlargest(2).iloc[-1]
    else:
        second_highest = None
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})