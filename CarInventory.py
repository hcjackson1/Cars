from Car import Car
from CarInventoryNode import CarInventoryNode


class CarInventory:
    def __init__(self):
        self.root = None



    def show_tree(self, node):
        """
        * -> Indicates the base node
        L -> Indicates the left child of the base node
        R -> Indicates the right child of the base node
        LR -> Indicates the right child of the left child of the base node
        ..... and so on
        """
        import sys
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        if node is None:
            print("No cars in inventory.")
        else:
            print(f"Showing Tree Representation of Children under Node - Make: {node.get_make()}, Model: {node.get_model()}\n")
            self._print_tree(node, 0, "")
            print("\nEnd of the car inventory. \n")
        print("\n" + "="*50 + "\n")
        contents = sys.stdout.getvalue()
        sys.stdout = old_stdout
        print(contents)        

    def _print_tree(self, node, level, position):
        if node is not None:
            self._print_tree(node.get_right(), level + 1, position + "R")
            print("   " * level + "|----" + f"(Level {level}) {node.get_make()} : {node.get_model()} ({position if position else '*'})")
            self._print_tree(node.get_left(), level + 1, position + "L")


    def add_car(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
            #print('root',car)
        else:
            node = self.root
            #print('n',node)
            #print('c',car)
            self._add_car(node, car)
            
            
    def _add_car(self, node, car):
##        if node == None:
##            #print('n',node)
##        if car == None:
##            #print('c',car)
        if node.make == car.make and node.model == car.model:
            node.cars.append(car)
            #print('hi',car)
            #self._add_car(node.left, car)

        elif car.make < node.make or (car.make == node.make and car.model < node.model):
            if node.left == None:
                new_node = CarInventoryNode(car)
                node.left = new_node
                new_node.parent = node
                #print('left',new_node)
            
            else:
                #print('leftskip',car)
                self._add_car(node.left, car)

        elif car.make > node.make or (car.make == node.make and car.model > node.model):
            if node.right == None:
                new_node = CarInventoryNode(car)
                node.right = new_node
                new_node.parent = node
                #print('right',new_node)
            else:
                #print('rightskip')
                self._add_car(node.right, car)

    def _inorder(self, root, inorder):
        if root == None:
            return inorder
        if root != None:
            self._inorder(root.left, inorder)
            inorder.append(str(root))
            self._inorder(root.right, inorder)
        return inorder
            

    def inorder(self):
        inorder = []
        if self.root != None:
            inorder = self._inorder(self.root, inorder)
        in_str = ''
        for items in inorder:
            in_str += items
        return in_str

    def _preorder(self, root, preorder):
        if root == None:
            return preorder
        if root != None:
            preorder.append(str(root))
            self._preorder(root.left, preorder)
            self._preorder(root.right, preorder)
        return preorder


    def preorder(self):
        preorder = []
        if self.root != None:
            preorder = self._preorder(self.root, preorder)
        
        pre_str = ''
        for items in preorder:
            pre_str += items
        return pre_str    
            
    def _postorder(self, root, postorder):
        if root == None:
            return postorder
        if root != None:
            self._postorder(root.left, postorder)
            self._postorder(root.right, postorder)
            postorder.append(str(root))
        return postorder


    def postorder(self):
        postorder = []
        if self.root != None:
            postorder = self._postorder(self.root, postorder)
        
        post_str = ''
        for items in postorder:
            post_str += items
        return post_str 
        
        
            



    def does_car_exist(self, car):
        search = self._get_node(self.root, car.make, car.model)
        if search == None:
            return False
        if car in search.cars:
            if str(car) + '\n' in str(search):
                #print("price isn't equal")
                return True
            return False
        else:
            return False

    def get_best_car(self, make, model):
        make = make.upper()
        model = model.upper()
        search = self._get_node(self.root, make, model)
        if search == None:
            return None
        return max(search.cars)

    def get_worst_car(self, make, model):
        make = make.upper()
        model = model.upper()
        search = self._get_node(self.root, make, model)
        if search == None:
            return None
        return min(search.cars)



    def _price(self, root, price):
        if root == None:
            return price
        if root != None:
            self._price(root.left, price)
            self._price(root.right, price)
            price.append(root)
        return price


        

    def get_total_inventory_price(self):
        '''
        total = 0
        total += self._sum_price(self.root, total)
        return total
        '''
        total = 0
        price = []
        if self.root != None:
            price = self._price(self.root, price)
        #print(len(price))
        for cars in price:
            if len(cars.cars) > 1:
                for prices in cars.cars:
                    total += prices.price
            else:
                total += cars.car.price
        return total


    def _get_node(self, node, make, model):
        if node == None:
            return None

        if node.make == make and node.model == model:
            return node


        if make < node.make or (node.make == make and model < node.model):
            return self._get_node(node.left, make, model)

        return self._get_node(node.right, make, model)
    
    def _get_successor(self, node):
        if node.left != None:
            node = node.left
            return self._get_successor(node)
        else:
            print(node)
            return node

    def get_successor(self, make, model):
        
        self.show_tree(self.root)
        make = make.upper()
        model = model.upper()
        print(make, model)
        search2 = self._get_node(self.root, make, model)
        if search2 == None:            
            return None
        if search2.right == None and search2.left == None:
            if search2.parent.left == search2:
                return search2.parent
            return None
        if search2.right == None and search2.left != None:
            print('hi')
            if search2.left.left == None:
                print('returning left' ,search2.parent)
                return search2.parent
            if search2.parent != None:
                if search2.parent.right == None:
                    return search2.parent
                else:
                    return None
            else:
                print('returning None')
                return None
        #if search2.right != None and search2.left == None:
            #print('returning right' ,search2.right)
            #return search2.right
        
        successor = self._get_successor(search2.right)
        print('s',successor)
        return successor
            
        #print(search)

    def remove_car(self, make, model, year, price):
        self.show_tree(self.root)
        make = make.upper()
        model = model.upper()
        print(make, model)
        search3 = self._get_node(self.root, make, model)
        if search3 == None:
            return False
        stop = False
        for cars in search3.cars:
            if cars.year == year:
                if cars.price == price:
                    removal_car = cars
                    print(removal_car)
                    stop = True
        if stop == False:
            return False
        if len(search3.cars) > 1:
            search3.cars.remove(removal_car)
            return True


        
        parent = search3.parent
        if search3.right == None and search3.left == None:
            print('no children')
            if search3 == self.root:
                self.root = None
                self.show_tree(self.root) 
                return True                
            if parent.right == search3:
                parent.right = None
                self.show_tree(self.root) 
                return True
            if parent.left == search3:
                search3.parent.left = None
                self.show_tree(self.root)
                return True
        if search3.right == None:
            print('right child')
            if parent == None:
                
                self.root = search3.left
                self.root.parent = None
                
                search3.left = None
                self.show_tree(self.root)
                return True
            if parent.right == search3:
                #suc = self.get_successor(make, model)
                #parent2 = suc.parent
                parent.right = search3.left
                parent.right.parent = parent
                #parent2.left = None
                self.show_tree(self.root)
                return True
            if parent.left == search3:
                parent.left = search3.left
                parent.left.parent = parent
                self.show_tree(self.root)
                return True
        if search3.left == None:
            print('hi')
            rt = search3.right
            suc = self.get_successor(make, model)
            sp = suc.parent
            
            
            if parent == None:
                self.root = search3.right
                #suc.right = search3.right
                search3.right = None
                #suc.parent = None
                self.root.parent = None
                self.show_tree(self.root)
                return True
            if search3.right != suc:
                sp.left = None    
            if parent.left == search3:
                suc.parent = parent
                parent.left = suc
                if search3 == selft.root:
                    self.root = suc
                self.show_tree(self.root)
                return True
            if parent.right == search3:
                suc.parent = parent
                parent.right = suc
                if search3 == selft.root:
                    self.root = suc
                self.show_tree(self.root)
                return True
        else:
            suc = self.get_successor(make, model)
            print(suc)
            sp = suc.parent
            rt = search3.right
            lf = search3.left
            if sp.left == suc:
                sp.left = None
            if sp.right == None:
                sp.right = None
            if rt != suc:
                suc.right = rt
                suc.right.parent = suc
            else:
                suc.right = None
            if lf != suc:
                suc.left = lf
                suc.left.parent = suc
            else:
                suc.left = None
            
            if parent == None:
                self.root = suc
                print(self.root)
                suc.parent = None
                self.show_tree(self.root)
                return True
                
            if search3.parent.right == search3:
                suc.parent.right = suc
                self.show_tree(self.root)
                return True

            if search3.parent.left == search3:
                suc.parent.left = suc
                self.show_tree(self.root)
                return True
        print('end')
            
                
                
                
                
            
            
            
        
                
                
                
            
            
                
                
            
            
            
        
        
        
            
        
    
      
    

'''

bst = CarInventory()

car1 = Car("Toyota", "Sienna", 2018, 18000)
car2 = Car("Toyota", "Prius", 2018, 50000)
car3 = Car("Toyota", "Corolla", 2022, 40000)
#car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Honda", "Odyssey", 2020, 25000)
car8 = Car("N", "T", 2020, 25000)
car9 = Car("N", "S", 2020, 25000)
car6 = Car("N", "Z", 2018, 17000)
car7 = Car("Nissan", "Leaf", 2018, 20000)
'''
'''
car1 = Car("H", "O", 2018, 18000)
car2 = Car("T", "S", 2018, 50000)
car3 = Car("T", "P", 2022, 40000)
car4 = Car("T", "C", 2018, 18000)
#car5 = Car("Toyota", "Prius", 2018, 50000)
'''




'''
bst.add_car(car1)
#bst.add_car(car1)
bst.add_car(car2)
bst.add_car(car3)
bst.add_car(car5)
#bst.add_car(car8)
#bst.add_car(car9)
#bst.add_car(car6)
'''
'''
bst.add_car(car2)
#bst.add_car(car1)
bst.add_car(car1)
bst.add_car(car5)
#bst.add_car(car5)
'''
'''
bst.add_car(car5)
bst.add_car(car1)
bst.add_car(car2)
bst.add_car(car3)
#bst.add_car(car5)


#bst.add_car(car6)
#bst.add_car(car7)
#print(bst.inorder())
#print(bst.does_car_exist(car6))
#print(bst.get_best_car('Nissan', 'Leaf'))
#bst.get_total_inventory_price()
bst.show_tree(bst.root)
#bst.remove_car("toyota", "prius", 2018, 50000)
#print(bst.get_successor('toyota', 'corolla'))
bst.remove_car("Honda", "Odyssey", 2020, 25000)
'''
'''
def show_tree(node):
    """
    * -> Indicates the base node
    L -> Indicates the left child of the base node
    R -> Indicates the right child of the base node
    LR -> Indicates the right child of the left child of the base node
    ..... and so on
    """
    import sys
    from io import StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    if node is None:
        print("No cars in inventory.")
    else:
        print(f"Showing Tree Representation of Children under Node - Make: {node.get_make()}, Model: {node.get_model()}\n")
        _print_tree(node, 0, "")
        print("\nEnd of the car inventory. \n")
    print("\n" + "="*50 + "\n")
    contents = sys.stdout.getvalue()
    sys.stdout = old_stdout
    print(contents)        

def _print_tree(node, level, position):
    if node is not None:
        _print_tree(node.get_right(), level + 1, position + "R")
        print("   " * level + "|----" + f"(Level {level}) {node.get_make()} : {node.get_model()} ({position if position else '*'})")
        _print_tree(node.get_left(), level + 1, position + "L")

show_tree(bst.root)
'''
'''
if __name__ == "__main__":
    #inventory = CarInventory()
    # Adding some cars
    #inventory.add_car(Car("Toyota", "Prius", 2020, 25000))
    #inventory.add_car(Car("Toyota", "Sienna", 2019, 23000))
    #inventory.add_car(Car("Toyota", "Corolla", 2018, 20000))
    #inventory.add_car(Car("Toyota", "Camry", 2021, 22000))
    #inventory.add_car(Car("Toyota", "Odyssey", 2017, 18000))
    #inventory.add_car(Car("Toyota", "Camry", 2016, 17000))
    #inventory.add_car(Car("Toyota", "Equinox", 2016, 17000))
    #inventory.add_car(Car("toyota", "prius", 2022, 25000))
    #inventory.add_car(Car("Honda", "ODYSSEY", 2009, 30000))
    #inventory.add_car(Car("Ferrari", "testarossa", 1990, 100000))
    #inventory.add_car(Car("Chevrolet", "Equinox", 2011, 10000))
    #inventory.add_car(Car("Nissan", "Leaf", 2018, 18000))
    #inventory.add_car(Car("Tesla", "Model3", 2018, 50000))
    #inventory.add_car(Car("Mercedes", "Sprinter", 2022, 40000))
    #inventory.add_car(Car("Mercedes", "Sprinter", 2014, 25000))
    #inventory.add_car(Car("Ford", "Ranger", 2021, 25000))
    # Displaying the inventory
    #show_tree(inventory.root)
    bst = CarInventory()
    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Ferrari", "testarossa", 1990, 100000)
    car4 = Car("ferrari", "monza", 2020, 500000)
    car5 = Car("Chevrolet", "Equinox", 2011, 10000)
    bst.add_car(car1)
    bst.add_car(car5)
    bst.add_car(car2)
    bst.add_car(car4)
    bst.add_car(car3)
    show_tree(bst.root)
'''


