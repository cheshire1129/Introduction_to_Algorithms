class node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, x):
        if x != None:
            self.inorder_traversal(x.left)
            print(x.key, end=" ")
            self.inorder_traversal(x.right)

    def print_tree(self):
        self.inorder_traversal(self.root)
        print()   

    def search_rec(self, x, k):
        if x != None:
            if x.key == k:
                return x
            elif x.key > k:
                return self.search_rec(x.left, k)
            else:
                return self.search_rec(x.right, k)
        else:
          return x

    def search_it(self, x, k):
        while x != None and k != x.key:
            if x.key > k:
                x = x.left
            else:
                x = x.right
        return x    

    def min(self, x):
        while x != None:
            y = x
            x = x.left
        return y
    
    # max 함수는 predessor를 찾을 때 필요하지만, successor를 통해 구현할 것이므로 주석처리한다.  
    # def max(self, x):
    #     while x != None:
    #         y = x
    #         x = x.right
    #     return y
    
    def successor(self, x):
        # right == null 인 경우와 아닌 경우로 나뉜다.
        if x.right != None:
            return self.min(x.right)
        y = x.parent
        while y != None and y != x.left:
            x = y
            y = y.parent
        return y

    def insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, z):
        # 삭제할 노드를 y 포인터, y 아래 자식을 x 포인터
        # step 1. 삭제할 노드 선택
        if z.left != None and z.right != None:
            y = self.successor(z)
        else:
            y = z 
        # step 2. x 구하기 
        if y.left != None:
            x = y.left
        else:
            x = y.right
        # step 3. x를 y의 parent와 연결해주기
        if x != None:
            x.parent = y.parent
        # step 4. y의 parent를 x와 연결해주기
        if y.parent == None:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        # step 5. 삭제되는 노드가 successor인 경우 값 바꿔주기
        if y != z:
            z.key = y.key
        return y
    
    

tree = tree()
# 교재에 있는 트리 모양을 만들기 위해 node_key 리스트를 만들고, 순차적으로 삽입한다. 
node_key_list = [56, 26, 200, 18, 28, 190, 213, 12, 24, 27]
for key in node_key_list:
    print(f"{key} 삽입 전 : ", end = " ")
    tree.print_tree()
    temp_node = node(key)
    tree.insert(temp_node)
    print(f"{key} 삽입 후 : ", end = " ")
    tree.print_tree()
    print()

# 최종 트리 확인
print("현재까지의 트리 확인 : ", end = " ")
tree.print_tree()    
print()

# search 함수 확인
#print(tree.search_it(tree.root, 56).key)
#print(tree.search_rec(tree.root, 26))
#tree.print_tree()


# key 값이 195인 노드 삽입
print("195 삽입 전 : ", end = " ") 
tree.print_tree()
node_195 = node(195)
tree.insert(node_195)
print("195 삽입 후 : ", end = " ") 
tree.print_tree()
print()

# case 0
# key 값이 190인 노드 삭제
# key 값이 190인 노드를 포인터 node_190으로 잡는다. 
node_190= tree.search_it(tree.root, 190)
# 해당 노드를 삭제
print("190 삭제 전 : ", end = " ") 
tree.print_tree()
tree.delete(node_190)
print("190 삭제 후 : ", end = " ") 
tree.print_tree()   
print()

# case 1
# key 값이 28인 노드 삭제
# key 값이 28인 노드를 포인터 node_28으로 잡는다. 
node_28= tree.search_it(tree.root, 28)
# 해당 노드를 삭제
print("28 삭제 전 : ", end = " ") 
tree.print_tree()
tree.delete(node_28)
print("28 삭제 후 : ", end = " ") 
tree.print_tree()   
print()

# case 2
# key 값이 26인 노드 삭제
# key 값이 26인 노드를 포인터 node_26으로 잡는다. 
node_26= tree.search_it(tree.root, 26)
# 해당 노드를 삭제
print("26 삭제 전 : ", end = " ") 
tree.print_tree()
tree.delete(node_26)
print("26 삭제 후 : ", end = " ") 
tree.print_tree()   
print()

    
