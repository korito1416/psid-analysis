"""
Statistical analysis functions for economics research
"""
import pandas as pd
import numpy as np
from typing import Dict, Union

def compute_moments(data: pd.Series, variable_name: str) -> Dict[str, float]:
    """
    Compute the first four moments of a statistical distribution.

    Your task: Implement this function to calculate:
    1. Mean (1st moment)
    2. Variance (2nd central moment) 
    3. Skewness (3rd standardized moment)
    4. Kurtosis (4th standardized moment)

    Args:
        data: A pandas Series containing the data
        variable_name: Name of the variable for reporting

    Returns:
        Dictionary with moment statistics

    Think about:
    - What do each of these moments tell us about the data distribution?
    - How would you interpret high skewness in earnings data?
    - What does kurtosis reveal about tail behavior?
    """

    # Remove any missing values
    clean_data = data.dropna()

    # TODO: Calculate each moment
    # Hint: pandas Series have methods like .mean(), .var(), .skew(), .kurtosis()
    # But try to understand what these actually compute!

    moments = {
        'count': len(clean_data),
        'mean': float(clean_data.mean()),
        'variance': float(clean_data.var(ddof=1)),   # sample variance
        'skewness': float(clean_data.skew()),        # sample skewness
        'kurtosis': float(clean_data.kurtosis())  
    }

    return moments

def analyze_variable(df: pd.DataFrame, column: str) -> None:
    """
    Print a formatted analysis of a variable.

    Your task: Complete this function to nicely display the moments
    """
    # TODO: Use compute_moments and format the output nicely
    pass