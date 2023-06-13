#!/usr/bin/python3
""" 
Module to print status codes. 

"""
import sys


class Magic:
    """ Class magic"""
    def __init__(self):
        """ Init method """
        self.dict = {}
        self.size = 0

    def init_dict(self):
        """ Initialize dict """
        self.dict['200'] = 0
        self.dict['301'] = 0
        self.dict['400'] = 0
        self.dict['401'] = 0
        self.dict['403'] = 0
        self.dict['404'] = 0
        self.dict['405'] = 0
        self.dict['500'] = 0

    def add_status_code(self, status):
        """ add repeated numbers to the status code """
        if status in self.dict:
            self.dict[status] += 1

    def print_info(self, sig=0, frame=0):
        """ print status code """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dict.keys()):
            if self.dict[key] is not 0:
                print("{}: {:d}".format(key, self.dict[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dict()
    n_lines = 0

    try:
        for line in sys.stdin:
            if n_lines % 10 == 0 and n_lines is not 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except:
                pass
            n_lines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()
