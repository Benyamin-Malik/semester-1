# Worksheet 1.3: Task 1

L = int(input("Length of sequence:")) # this should be your only input
k=0
ak=0
sequence=list()
# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

while len(sequence)<L :
    k=k+1
    if (ak-k)>0 and (ak-k) not in sequence :
        ak=ak-k
    else:
      ak=ak+k

    sequence.append(ak)
        
print(sequence)
        

# You may wish to use further output for testing purposes while you develop your code

#[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence