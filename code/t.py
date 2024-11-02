from ete3 import Tree, TreeStyle
#pip install PyQt5
#pip install --upgrade ete3
    
tree_str = "((((r)a)e)b);"

#tree_str = "((1,6),((3,2,9),4));"

#tree_str = "((1,2),4);"

#tree_str = "((1,4)3,(7,(20)14)10)5;"
t = Tree(tree_str, format=1)
print(t.get_ascii(show_internal=True))

#ts = TreeStyle()
#ts.show_leaf_name = True
#ts.scale = 120
#ts.show_scale = True
#t.show(tree_style=ts)
#t.render("mytree.png", tree_style=ts)
# Baum aufbauen fuer Suffix minimize

