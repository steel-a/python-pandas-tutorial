# Function without parameter
def showLine():
    """
    -> Show a line with size 40
    """
    print('-' * 40)


# Function with parameter
def showTitle(title):
    """
    -> Show a title in center between lines with size 40
    :param title: Title to show
    """
    showLine()
    print(f'{title:^40}')
    showLine()