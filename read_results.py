import csv
import sys

def read_single_result():
    """ Function to read a single result
        Returns a tuple of:
            table1, table2, p1, p2, runtime
        as strings
    """
    # TODO: your code here
    # example return values
    return "some_table1", "some_table2", "p1", "p2", "runtime"

def parse_results(csvfilename):
    """ Main function. Should read all results from 'simple_results' and output them to a
        given CSV file. It will create the file if it doesn't exist.
    """
    # open a CSV file ready for writing
    with open(csvfilename, 'w', newline='') as csvfile:
        # create a writer object
        writer = csv.writer(csvfile)

        # TODO: Write a header row

        # we don't know how long the input is going to be, so we use a while True (forever)
        # we can break when we reach the end of the input. Python will raise an EOFError for us here
        while True:
            try:
                # call our function
                line = read_single_result()
            except EOFError:
                # end of file
                break

        # examples of writing a row 8< ========= TODO: delete these lines
        # sample_row = ("a", "b", "c", "d")
        # writer.writerow(sample_row)

        # sample_2 = read_single_result()
        # writer.writerow(sample_row)
        # ============= >8


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <outputfile.csv>")
        sys.exit(1)
    parse_results(sys.argv[1])
