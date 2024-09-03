# rbt에서는 color을 추가로 넣어준다.
class node:
    def __init__(self, key, color):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

# rbt를 만들기 위해 bst를 만든 tree class에 추가로
# Nil 노드를 만든다. 
class tree:
    def __init__(self):
        self.root = None
        self.Nil = node("None", "Black")

    def inorder_traversal(self, x):
        if x != self.Nil:
            self.inorder_traversal(x.left)
            print(f"{x.key}{x.color}", end=" ")
            self.inorder_traversal(x.right)

    def print_tree(self):
        self.inorder_traversal(self.root)
        print()   

    def search_it(self, x, k):
        while x != self.Nil and k != x.key:
            if x.key > k:
                x = x.left
            else:
                x = x.right
        return x    

    def min(self, x):
        while x != self.Nil:
            y = x
            x = x.left
        return y
    
    def successor(self, x):
        # right == null 인 경우와 아닌 경우로 나뉜다.
        if x.right != self.Nil:
            return self.min(x.right)
        y = x.parent
        while y != None and y != x.left:
            x = y
            y = y.parent
        return y

    def insert(self, z):
        y = self.Nil
        x = self.root
        while x != self.Nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.Nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.right = self.Nil
        z.left = self.Nil
        z.color = "Red"
        self.rb_insert_fixup(z)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.Nil:
            y.left.parent = x
        y.parent = x.parent
        if y.parent == self.Nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.Nil:
            y.right.parent = x
        y.parent = x.parent
        if y.parent == self.Nil:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def rb_insert_fixup(self, z):
        # 루프 불변성에 의해 parent가 red일 때 root일 수 없으므로 3대 이상인 상황
        while z.parent.color == "Red":
            # 부모가 왼쪽
            if z.parent == z.parent.parent.left:
                # uncle을 y로 포인트
                y = z.parent.parent.right
                # case 1
                if y.color == "Red":
                    y.color = "Black"
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                # case 2
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                # case 3
                else: 
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                # case 4  
                if y.color == "Red":
                    y.color = "Black"
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    z = z.parent.parent
                # case 5
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                # case 6
                else: 
                    z.parent.color = "Black"
                    z.parent.parent.color = "Red"
                    self.left_rotate(z.parent.parent)      
        self.root.color = "Black"

    
    def rb_transplant(self, u, v):
        if u.parent == self.Nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.Nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.Nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.min(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left  = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "Black":
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        # x 가 black 이고, root가 아닐 때까지 루프
        while x != self.root and x.color == "Black":
            if x == x.parent.left:
                w = x.parent.right
                # case 1 형제가 red
                if w.color == "Red":
                    w.color = "Black"
                    x.parent.color = "Red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                # case 2, 3, 4는 형제가 black
                # case 2 형제가 black, 형제 자식 모두  black
                elif w.left.color == "Black" and w.right.color == "Black":
                    w.color = "Red"
                    x = x.parent
                # case 3. 형제가 black, 오른 자식만 black
                elif w.left.color == "Red" and w.right.color == "Black":
                    w.left.color = "Black"
                    w.color = "Red"
                    self.right_rotate(w)
                    w = x.parent.right
                # case 4. 형제가 black, 오른 자식이 red
                else:
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.right.color = "Black"
                    self.left_rotate(x.parent)
                    x = self.root
            else: 
                # 대칭적으로 적용
                w = x.parent.left
                # case 1 형제가 red
                if w.color == "Red":
                    w.color = "Black"
                    x.parent.color = "Red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                # case 2, 3, 4는 형제가 black
                # case 2 형제가 black, 형제 자식 모두  black
                elif w.left.color == "Black" and w.right.color == "Black":
                    w.color = "Red"
                    x = x.parent
                # case 3. 형제가 black, 왼 자식만 black
                elif w.right.color == "Red" and w.left.color == "Black":
                    w.right.color = "Black"
                    w.color = "Red"
                    self.left_rotate(w)
                    w = x.parent.left
                # case 4. 형제가 black, 왼 자식이 red
                else:
                    w.color = x.parent.color
                    x.parent.color = "Black"
                    w.left.color = "Black"
                    self.right_rotate(x.parent)
                    x = self.root
        
        x.color = "Black"

tree = tree()
node_key_list = [7, 3, 18, 10, 22, 8, 11, 26, 15]
node_color_list = ["Black", "Black", "Red", "Black", "Black", "Red", "Red", "Red", "Red"]

node_7 = node(node_key_list[0], node_color_list[0])
node_3 = node(node_key_list[1], node_color_list[1])
node_18 = node(node_key_list[2], node_color_list[2])
node_10 = node(node_key_list[3], node_color_list[3])
node_22 = node(node_key_list[4], node_color_list[4])
node_8 = node(node_key_list[5], node_color_list[5])
node_11 = node(node_key_list[6], node_color_list[6])
node_26 = node(node_key_list[7], node_color_list[7])
node_15 = node(node_key_list[8], node_color_list[8])

# node 7
tree.root = node_7
node_7.parent = tree.Nil
node_7.left = node_3
node_7.right = node_18

# node 3
node_3.parent = node_7
node_3.left = tree.Nil
node_3.right = tree.Nil

# node 18
node_18.parent = node_7
node_18.left = node_10
node_18.right = node_22

# node 10
node_10.parent = node_18
node_10.left = node_8
node_10.right = node_11

# node 22
node_22.parent = node_18
node_22.left = tree.Nil
node_22.right = node_26


# node 8 
node_8.parent = node_10
node_8.left = tree.Nil
node_8.right = tree.Nil

# node 11
node_11.parent = node_10
node_11.left = tree.Nil
node_11.right = tree.Nil

# node 26
node_26.parent = node_22
node_26.left = tree.Nil
node_26.right = tree.Nil
print("15 삽입 전 : ")
tree.print_tree()
print("15 삽입 후 : ")
tree.insert(node_15)
tree.print_tree()    



    
