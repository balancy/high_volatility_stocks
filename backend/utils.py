from typing import Optional


def fix_value(value: str) -> Optional[float]:
    """Fixes value.
    If value represents -, returns None. If '%' or ',' in value, deletes it.
    If value contains on (like % on date), returns it as it is.

    Arguments:
        value: value to fix

    Returns:
        fixed value
    """

    value = value.strip()

    if 'on' in value:
        return value

    if value == '-':
        return None

    if ',' in value:
        return int(value.replace(',', ''))

    value = value.replace('%', '')

    return float(value)
