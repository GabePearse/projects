'''
This is a very simple polls system using functions
'''

def vote(inp):
 while True:
  inp = input("Cast your vote: ")
  if inp in ballot:
   ballot[inp] = ballot.get(inp,0) + 1
   print(inp, "has been voted for", ballot[inp], "times.")
   init()
  if inp == "Done":
   break
  if inp not in ballot:
   print(inp, "cannot be found inside of ballot. Please add to Ballot")
   init()

def check(inp):
  while True:
   inp = input("Please enter a Candidates name: ")
   if len(inp) == 0:
    print("Please enter a name")
    continue
   elif inp in ballot:
    print(inp, 'already in Ballot. Try "Vote" instead.')
    init()
    continue
   elif inp == "Done":
    break
   else:
    ballot[inp] = ballot.get(inp,0)
    print(inp, "has been added to the ballot.")
    init()

ballot = dict()
def init(): 
 while True:
  inp = input("What would you like to do?: ")
  inp = inp.upper()
  if inp == "ADD NEW":
   check(inp)
  elif inp == "VOTE":
   vote(inp)
   break
  elif inp == 'DONE':
   print("Final standing:")
   for k,v in ballot.items():
    print(k+':',v)
   exit()
  
  else:
   print("Please try again")
   continue


init()