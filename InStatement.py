print ("using in statement")

testphrase = "to be or not be that is the question whether be tis nobler be in the mind to be suffer the slings and be arrows of outrageous be fortune"

# split out the phrase into constituent words
splittestphrase = testphrase.split()
testword = "be"

# print out the split phrase
print splittestphrase

count = 1

# go through each word and see if it matches the testword
for word in splittestphrase:
    if word == testword:
        print ("found: ", testword, "number:", count)
        count = count + 1
