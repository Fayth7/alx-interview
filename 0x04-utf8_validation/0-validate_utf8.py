#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a given data set is a valid UTF-8 encoding.

    Args:
    - data: List of integers representing 1-byte data

    Returns:
    - True if data is a valid UTF-8 encoding, else False
    """
    # Variable to keep track of the number of expected following bytes
    expected_following_bytes = 0

    for byte in data:
        if expected_following_bytes == 0:
            if byte >> 7 == 0:
                # 1-byte character
                expected_following_bytes = 0
            elif byte >> 5 == 0b110:
                # 2-byte character
                expected_following_bytes = 1
            elif byte >> 4 == 0b1110:
                # 3-byte character
                expected_following_bytes = 2
            elif byte >> 3 == 0b11110:
                # 4-byte character
                expected_following_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a following byte
            if byte >> 6 != 0b10:
                return False

            # Decrease the count of expected following bytes
            expected_following_bytes -= 1

    # Check if all expected following bytes have been found
    return expected_following_bytes == 0
