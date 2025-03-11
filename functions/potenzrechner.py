from utils import helpers

def calculate_exponentiation(base, exponent, timezone='Europe/Zurich'):
    """
    Calculate the exponentiation and return a dictionary with inputs, result, and timestamp.

    Args:
        base (float): The base value.
        exponent (float): The exponent value.

    Returns:
        dict: A dictionary containing the inputs, calculated exponentiation, and timestamp.
    """
    result = base ** exponent

    return {
        "timestamp": helpers.ch_now(),
        "base": base,
        "exponent": exponent,
        "exponentiation": result,
    }