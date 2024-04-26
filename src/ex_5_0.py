"""ex_5_0.py"""


def line_count(infile):
    """
       Count the number of lines in the given file and print the count to the console.

       Args:
       - infile (str): The name of the input file.

       Returns:
       - None
       """
    with open(infile, 'r') as file:
        lines = file.readlines()
        count = len(lines)
        print(f"Number of lines in {infile}: {count}")
    pass



if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
