from Node import Node 

class SplayTree:
    def __init__(self):
        self.root = None
        self.counter = 0
        self.kera = 1
        self.crot = 0

    def mini(self, x):  # Tree_Minimum
        while x.left is not None:
            x = x.left
        return x

    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                a = x
                x = x.left
                if x is None:
                    self.splay(a)
            else:
                b = x
                x = x.right
                if x is None:
                    self.splay(b)
        if x is not None:
            self.splay(x)
        return x

    def insert(self, key, data):
        z = Node(key, data)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.splay(z)

    def delete(self, key):
        z = self.search(key)
        if z is None:
            return None
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.mini(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def rotateright(self, x):
        self.crot += 1
        y = x.left
        if x.p is None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.p = x.p
        x.left = y.right
        if x.left is not None:
            x.left.p = x
        y.right = x
        x.p = y

    def rotateleft(self, x):
        self.crot += 1
        y = x.right
        if x.p is None:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.p = x.p
        x.right = y.left
        if x.right is not None:
            x.right.p = x
        y.left = x
        x.p = y

    def splaystep(self, x):
        if x.p is None:
            return None
        elif x.p.p is None and x == x.p.left:
            self.rotateright(x.p)
        elif x.p.p is None and x == x.p.right:
            self.rotateleft(x.p)
        elif x == x.p.left and x.p == x.p.p.left:
            self.rotateright(x.p.p)
            self.rotateright(x.p)
        elif x == x.p.right and x.p == x.p.p.right:
            self.rotateleft(x.p.p)
            self.rotateleft(x.p)
        elif x == x.p.left and x.p == x.p.p.right:
            self.rotateright(x.p)
            self.rotateleft(x.p)
        else:
            self.rotateleft(x.p)
            self.rotateright(x.p)

    def splay(self, x):
        print("Splay an Knoten:", x.key)
        self.crot = 0
        while x.p is not None:
            self.splaystep(x)

    def depth(self, node):
        r = 0
        while node.p:
            node = node.p
            r += 1
        return r

    def position(self, node):
        w = node.p
        if w is None:
            w = self.root
            node.posx = 500
            node.posy = 30
        if node == w.left:
            node.posx = w.posx - 100 * 2 ** (-self.depth(node) - 1)
            node.posy = w.posy + 100
        elif node == w.right:
            node.posx = w.posx + 100 * 2 ** (-self.depth(node) - 1)
            node.posy = w.posy + 100

    def draw_node(self, node, canvas):
        self.position(node)
        x = node.posx
        y = node.posy
        canvas.create_rectangle(x, y, x + 20, y + 20, fill="yellow")
        canvas.create_text(x + 10, y + 10, text=node.key)
        if node.left:
            self.draw_node(node.left, canvas)
            canvas.create_line(x + 10, y + 20, node.left.posx + 10, node.left.posy)
        if node.right:
            self.draw_node(node.right, canvas)
            canvas.create_line(x + 10, y + 20, node.right.posx + 10, node.right.posy)

    def draw(self, canvas):
        canvas.delete("all")
        if self.root:
            self.draw_node(self.root, canvas)
