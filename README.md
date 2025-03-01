# SplayTree Visualization

This project provides a graphical user interface (GUI) for visualizing and interacting with a **Splay Tree**, a self-adjusting binary search tree. The application allows users to insert, search, and delete nodes while dynamically visualizing the tree structure and splaying operations.

---

## Features
- **Insert Nodes**: Add new nodes to the SplayTree with a key and optional data.
- **Search Nodes**: Search for a node by its key, which triggers a splaying operation to bring the node to the root.
- **Delete Nodes**: Remove a node from the SplayTree.
- **Dynamic Visualization**: The tree is visualized in real-time using a Tkinter canvas.
- **Splaying Animation**: Watch the tree adjust itself during search, insert, and delete operations.

---

## Tools and Technologies
- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Data Structure**: Splay Tree
- **Visualization**: Canvas widget for drawing nodes and edges

---

## How It Works
1. **Insertion**: When a new node is inserted, it is added to the tree and splayed to the root.
2. **Search**: Searching for a node brings it to the root through splaying.
3. **Deletion**: Deleting a node removes it from the tree and splays its parent.
4. **Visualization**: The tree is drawn recursively on a Tkinter canvas, with nodes and edges dynamically updated after each operation.

---

## Screenshot
![SplayTree Visualization](/SplayedTree.png)  
*Example of a SplayTree after inserting and splaying nodes.*

3. **Using the GUI**:
   - Enter a **key** (integer) and optional **data** in the input fields.
   - Use the buttons to **Insert**, **Search**, or **Delete** nodes.
   - Watch the tree update in real-time on the canvas.

---

## Code Structure
- **`Node` Class**: Represents a node in the SplayTree.
- **`SplayTree` Class**: Implements the SplayTree data structure and operations.
- **`TreeVisualizer` Class**: Handles the Tkinter GUI and visualization logic.

---

## Example
```python
# Insert a node with key=10 and data="A"
tree.insert(10, "A")

# Search for a node with key=10
tree.search(10)

# Delete a node with key=10
tree.delete(10)
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Inspired by the SplayTree data structure and its applications in dynamic optimality.
- Built with Python and Tkinter for simplicity and ease of use.

---
