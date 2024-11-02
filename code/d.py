#!//home/asdf/temp/p3/bin/python3
from ete3 import Tree, TreeStyle

class TrieNode:
  def __init__(self):
    # Array for child nodes of each node
    self.child = [None] * 26
    # for end of word
    self.word_end = False
  c = "" #Zusatz
  pos = "" #Zusatz

def create_suffix_list(str1):
  l = []
  for i in range(0, len(str1)):
    l.append(str1[i:])
  return l

def insert_key(root, key, nr):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        #print("INDEX: " + str(index))
        if curr.child[index] is None:
            new_node = TrieNode()
            new_node.c = c # Zusatz
            new_node.pos = nr
            curr.child[index] = new_node
        curr = curr.child[index]
    curr.word_end = True

def treeClean(r):
  try:
    for i in range(0, len(r.child)):
      if r.child[i] == None:
        r.child.pop(i)
      else:
        treeClean(r.child[i])
  except:
    pass

#def node_copy(node):
#  if node is None:
#    return node
#  node1 = Node3(node.c, [])
#  for i in range(0, len(node.nodes)):
#    node1.nodes.append(node.nodes[i])
#  return node1

def tree2postfix2(r, s):
  len1 = len(r.child)
  for i in range(0, len1):
    if (i == 0):
      s.append("(")
    tree2postfix2(r.child[i], s)
    if (i == len1-1):
      s.append(r.child[i].c + ")")
    else:
      #print(r.child[i].word_end)
      s.append(r.child[i].c + ",")


if 1==2:
  root = TrieNode()
  #l = ['abc', 'acb', 'ade', 'aaa', 'b']
  l = ["and", "ant", "do", "geek", "dad", "ball", "abcd", "ddb", "dda", "bbad"]

  for i in l:
    insert_key(root, i, str(0))
    
    s = []
    tree2postfix2(root, s)
    s = ''.join(s)+";"
    #print(s)
    t = Tree(s, format=1)
    print(i)
    print(t.get_ascii(show_internal=True))










if 1==2:
  #l = ['abc', 'acb', 'ade', 'aaa', 'b']
  #l = ["and", "ant", "do", "geek", "dad", "ball", "abcd", "ddb", "dda", "bbad"]

  #l = ["philip", "ida", "paul", "kevin", "simon", "jaqueline", "christian", "lukas", "lucas", "dominik", "marko", "philipp", "dominik", "jakob", "benjamin", "moritz",  "louis", "helal", "philipp", "ehsan", "carl"]

  l = ["bear", "bell", "bid", "bull", "stock", "stop"]

  for j in range(0, len(l)):
    root = TrieNode()
    for i in range(0, j+1):
      insert_key(root, l[i], "")

    for i in range(0, 10000):
      treeClean(root)

    s = []
    tree2postfix2(root, s)
    s = ''.join(s)+";"
    #print(s)
    t = Tree(s, format=1)
    print(l[j])
    print(t.get_ascii(show_internal=True))


if 1==1:
  l = create_suffix_list('bananaz')
  for j in range(0, len(l)):
    print(l[j:])
    root = TrieNode()
    for i in l[0:j]:
      insert_key(root, i, str(i))

    for i in range(0, 10000):
      treeClean(root)

    s = []
    tree2postfix2(root, s)
    s = ''.join(s)+";"

    t = Tree(s, format=1)
    print(t.get_ascii(show_internal=True))

if 1==2:
  root = TrieNode()
  l = create_suffix_list('bananaz')
  #l = create_suffix_list('catacatcaz')
  for j in range(0, len(l)):
    print( l[j], str(j) )
    insert_key(root, l[j], str(j))

  for i in range(0, 1000):
    treeClean(root)


  s = []
  tree2postfix2(root, s)
  s = ''.join(s)+";"
  t = Tree(s, format=1)
  print(t.get_ascii(show_internal=True))


#l = create_suffix_list('minimize$')
#for j in range(0, len(l)):
#  print( l[j] )



