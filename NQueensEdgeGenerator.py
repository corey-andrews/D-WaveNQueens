import threading

THREADS = 4

# Global variable to emulate return from multithreaded
# function
globalEdges = []
# Lock for safe threading of globalEdges edits
lock = threading.Lock()

def getEdges(dimension):
    # set up thread list and empty our global variable 
    # before using
    threadList = []
    globalEdges.clear()
    
    # Create the threads for each square that can have
    # a larger neighbor then pass them the thread function
    # and the args as a tuple
    for start in range(1, dimension**2):
        threadList.append(threading.Thread(target=edgeThread,
                                           args=(dimension, start)))

    # Begin then join all threads
    for thread in threadList:
        thread.start()    
    for thread in threadList:
        thread.join()

    # Return the graph that we generated
    return globalEdges

# Needs to return void as a threading function so we
# Give its return to a global variable
def edgeThread(dimension, start):
    # Generate all the edges from a starting square
    # that haven't been accounted for by another
    # square
    edges = []
    edges.extend(getRightEnds(dimension,start))
    edges.extend(getDLEnds(dimension, start))
    edges.extend(getDownEnds(dimension, start))
    edges.extend(getDREnds(dimension, start))
    with lock:
        globalEdges.extend(edges)

# Returns the edges to the rest of the horizontal row
def getRightEnds(dimension, start):
    # if we are at the end of the row, there are no 
    # squares to the right
    if(start % dimension == 0):
        return []

    # otherwise there get the rest of the row    
    edges = []
    # 1 + start//dimensions tells us which row we are on 
    # starting from row 1
    # multiplying that by dimension tells us the last square 
    # of the row
    # adding a further 1 accounts for range stopping short 
    # of its endpoint
    for i in range(start+1, dimension*(1 + start//dimension) + 1):
        edges.append((start, i))
    
    return edges

# Returns the edges to the rest of the column
def getDownEnds(dimension, start):
    # if we are on the bottom row return
    # start-1 prevents the end of a row being counted as part 
    # of the next row
    # /dimension + 1 tells us which row we are on
    # >= dimension tells us if we are on the last row 
    if((start-1)/dimension + 1 >= dimension):
        return []
    # otherwise get the rest of the column
    edges = []
    # start+dimension starts us on the row beneath us
    # dimension**2+1 ensures that we can get up to the bottom
    # right corner and not past it
    # dimension causes us to step to the next position in the column
    for i in range(start+dimension, dimension**2+1, dimension):
        edges.append((start, i))

    return edges

# Returns the edges along the down-left diagonal
def getDLEnds(dimension, start):
    edges = []
    # since we step at the beginning of the loop start with the end of 
    # our edge at the start 
    end = start
    while True:
        # step down a square and left a square
        end = end + dimension - 1
        # if we wrap around to the left or we go off the bottom
        # then we are done looping
        if(end%dimension == 0 or end//dimension >= dimension):
            break
        # append edge to list
        edges.append((start,end))

    return edges

# Returns the edges along the down-right diagonal
def getDREnds(dimension, start):
    edges = []
    # since we step at the beginning of the loop start with the end of 
    # our edge at the start 
    end = start
    while True:
        # step down a square and right a square
        end = end + dimension + 1
        # if we wrap around to the right or we go off the bottom
        # then we are done looping
        if(end%dimension == 1 or end > dimension**2):
            break
        # append edge to list
        edges.append((start,end))

    return edges