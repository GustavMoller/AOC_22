import numpy as np

def text_parser(filepath: str, return_chunks=True, detect_integers=True, return_array=False) -> list:
    """Returns a list of strings corresponding to each line of the input file

    Args:
        filepath (str): filepath to .txt file

    Returns:
        list: list of strings corresponding to each line of the input file

    Future functionality:
        - Add casting to ints
        - Add casting to numpy arrays
        - Detect chunks separated by '' 
    """

    data = open(f'inputs/{filepath}', 'r').read().split('\n')
    
    
    return data