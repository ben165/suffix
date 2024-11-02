#!/home/asdf/temp/p3/bin/python3

from ete3 import Tree, TreeStyle
#pip install PyQt5
#pip install --upgrade ete3

class Node:
  def __init__(self, c, nodes):
    self.c = c
    self.nodes = nodes
    self.end1 = 0
  info = ""

def tree2postfix(r):
  for i in r.nodes:
    tree2postfix(i)
  print(r.c, end=", ")


def tree2newick(r, str1):
  #
  # Postfix
  # ( = beim runtergehen, linkeste node
  # , = beim rausgehen - stimmt aber nicht wenn es zum vater geht
  # ) = wenn man zum Vater geht
  #
  len1 = len(r.nodes)
  for i in range(0, len1):
    #print(r.nodes[i].c + "   len: " + str(len1))
    if len1 == 1:
      #print("hallo", end="")
      str1.append("(")
      r.nodes[i].end1 = 1
    elif i == 0:
      #print("(", end="")
      str1.append("(")
    elif i == len1-1:
      r.nodes[i].end1 = 1

    tree2newick(r.nodes[i], str1)
  
  #print(r.c + ",", end="")
  if r.end1 != 1:
    str1.append(r.c + ",")
  else:
    str1.append(r.c)
  if r.end1 == 1:
    #print(")", end="")
    str1.append(")")

tree_str = "(A:1,(B:1,(E:1,e:1)b:0.5)a:0.5)S;"
tree_str = "(A,(B,(E,e)b)a)S;"

#tree_str = "((1,6),((3,2,9),4));"

#tree_str = "((1,2),4);"

#tree_str = "((1,4)3,(7,(20)14)10)5;"
#t = Tree(tree_str, format=1)
#t = t.get_ascii(show_internal=True)
#print(t)

# Baum aufbauen fuer Suffix minimize

if 1==1:
  a0 = Node("e", [])

  a1 = Node("mize", [])
  a2 = Node("nimize", [])
  a3 = Node("ze", [])

  a4 = Node("nimize", [])
  a5 = Node("ze", [])

  a6 = Node("nimize", [])

  a7 = Node("ze", [])

  a8 = Node("i", [a1, a2, a3])
  a9 = Node("mi", [a4, a5])

  r = Node("", [a0, a8, a9, a6, a7])

if 1==2:
  a0 = Node("1", [])
  a1 = Node("4", [])

  a2 = Node("7", [])

  a3 = Node("20", [])

  a4 = Node("14", [a3])

  a5 = Node("3", [a0, a1])
  a6 = Node("10", [a2, a4])

  r = Node("5", [a5, a6])


if 1==2:
  a0 = Node("r", [])
  a1 = Node("l", [])

  a2 = Node("a", [a0])
  a3 = Node("e", [a2])


  a4 = Node("l", [a1])
  a5 = Node("e", [a4])
  
  r = Node("b", [a3, a5])


if 1==2:
  a0 = Node("r", [])
  a1 = Node("a", [a0])
  a2 = Node("l", [])
  a3 = Node("l", [a2])
  a4 = Node("e", [a1, a3])#, a3
  #
  a5 = Node("d", [])
  a6 = Node("i", [a5])
  #
  a7 = Node("l", [])
  a8 = Node("l", [a7])
  a9 = Node("u", [a8])
  #
  a10 = Node("b", [a4, a6]) #, a6, a9
  #
  a11 = Node("k", [])
  a12 = Node("c", [a11])
  a13 = Node("p", [])
  a14 = Node("o", [a12, a13])
  a15 = Node("t", [a14])
  a16 = Node("s", [a15])

  r = Node("", [a10]) #, a16

# Suffix Tree banana$
if 1==2:
  r = Node("", [])
  a0 = Node("$", [])
  r.nodes.append(a0)
  
  a1 = Node("$", [])
  a2 = Node("na$", [])
  a3 = Node("na", [a1, a2])
  a4 = Node("$", [])
  a5 = Node("a", [a4, a3])
  r.nodes.append(a5)

  a6 = Node("$", [])
  a7 = Node("na$", [])
  a8 = Node("na", [a6, a7])
  r.nodes.append(a8)
  
  a9 = Node("banana$", [])
  r.nodes.append(a9)

# Suffix Tree of Banana Creation
if 1==2:
  o = 4

  # Erste 3 Woerter
  if o==1:
    r = Node("", [])
    a0 = Node("banana$", [])
    a1 = Node("anana$", [])
    a2 = Node("nana$", [])
    r.nodes.append(a0)
    r.nodes.append(a1)
    r.nodes.append(a2)

  # Hinzufuegen von "ana"
  if o==2:
    r = Node("", [])
    a0 = Node("banana$", [])

    a11 = Node("na$", [])
    a12 = Node("$", [])

    a1 = Node("ana$", [a11, a12])
    a2 = Node("nana$", [])
    r.nodes.append(a0)
    r.nodes.append(a1)
    r.nodes.append(a2)

  # Hinzufuegen von "na"
  if o==3:
    r = Node("", [])
    a0 = Node("banana$", [])

    a11 = Node("na$", [])
    a12 = Node("$", [])

    a1 = Node("ana$", [a11, a12])
    
    a21 = Node("na$", [])
    a22 = Node("$", [])
    a2 = Node("na$", [a21, a22])
    r.nodes.append(a0)
    r.nodes.append(a1)
    r.nodes.append(a2)

  # Hinzufuegen von a und $
  if o==4:
    r = Node("", [])
    a0 = Node("banana$", [])

    a11 = Node("na$", [])
    a12 = Node("$", [])

    a3 = Node("a", [])
    a33 = Node("na", [])
    a31 = Node("$", [])
    a3.nodes.append(a33)
    a3.nodes.append(a31)
    a34 = Node("na", [])
    a35 = Node("$", [])
    a33.nodes.append(a34)
    a33.nodes.append(a35)

    a21 = Node("na$", [])
    a22 = Node("$", [])
    a2 = Node("na$", [a21, a22])
    r.nodes.append(a0)
    r.nodes.append(a3)
    r.nodes.append(a2)
    r.nodes.append(Node("$", []))

#a0 = Node(["mize", "nimize", "ze"], [])
#a1 = Node(["nimize", "ze"], [])
#a3 = Node(["i"], [a0])
#a4 = Node(["e"], [])
#a5 = Node(["nimize"], [])
#a6 = Node(["ze"], [])
#a7 = Node(["mi"], [])

#str1 = tree2newick(r)
#str1[-1] = ";"
#print(str1)

str1 = []
tree2newick(r, str1)
tree_str = ''.join(str1)[0:-1]+";"
#tree_str = tree_str.replace(",(", "(")
#print(tree_str)
#tree_str = tree_str.replace(",)",")")
#print(tree_str)


t = Tree(tree_str, format=1)
print(t.get_ascii(show_internal=True))
#t.render("mytree.png", w=183, units="mm")

#circular_style = TreeStyle()
#circular_style.mode = "c" # draw tree in circular mode
#circular_style.scale = 20
#t.render("mytree.png", w=183, units="mm", tree_style=circular_style)


if 1==2:
  #t.populate(10)
  ts = TreeStyle()
  ts.show_leaf_name = True
  #ts.rotation = 90
  ts.scale =  120
  #ts.scale_length = 0.5 #geht nicht
  ts.show_scale = False
  #ts.show
  #t.show(tree_style=ts)
  t.render("mytree.png", tree_style=ts) #, w=183, units="mm"
