from typing import List
from logging import getLogger
from EUIVManagement.helpers import timeit

logger = getLogger(__name__)


@timeit
def parse_save_game_lines(lines: List[str]) -> dict:
    """
    Function to parse .eu4 files with a wrapper that check the execution time
    :param lines:
    :return:
    """

    final_dict = parse_lines(lines[1:])
    return final_dict


def parse_lines(lines: List[str]) -> dict:
    """
    Function to parse lines raw lines into a dict

    It will return a dict with all the raw information of the file.
    :param lines:
    :return:
    """
    common_keys = []
    return_dict = {}

    reading_dict = False
    total_brackets = 0
    dict_lines = []
    list_values = []

    key = ''

    not_named_keys_counter = 0
    replaced_value = False  # For the special case {{

    for line in lines:
        # Remove not necessary characters
        line = line.replace('\n', '')
        line = line.replace('\t', '')
        line = line.replace('\b', '')
        if line == '':
            continue

        # Check if is a special case where key-value are not like key={...
        if '{' in line and line != '{' and '={' not in line:
            line = line.replace('{', '={')

        # Case 0
        if '={' in line and '}' in line:
            line = line.replace('}', '')
            special_line = line.split('{')
            dict_lines.append(f"{special_line[0]}{{")
            dict_lines.append(special_line[1])
            dict_lines.append('}')

        # Case 1
        elif '={' in line:
            reading_dict = True
            total_brackets += 1
            if '{{' in line:
                total_brackets += 1
                line = line.replace('{{', '{')
                replaced_value = True

            # Only get the key of the actual dict
            if total_brackets == 1:
                key = line.replace('={', '')
                if key in common_keys:
                    key = f"{key}_{len(common_keys)}"
                common_keys.append(key)
            else:
                dict_lines.append(line)

            # Special case where 2 { in one
            if replaced_value:
                special_key = line.replace('={', '')
                dict_lines.append(f'{special_key}={{')
                replaced_value = False

            continue

        # total_brackets should decrease
        elif '}' in line:
            total_brackets -= 1

            # Should be VALUE }
            lines_to_append = line.split('}')
            lines_to_append.extend('}')

            # End of dict
            if total_brackets == 0:
                reading_dict = False

                # Check if is a dict of not named dicts
                try:
                    return_dict[key] = parse_lines(dict_lines)
                except Exception as ex:
                    logger.error(f"Error processing line '{line}'", exc_info=ex)

                    raise ex

                # Clear the dict lines for new dictionaries
                dict_lines.clear()
            else:
                dict_lines.extend(lines_to_append)

        elif reading_dict:
            if line == '{':
                total_brackets += 1
                line = f"{key}_{not_named_keys_counter}={{"
                not_named_keys_counter += 1
            dict_lines.append(line)

        # Case 2
        elif '=' in line:
            # Check if multiple =
            if line.count('=') == 1:
                key, value = line.split('=')
                try:
                    return_dict[key] = value
                except Exception as ex:
                    logger.info(f'There is a problem processing line {line}')
                    raise ex
            else:
                dict_lines.extend(line.split())

        else:
            list_values.append(line.replace('"', ''))
            return_dict = list_values
    return return_dict
