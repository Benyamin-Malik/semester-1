import random
with open("week1.8/session1/task1-random/random.txt","w") as outfile:
# Get user to input how many random numbers they want
 num_of_rand=int(input("How many random numbers do you eish to generate"))

rng_list=[]
for i in range(1,num_of_rand+1):
    a=random.randint(0,1000)
    rng_list.append(a)

for k in rng_list:
     outfile.write(k)
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line

                                                                           