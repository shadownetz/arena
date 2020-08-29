"""
This contains functions returning objects of various constants
"""


def sort_according_second_index(val):
    return val[1]


def countries():
    """
    function returning list of all countries globally
    :return: tuple object
    """
    content = [
        ('Nigeria', 'NIGERIA')
    ]
    content.sort(key=sort_according_second_index)

    return content


def states():
    """
    function returning list of all countries globally
    :return: tuple object
    """

    content = [
        ('Lagos', 'LAGOS'),
        ('Abia', 'ABIA'),
        ('Enugu', 'ENUGU'),
    ]
    content.sort(key=sort_according_second_index)
    return content
