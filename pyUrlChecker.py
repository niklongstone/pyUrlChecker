#!/usr/bin/python

import sys, getopt, os.path, urllib2, socket
import argparse

def main(argv):
    inputfile = ''
    outputfile = 'log.txt'
    timeout = ''

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="inputfile", required=True, help="path of the input file with urls lists")
    parser.add_argument("-o", dest="outputfile", default="out.txt", help="path of the output log file, default out.txt")
    parser.add_argument("-t", dest="timeout", default=10, help="timeout for the response in second, default 10")
    parser.add_argument("-cookie", dest="cookie", default=None, help="add cookie sessioni to header")
    parser.add_argument("-v", action='store_true', dest="verbose", default=False, help="verbose mode, shows the output of the request")

    args = parser.parse_args()

    if os.path.isfile(args.inputfile):
        readFileLines(args.inputfile, args.outputfile, args.timeout, args.cookie, args.verbose)
    else: 
        print "input file doesn't exists"

def readFileLines(inputfile, outputfile, timeout, cookie, verbose):
    socket.setdefaulttimeout(float(timeout))
    fout = open(outputfile, 'w') 
    count = 0

    with open(inputfile) as f:
        count+=1
        rows = f.readlines()
        
        for row in rows:
            req = urllib2.Request(row)
            if cookie:
                print "cookie present"
                req.add_header("Cookie", cookie);
            openUrl = urllib2.urlopen(req)
            openUrl.read()
            status = openUrl.getcode()
            outstring =  str(row).rstrip("\n") + ' | status: ' + str(status) + "\n"
            if (verbose):
                print outstring.rstrip("\n")
            fout.write(outstring) 

if __name__ == "__main__":
    main(sys.argv[1:])
