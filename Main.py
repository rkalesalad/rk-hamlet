###rk!!
def make_lists():
  with open("hamlet.txt") as hamlet:
    text = hamlet.read() 
    global script_list 
    script_list = text.splitlines() 
    global actor_list 
    actor_list = []
  for i in range(len(script_list)):
    check = script_list[i] 
    if check == check.upper() and check not in actor_list and "SCENE" not in check and "ACT" not in check and ":" not in check: # removes all values that aren't a character name from the list, since all "uppercase" words are either a name or stage direction
      actor_list.append(check) 
  actor_list.remove('') 

def lines():
  lines = False 
  index = "" 
  global lines_list
  lines_list = [] 
  for i in range (len(actor_list)):
    lines_list.append(0) 
  for i in range (len(script_list)):
    if script_list[i] in actor_list:
      lines = True 
      index = actor_list.index(script_list[i]) 
    elif lines == True and script_list[i] != "" and "Exit" not in script_list[i] and "Enter" not in script_list[i]:
      lines_list[index] += 1 

def display():
  end_dict = dict(zip(actor_list, lines_list)) 
  end_dict = sorted(end_dict.items(), key = lambda item: item[1], reverse = True) 
  final_dict = {}
  print("Found " + str(len(actor_list)) + " unique actors ...") 
  for key, value in end_dict:
    final_dict[key] = value
  print("""
  Rank  Actor                         Lines
    _____________________________________""") 
  for i in range(len(final_dict)): 
    print("    {:<6}{:<28}{:<20}".format(i+1, list(final_dict)[i].title(), final_dict.get(list(final_dict)[i])))

def order():
    print("Initializing ...")
    make_lists()
    lines()
    display()

if __name__ == "__main__": 
  order()
