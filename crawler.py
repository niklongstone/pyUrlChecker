#!/usr/bin/python

import sys, getopt, os.path, urllib2, socket

def main(argv):
    inputfile = ''
    outputfile = 'log.txt'
    timeout = ''


    try:
      opts, args = getopt.getopt(argv,"hi:o:t:", ["help", "ifile=", "ofile=", "timeout="])
    except getopt.GetoptError:
      print '-i <inputfile> -t <timeout>'
      sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'crawler.py -i <urlfile> -o <outputlog> -t <timeout>'
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t", "--timeout"):
            timeout = arg
        else:
            print 'error parsing command'

    if os.path.isfile(inputfile):
        readFileLines(inputfile, outputfile, timeout)
    else: 
        print "input file doesn't exists"

def readFileLines(inputfile, outputfile, timeout):
    socket.setdefaulttimeout(float(timeout))
    fout = open(outputfile, 'w') 
    count = 0

    with open(inputfile) as f:
        count+=1
        rows = f.readlines()
        #numLines = len(rows)

        for row in rows:
            req = urllib2.Request('http://www.google.it')
            status = urllib2.urlopen(req).getcode()
            outstring =  str(row).rstrip("\n") + ' | status: ' + str(status) + "\n"
            print outstring.rstrip("\n")
            fout.write(outstring) 
            #print str((count*1.0)/numLines*100) + '%'

if __name__ == "__main__":
    main(sys.argv[1:])
