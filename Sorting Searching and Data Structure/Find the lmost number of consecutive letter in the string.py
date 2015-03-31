import unittest

a = "aabbbbbssettttttttttttttttttttgeeeeeeeeeeeee"

def FindMostLengthCharac(string):
    
    #a = raw_input("Enter something: ")
    result = ''
    count = 1
    max_count = 0
    for i in range(0, len(string)-1):
        if((string[i] == string[i+1]) and (i != (len(string)-2))):
            count = count + 1
            #print count
        else:
            if(count > max_count):
                result = string[i]
                max_count = count
                #print count, max_count, result
            #print "not the same", a[i]
            count = 1
            
    print "The character has the most adjunct length is ", result
    return result
    
FindMostLengthCharac(a)
FindMostLengthCharac("aacccddbbbbbbbbbkkoka")

class TestFMC(unittest.TestCase):
    def testOne(self):
        self.assertEqual('b', FindMostLengthCharac("aacccddbbbbbbbbbkkoka"))
    def testTwo(self):
        self.assertEqual('t', FindMostLengthCharac("aacccddbbbbbbbkktttttttttttttttttttttttelsa"))

if __name__ == "__main__":
    unittest.main()