# LinearList class implements a linear data structure using Python list
class LinearList:
    
    # Constructor: initializes an empty list to store elements
    def __init__(self):
        self.items = []
    
    # Inserts an element at a given position
    # If no position is provided, element is added at the end
    def insert(self, element, position=None):
        """Insert element at position (or end if None)"""
        if position is None:
            self.items.append(element)  # Append element at the end
            print(f"✓ Inserted {element} at end")
        else:
            self.items.insert(position, element)  # Insert at specific index
            print(f"✓ Inserted {element} at position {position}")
    
    # Deletes an element from a specified position
    def delete(self, position):
        """Delete element at position"""
        # Check if position is valid
        if 0 <= position < len(self.items):
            removed = self.items.pop(position)  # Remove and return element
            print(f"✗ Deleted {removed} from position {position}")
            return removed
        print("✗ Invalid position!")
        return None
    
    # Searches for an element in the list
    # Returns index if found, otherwise -1
    def search(self, element):
        """Search for element and return position"""
        try:
            pos = self.items.index(element)  # Find index of element
            print(f"🔍 Found {element} at position {pos}")
            return pos
        except ValueError:
            print(f"🔍 {element} not found!")
            return -1
    
    # Displays all elements and length of the list
    def display(self):
        """Display all elements"""
        print(f"\n📊 Current List: {self.items}")
        print(f"📏 Length: {len(self.items)}")
        return self.items
    
    # Provides an ASCII-style visualization of the list
    def visualize(self):
        """ASCII visualization"""
        print("\n┌─────────────────────────────────────┐")
        print("│  Visual Representation of List     │")
        print("└─────────────────────────────────────┘")
        
        # Check if list is empty
        if not self.items:
            print("  [Empty List]")
        else:
            # Display each element with its index
            for i, item in enumerate(self.items):
                print(f"  Index {i}: [{item}]")
        print()


# ---------------- DEMONSTRATION ---------------- #

# Title output
print("=" * 50)
print("  STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 50)

# Creating an object of LinearList to store grades
grades = LinearList()

# Adding student grades
print("\n📝 Adding Student Grades:")
grades.insert(85)   # Student 0
grades.insert(92)   # Student 1
grades.insert(78)   # Student 2
grades.insert(95)   # Student 3
grades.insert(88)   # Student 4

# Visualize current list
grades.visualize()

# Insert a new grade at a specific position
print("📌 Inserting new student at position 2:")
grades.insert(90, 2)
grades.visualize()

# Search operations
print("🔎 Searching Operations:")
grades.search(95)    # Existing element
grades.search(100)   # Non-existing element

# Delete a grade at a specific position
print("\n🗑️ Deleting student at position 3:")
grades.delete(3)
grades.visualize()

# Display final list
print("📈 Final Grade List:")
grades.display()

# Time complexity analysis of operations
print("\n⚡ Performance Characteristics:")
print("  • Access by index: O(1)")
print("  • Search: O(n)")
print("  • Insert at end: O(1)")
print("  • Insert at middle: O(n)")
print("  • Delete: O(n)")