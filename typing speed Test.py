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



