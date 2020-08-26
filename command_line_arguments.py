import argparse


def check_if_update():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l")
    parser.add_argument("-p")
    args = parser.parse_args()
    return args
