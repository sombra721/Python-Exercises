'''
The script will detect if the regular expression pattern is contained in the files in the directory and it's sub-directory.

Suppose the directory structure is shown as below:

    test
    |---sub1
    |   |---1.txt (contains)
    |   |---2.txt (does not contain)
    |   |---3.txt (contains)
    |---sub2
    |   |---1.txt (contains)
    |   |---2.txt (contains)
    |   |---3.txt (contains)
    |---sub3
    |---|---sub3-1

The result will be: {"sub1": 2, "sub2": 3,"sub3": 0,"sub3\sub3-1": 0}

Running the script with the two arguments:
1. Tha path to be traversal.
2. Ragular Expression pattern.

e.g.:
python re_traversal.py C:/test ("^[a-zA-Z]+_TESTResult.*") 

'''
import sys
import os
import re
import pylab

def draw_graph(result):
    names = result.keys()
    counts = result.values()
    pylab.xticks(range(len(names)), names)
    pylab.plot(range(len(names)), counts, "b")
    pylab.show()    
    
def main(argv):
    result = {}
    for path, subdirs, files in os.walk(argv[1]):
        for subdir in subdirs:
            result[os.path.join(path, subdir)[len(argv[1])+1:]] = 0
        for name in files:
            if re.search(argv[2], open(os.path.join(path, name), 'r').read()):
                result[os.path.join(path, name)[len(argv[1])+1:-len(name)]] = result.get(os.path.join(path, name)[len(argv[1])+1:-len(name)], 0) + 1
    if result:
        print result
    else:
        print "No match detected."
    draw_graph(result)

if __name__ == '__main__':
    main(sys.argv)