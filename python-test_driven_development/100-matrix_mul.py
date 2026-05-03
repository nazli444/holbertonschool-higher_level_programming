#!/usr/bin/python3
"""
Matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b
    """

    # Validate type: must be list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate list of lists
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate empty matrices
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Validate elements type (int or float)
    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Validate rectangular shape
    row_len_a = len(m_a[0])
    if any(len(row) != row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if any(len(row) != row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize result matrix
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_b)):
                value += m_a[i][k] * m_b[k][j]
            new_row.append(value)
        result.append(new_row)

    return result
