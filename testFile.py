from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

c1 = Car("Honda", "CRV", 2007, 8000)
c2 = Car("Dodge", "dart", 2015, 6000)
c3 = Car("Honda", "CRV", 2007, 8000)
c4 = Car("Honda", "dRV", 2007, 8000)
c5 = Car("Honda", "CRV", 2008, 8000)
c6 = Car("Honda", "CRV", 2008, 9000)

class Test_Car:
    def test_init_(self):
        assert c1.make == "HONDA"

    def test_gt(self):
        assert c2 > c1
        assert c3 > c4
        assert c5 > c3
        assert c6 > c3

    def test_lt(self):
        assert c1 < c2
        assert c4 < c3
        assert c3 < c5
        assert c3 < c6

    def test_eq(self):
        assert c1 == c3

    def test_str(self):
        assert str(c1) == 'Make: HONDA, Model: CRV, Year: 2007, Price: $8000'

t1 = CarInventoryNode(c1)
class Test_CarInventoryNode:
    def test_init(self):
        assert t1.car == c1
        assert t1.make == "HONDA"

    def test_get_make(self):
        assert t1.get_make() == "HONDA"

    def test_get_model(self):
        assert t1.get_model() == "CRV"

    def test_get_parent(self):
        assert t1.get_parent() == None

    def test_set_parent(self):
        t1.set_parent(c2)
        assert t1.get_parent() == c2

    def test_get_left(self):
        assert t1.get_left() == None

    def test_set_left(self):
        t1.set_left(c3)
        assert t1.get_left() == c3
        
    def test_get_right(self):
        assert t1.get_right() == None

    def test_set_right(self):
        t1.set_right(c4)
        assert t1.get_right() == c4

    def test_str(self):
        assert str(t1) == 'Make: HONDA, Model: CRV, Year: 2007, Price: $8000\n'


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

bst = CarInventory()
car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)
car6 = Car("Ford", "Ranger", 2021, 2500)
car7 = Car("Ford", "Ranger", 2020, 25000)
bst.add_car(car1)
bst.add_car(car2)
bst.add_car(car3)
bst.add_car(car4)
bst.add_car(car5)

bst1 = CarInventory()
car1a = Car("toyota", "prius", 2022, 25000)
car2a = Car("Honda", "ODYSSEY", 2009, 30000)
car3a = Car("Ferrari", "testarossa", 1990, 100000)
car4a = Car("Chevrolet", "Equinox", 2011, 10000)
bst1.add_car(car1a)
bst1.add_car(car2a)
bst1.add_car(car3a)
bst1.add_car(car4a)
show_tree(bst.root)


bst2 = CarInventory()
cara = Car("toyota", "sienna", 2022, 25000)
carb = Car("toyota", "prius", 2009, 30000)
carc = Car("apple", "banana", 1990, 100000)
card = Car("ty", "z", 2011, 10000)
bst2.add_car(cara)
bst2.add_car(carb)
bst2.add_car(carc)
bst2.add_car(card)
show_tree(bst.root)


class Test_CarInventoryNode:
    def test_add_car(self):
        show_tree(bst.root)

    def test_does_car_exist(self):
        assert bst.does_car_exist(car1) == True
        assert bst.does_car_exist(car6) == False
        assert bst.does_car_exist(car7) == False
        

    def test_inorder(self):
        assert bst1.inorder() == \
               'Make: CHEVROLET, Model: EQUINOX, Year: 2011, Price: $10000\n\
Make: FERRARI, Model: TESTAROSSA, Year: 1990, Price: $100000\n\
Make: HONDA, Model: ODYSSEY, Year: 2009, Price: $30000\n\
Make: TOYOTA, Model: PRIUS, Year: 2022, Price: $25000\n'

    def test_preorder(self):
        assert bst1.preorder() == \
               'Make: TOYOTA, Model: PRIUS, Year: 2022, Price: $25000\n\
Make: HONDA, Model: ODYSSEY, Year: 2009, Price: $30000\n\
Make: FERRARI, Model: TESTAROSSA, Year: 1990, Price: $100000\n\
Make: CHEVROLET, Model: EQUINOX, Year: 2011, Price: $10000\n'

    def test_postorder(self):
        assert bst1.postorder() == \
               'Make: CHEVROLET, Model: EQUINOX, Year: 2011, Price: $10000\n\
Make: FERRARI, Model: TESTAROSSA, Year: 1990, Price: $100000\n\
Make: HONDA, Model: ODYSSEY, Year: 2009, Price: $30000\n\
Make: TOYOTA, Model: PRIUS, Year: 2022, Price: $25000\n'

    def test_get_best_car(self):
        assert bst.get_best_car("Mercedes", "Sprinter") == car3

    def test_get_worst_car(self):
        assert bst.get_worst_car("Mercedes", "Sprinter") == car4

    def test_get_total_inventory_price(self):
        assert bst1.get_total_inventory_price() == 165000

    def test_get_successor(self):
        assert bst.get_successor('Tesla', 'model3') == None
        assert bst.get_successor("Nissan", "Leaf").make == 'TESLA'
        assert bst.get_successor("Mercedes", "Sprinter").make == 'NISSAN'
        assert bst.get_successor("Ford", "Ranger").make == 'MERCEDES'
        
    
    def test_remove_car(self):
        bst.remove_car("Tesla", "Model3", 2018, 50000)
        bst1.remove_car("Ferrari", "testarossa", 1990, 100000)
        bst2.remove_car("toyota", "prius", 2009, 30000)
        bst.inorder() == 'Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER,Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n'
        bst1.inorder() == 'Make: CHEVROLET, Model: EQUINOX, Year: 2011, Price: $10000\n\
Make: HONDA, Model: ODYSSEY, Year: 2009, Price: $30000\n\
Make: TOYOTA, Model: PRIUS, Year: 2022, Price: $25000\n'
        bst2.inorder() == 'Make: APPLE, Model: BANANA, Year: 1990, Price: $100000\nMake: TOYOTA, Model: PRIUS, Year: 2009, Price: $30000\n\
Make: TOYOTA, Model: SIENNA, Year: 2022, Price: $25000\n\
Make: TY, Model: Z, Year: 2011, Price: $10000\n'
        

        
