#!//home/asdf/temp/p3/bin/python3
from ete3 import Tree, TreeStyle


class Node3:
  def __init__(self, c, nodes):
    # Content = Buchstabe
    self.c = c
    self.nodes = nodes
    self.end1 = 0

def create_suffix_list(str1):
  l = []
  for i in range(0, len(str1)):
    l.append(str1[i:])
  return l

def node_copy(node):
  if node is None:
    return node
  node1 = Node3(node.c, [])
  for i in range(0, len(node.nodes)):
    node1.nodes.append(node.nodes[i])
  return node1

def tree2postfix2(r, s):
  len1 = len(r.nodes)
  for i in range(0, len1):
    if (i == 0):
      s.append("(")
    tree2postfix2(r.nodes[i], s)
    if (i == len1-1):
      s.append(r.nodes[i].c + ")")
    else:
      s.append(r.nodes[i].c + ",")

def check_if_inside(c, node):
  for i in range(0, len(node.nodes)):
    if node.nodes[i].c == c:
      #print("found char")
      return [True, i] # Found position
  
  # Did not found position, 
  # give you hint where it should be
  #print("didnt find char")
  pos = 0
  for i in range(0, len(node.nodes)):
    #print(c + "<" + node.nodes[i].c)
    if c > node.nodes[i].c:
      pos += 1
  return [False, pos]

def insert(root, key):
  curr = root
  for c in key:
    found, pos = check_if_inside(c, curr)
    #print(found, pos)
    if not(found):
      new_node = Node3(c, [])
      curr.nodes.insert(pos, new_node)
      pos = len(curr.nodes) - 1
    curr = curr.nodes[pos]
  curr.end1 = True


if 1==2:
  root = Node3("", [])
  #l = ['abc', 'acb', 'ade', 'aaa', 'b']
  l = ["and", "ant", "do", "geek", "dad", "ball", "abcd", "ddb", "dda", "bbad"]

  for i in l:
    insert(root, i)

  # Copy
  root2 = node_copy(root)

  s = []
  tree2postfix2(root, s)
  s = ''.join(s)+";"
  print(s)

  t = Tree(s, format=1)
  print(t.get_ascii(show_internal=True))




l = create_suffix_list('banana$')
for j in range(1, len(l)):
  root = Node3("", [])
  for i in l[0:j]:
    insert(root, i)

  s = []
  tree2postfix2(root, s)
  s = ''.join(s)+";"

  t = Tree(s, format=1)
  print(t.get_ascii(show_internal=True))
