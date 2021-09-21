from typing import Optional


def fix_value(value: str) -> Optional[float]:
    """Fixes value.
    If value represents -, returns None. If % in value, deletes it.

    Arguments:
        value: value to fix

    Returns:
        fixed value
    """

    if value == '-':
        return None

    value = value.replace('%', '')

    return float(value)
