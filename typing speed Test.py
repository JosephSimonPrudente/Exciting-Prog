from time import time # record the time 

# calculate the accuracy of input prompt
def tperror(prompt):
    global inwords 

    words = prompt.split()
    error = 0

    for i in range (len (inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words [i]:
                continue
            else:
                errors = errors + 1
        else: 
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1 
            else:
                errors += 1
    return error

# calculate the speed of typing words per minute 
def speed(inprompt, stime, etime):
    global time 
    global inwords 

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time 

    return speed 

# calculate hte total elapsed time 
def elapsedtiem(stime, etime):
    time = etime - stime # etime is the end time and stime is the start time 
    return time 

# this was the paragraph which you have you have to type to check your speed
if __name__ == '__main__':
    prompt = "Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing."
    print("Type this:-",prompt)

#Checking to input   
    print()
    input("*****Press enter when your ready to check your speed*****:")
    print()

