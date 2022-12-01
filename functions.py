import numpy as np

def text_parser(filepath: str) -> list:
    """_summary_

    Args:
        filepath (str): _description_

    Returns:
        list: _description_
    """

    data = open(f'inputs/{filepath}', 'r').read().split('\n')
    return data