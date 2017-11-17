import sys
import getopt


def run():
    opts, args = getopt.getopt(sys.argv[1:], "hi:t:", ["version", "file="])
    input_file = ""
    output_file = ""
    print opts, args
    for op, value in opts:
        if op == "-i":
            input_file = value
        elif op == "-t":
            output_file = value
        elif op == "-h":
            usage()
            sys.exit()
    print input_file, output_file


def usage():
    pass


if __name__ == "__main__":
    run()
