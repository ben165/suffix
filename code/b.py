class Node1:
  def __init__(self, c, nodes):
    self.c = c
    self.nodes = nodes
    self.end1 = 0

class Node2:
  def __init__(self, c):
    self.c = c

    self.nodes = []
    for i in range(0, 26):
      self.nodes.append(None)



# LVR Inorder
def inorder(node, list1):
  if (node != None): # && node.value != null
    for i in range(0, len(node.nodes)):
      inorder(node.nodes[i], list1)
      list1.append(node.c)
    #inorder(node.l, list1)
    #list1.push(node.value)
    #inorder(node.r, list1)



# geht vermutlich nicht?
def breitensuche(node, list1):
  queue = []
      
  if (node != None):
    queue.push(node)
    
  while ( queue.length != 0 ):
    temp = queue.splice(0,1)[0]
    list1.push( temp.value )
  
    if (temp.l != None):
      queue.push(temp.l)
    if (temp.r != None):
      queue.push(temp.r)


if (1==2):
  #list1 = ['bear', 'bell', 'bid', 'bull', 'stock', 'stop']
  list1 = ['bear', 'bell']
  
  root = Node2("root")
  for i in range(0, len(list1)):
    for j in range(0, len(list1[i])):
      #print(list1[i][j], end="")
      nr = ord( list1[i][j] ) - 97
      if root.nodes[nr] == None:
        print(list1[i][j] + " Char not found")
  
    print()



if 1==1:
  a0 = Node1("e", [])

  a1 = Node1("mize", [])
  a2 = Node1("nimize", [])
  a3 = Node1("ze", [])

  a4 = Node1("nimize", [])
  a5 = Node1("ze", [])

  a6 = Node1("nimize", [])

  a7 = Node1("ze", [])

  a8 = Node1("i", [a1, a2, a3])
  a9 = Node1("mi", [a4, a5])

  r = Node1("", [a0, a8, a9, a6, a7])


#list1 = []
#inorder(r, list1)
#print(list1)


def meins(node, list1):
  queue = []
  # Fuege erste Reihe hinzu
  for i in range(0, len(node.nodes)):
    if node.nodes[i] != None:
      queue.append( node.nodes[i] )
  # Plotte Baum
  
  # Fuege zweite Reihe hinzu
  for i in range(0, len(queue)):
    pass
    

# https://www.geeksforgeeks.org/trie-insert-and-search/


class TrieNode:
    def __init__(self):
        # Array for child nodes of each node
        self.child = [None] * 26
        
        # for end of word
        self.word_end = False

# Method to insert a key into the Trie
def insert_key(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:

            # If node for current character does 
            # not exist then make a new node
            new_node = TrieNode()

            # Keep the reference for the newly
            # created node
            curr.child[index] = new_node

        # Move the curr pointer to the
        # newly created node
        curr = curr.child[index]

    # Mark the end of the word
    curr.word_end = True

# Method to search a key in the Trie
def search_key(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False

        # Move the curr pointer to the 
        # already existing node for the 
        # current character
        curr = curr.child[index]

    # Return true if the word exists 
    # and is marked as ending
    return curr.word_end

# Create an example Trie
root = TrieNode()
arr = ["and", "ant", "do", "geek", "dad", "ball"]
for s in arr:
  insert_key(root, s)

if 1==2:
  # One by one search strings
  search_keys = ["do", "gee", "bat"]
  for s in search_keys:
    print(f"Key : {s}")
    if search_key(root, s):
      print("Present")
    else:
      print("Not Present")

# Print tree
#def tree2postfix(r):
#  for i in range(0, len(r.child)):
#    if r.child[i] != None:
#      print(chr(i))
#      tree2postfix(i)

def tree2postfix(r):
  for i in range(0, len(r.child)):
    if r.child[i] != None:
      #print(r.child[i])
      print(chr(ord('a')+ i))
      #print(r.child[i].word_end)
      
      if r.child[i].word_end:
        print()
      
      tree2postfix(r.child[i])
#print( len(root.child) )

    

#tree2postfix(root)


