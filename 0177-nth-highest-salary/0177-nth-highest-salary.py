import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_values = employee['salary'].drop_duplicates()

    if N < 1 or len(unique_values) < N:
        nth_highest = None
    else:
        nth_highest = unique_values.nlargest(N).iloc[-1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})