class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert node at the beginning"""
        new_node = DNode(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print(f"✓ Inserted {data} at beginning")
    
    def insert_at_end(self, data):
        """Insert node at the end"""
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            print(f"✓ Inserted {data} as first node")
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
        print(f"✓ Inserted {data} at end")
    
    def delete_node(self, key):
        """Delete node with given key"""
        current = self.head
        
        while current and current.data != key:
            current = current.next
        
        if not current:
            print(f"✗ {key} not found!")
            return
        
        # If node is head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
        
        print(f"✗ Deleted {key}")
    
    def display_forward(self):
        """Display list from head to tail"""
        if not self.head:
            print("📊 List is empty")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(f"\n📊 Forward: NULL ⇄ {' ⇄ '.join(elements)} ⇄ NULL")
    
    def display_backward(self):
        """Display list from tail to head"""
        if not self.head:
            print("📊 List is empty")
            return
        
        # Go to end
        current = self.head
        while current.next:
            current = current.next
        
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        print(f"📊 Backward: NULL ⇄ {' ⇄ '.join(elements)} ⇄ NULL")
    
    def visualize(self):
        """Visual representation"""
        print("\n┌─────────────────────────────────────┐")
        print("│  Doubly Linked List Structure       │")
        print("└─────────────────────────────────────┘")
        
        if not self.head:
            print("  NULL")
            return
        
        current = self.head
        print("  NULL", end="")
        while current:
            print(f" ⇄ [{current.data}]", end="")
            current = current.next
        print(" ⇄ NULL\n")

# Demonstration: Browser History
print("=" * 50)
print("  WEB BROWSER HISTORY - DOUBLY LINKED LIST")
print("=" * 50)

browser_history = DoublyLinkedList()

# Building browsing history
print("\n🌐 Building Browser History:")
browser_history.insert_at_end("google.com")
browser_history.insert_at_end("github.com")
browser_history.insert_at_end("stackoverflow.com")
browser_history.insert_at_end("wikipedia.org")

browser_history.visualize()

# Navigate forward
print("▶️ Forward Navigation:")
browser_history.display_forward()

# Navigate backward
print("\n◀️ Backward Navigation:")
browser_history.display_backward()

# Add new page at beginning (new tab)
print("\n📌 Opening new tab:")
browser_history.insert_at_beginning("youtube.com")
browser_history.visualize()

# Close a page
print("❌ Closing a page (github.com):")
browser_history.delete_node("github.com")
browser_history.visualize()

# Add another page
print("📌 Visiting new page:")
browser_history.insert_at_end("linkedin.com")
browser_history.visualize()

print("\n⚡ Performance Characteristics:")
print("  • Access: O(n)")
print("  • Search: O(n)")
print("  • Insert at beginning: O(1)")
print("  • Insert at end: O(n) [O(1) with tail pointer]")
print("  • Delete: O(1) [if node reference available]")
print("  • Bidirectional traversal: Yes")