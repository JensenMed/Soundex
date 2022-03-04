
##Jensen Medeiros(251234023)
## This algorithm completes the soundex encoding for user input. It then returns a list of what user inputs sound the same.



## Function that takes in user input
def inputCheck():
    data = []
    wordList = []
    name = None
    finish = "done"
    print("Enter names, one on each line. Type DONE to quit entering names.")
    while name != finish:
        name = input("")
        wordList.append(name)
        name = name.lower() ##---> Lowers data input
        newName = name.lower()

        data.append(newName)
    data = sorted(data[:-1])
    wordList = sorted(wordList[:-1])  ## --> Removes last variable(done) and sorts data
    loweredData = data[:]

    return data, wordList, loweredData




## Function that replaces letters with associated number

def letterReplace():
     loweredData, wordList, nameIndex = inputCheck()

     data2 = []


     ltrReplacment = {0: ["a", "e" ,"i" ,"o", "u", "y", "h", "w"],
            1: ["b", "f", "p", "v"],
            2: ["c", "g", "j", "k", "q", "s", "x", "z" ],  ## --> Dictonary for soundex
            3: ["d", "t"],
            4: ["l"],
            5: ["m", "n"],
            6: ['r']
            }


     for i in nameIndex:
         data2.append(i)


     for key, ltrs in ltrReplacment.items():
         for letter in ltrs:
             for i, z in enumerate(data2):
                 data2[i] = z.replace(letter, str(key))

     return data2, wordList, loweredData









## This function checks for no multiples

def noMultipleCheck():
    noMultiples, wordList, loweredData = letterReplace()


    ltrReplacment = {0: ["a", "e" ,"i" ,"o", "u", "y", "h", "w"],
            1: ["b", "f", "p", "v"],
            2: ["c", "g", "j", "k", "q", "s", "x", "z" ],
            3: ["d", "t"],
            4: ["l"],
            5: ["m", "n"],
            6: ['r']
            }


    data3 = loweredData[:]

    ### returns ["d"]
    for i, letters in enumerate(data3):
        data3[i] = letters[0]



    data4 = data3[:]

    ## returns ["0"]
    for keyz, ltrz in ltrReplacment.items():
         for ltr in ltrz:
             for z, lts in enumerate(data4):
                 data4[z] = lts.replace(ltr, str(keyz))

    for i, numbs in enumerate(noMultiples):
        noMultiples[i] = numbs[::-1]
        noMultiples[i] = ''.join(sorted(set(noMultiples[i]), key=noMultiples[i].index))   ## --> removes multiples
    for z, numz in enumerate(noMultiples):
        noMultiples[z] = numz[::-1]



    ##Replaces "0" with ""
    for inds, numbers in enumerate(noMultiples):
            noMultiples[inds] = numbers.replace("0", "")

    newLst = noMultiples[:]
    lst = []

    for i in newLst:
       lst.append(i[0])

    ## Makes soundex
    for a , b in enumerate(lst):
        if lst[a] == data4[a]:
            noMultiples[a] = data3[a] + noMultiples[a][1:]
            noMultiples[a] = ''.join(sorted(set(noMultiples[a]), key=noMultiples[a].index))
        elif lst[a] != data4[a]:
            noMultiples[a] = data3[a] + noMultiples[a]
            noMultiples[a] = ''.join(sorted(set(noMultiples[a]), key=noMultiples[a].index))
        else:
            noMultiples[a] = "0"
            noMultiples[a] = ''.join(sorted(set(noMultiples[a]), key=noMultiples[a].index))

    return wordList, noMultiples










## This function makes sure the length of the soundex is equal to 4

def lengthCheck():
    wordList , noMultiples = noMultipleCheck()


    for i, numbs in enumerate(noMultiples):
        if len(noMultiples[i]) >= 4:
            noMultiples[i] = noMultiples[i][:4]
        elif len(noMultiples[i]) < 4:
            noMultiples[i] = noMultiples[i].ljust(4, "0") ### --> adds 0 if not long enough


    return wordList, noMultiples





## The ovreall soundex check completes the steps 1-7

def overallSoundex():
    wordList, noMultiples = lengthCheck()




    newTuple = (wordList , noMultiples)


    return newTuple, wordList, noMultiples











## The main function calls on the  overall soundexcheck function and finds the words that hav ethe same overalll soundex encoding
def main():

    newTuple, wordList, noMultiples = overallSoundex()



    soundexLine = []
    newSet = set(noMultiples)

    indices = { value : [ i for i, v in enumerate(noMultiples) if v == value ]    ### ---> Finds Similar soundexs
            for value in newSet }

    for i, z in indices.items():
        if len(z) == 2:
            newlst = []
            newlst.append(wordList[z[0]])
            newlst.append(wordList[z[1]])
            new = sorted(newlst)
            soundexLine.append(f"{new[0]} and {new[1]} have the same Soundex encoding.")
        elif len(z) >= 3:
            newlst = []
            newlst.append(wordList[z[0]])
            newlst.append(wordList[z[1]])                           ### --> Goes through list and returns order of similar soundex
            newlst.append(wordList[z[2]])
            new = sorted(newlst)

            soundexLine.append(f"{new[0]} and {new[1]} have the same Soundex encoding.")


    for z in sorted(soundexLine):   ### Orders final outputs
        print(z)



main()





