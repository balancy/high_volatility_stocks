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

    if value == '-':
        return None

    if value[-1] == '%':
        value = value[:-1]

    if 'on' in value or not value[-1].isdigit():
        return value

    if ',' in value:
        return int(value.replace(',', ''))

    return float(value)


def get_modified_key(key: str) -> str:
    """Modifies the key for db field.
    DB fields couldn't contain spaces and the symbol /. Function modifies keys
    received from parsing to DB fields format.

    Arguments:
        key: key_to_modify

    Returns:
        modified_key
    """

    return key.lower().replace(' ', '__').replace('/', '_')


def get_modified_data(data: list) -> list:
    """Modify data to be in corresponding to db records form.
    It modifies keys to be correct field names of db model and fixes values.

    Arguments:
        data: data containing values and keys to fix

    Returns:
        modified data
    """

    modified_data = list()

    for record in data:
        modified_data.append(
            {
                get_modified_key(key): fix_value(value)
                for key, value in record.items()
            }
        )

    return modified_data
