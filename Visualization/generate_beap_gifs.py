#!/usr/bin/env python3
"""
BEAP Single Operation GIF Generator

Generates individual GIF animations for each BEAP operation.
Clean, educational animations perfect for academic use.
"""

import sys
import os
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend

sys.path.append(os.path.join('..', 'Paper and Summary'))
from visual import BeapEducationalVisualizer

def create_insert_animation():
    """Create insertion operation animation."""
    print("🔧 Creating INSERT animation...")
    
    visualizer = BeapEducationalVisualizer()
    visualizer.reset_demo()
    
    # Simple insertion demo showing bubble-up
    operations = [
        ('insert', 5),  # Root
        ('insert', 8),  # Right child
        ('insert', 2),  # This will bubble up to show the process
    ]
    
    visualizer.create_operation_demo(operations)
    visualizer.save_as_gif("insert_demo.gif", duration=3000)
    
    print("✅ Created: insert_demo.gif")

def create_search_animation():
    """Create search operation animation."""
    print("🔍 Creating SEARCH animation...")
    
    visualizer = BeapEducationalVisualizer()
    visualizer.reset_demo()
    
    # Build small beap then search
    operations = [
        ('insert', 6),
        ('insert', 3), 
        ('insert', 9),
        ('insert', 1),
        ('search', 9),  # Search for a value
    ]
    
    visualizer.create_operation_demo(operations)
    visualizer.save_as_gif("search_demo.gif", duration=3000)
    
    print("✅ Created: search_demo.gif")

def create_extract_animation():
    """Create extract operation animation."""
    print("🗑️ Creating EXTRACT animation...")
    
    visualizer = BeapEducationalVisualizer()
    visualizer.reset_demo()
    
    # Build beap then extract minimum
    operations = [
        ('insert', 4),
        ('insert', 2),
        ('insert', 7),
        ('insert', 1),
        ('extract', 1),  # Extract minimum to show heapify
    ]
    
    visualizer.create_operation_demo(operations)
    visualizer.save_as_gif("extract_demo.gif", duration=3000)
    
    print("✅ Created: extract_demo.gif")

def create_minmax_animation():
    """Create min/max operation animation."""
    print("🏆 Creating MIN/MAX animation...")
    
    visualizer = BeapEducationalVisualizer()
    visualizer.reset_demo()
    
    # Build beap and show min/max finding
    operations = [
        ('insert', 5),
        ('insert', 2),
        ('insert', 8),
        ('insert', 1),
        ('insert', 9),
        ('min_max', None),  # Show min/max operations
    ]
    
    visualizer.create_operation_demo(operations)
    visualizer.save_as_gif("minmax_demo.gif", duration=3500)
    
    print("✅ Created: minmax_demo.gif")

def create_structure_animation():
    """Create BEAP structure formation animation."""
    print("🏗️ Creating STRUCTURE formation animation...")
    
    visualizer = BeapEducationalVisualizer()
    visualizer.reset_demo()
    
    # Show how BEAP structure forms
    operations = [
        ('insert', 4),    # Root
        ('insert', 2),    # First child
        ('insert', 6),    # Second child
        ('insert', 1),    # Third level
    ]
    
    visualizer.create_operation_demo(operations)
    visualizer.save_as_gif("structure_demo.gif", duration=4000)
    
    print("✅ Created: structure_demo.gif")

def main():
    """Generate all BEAP operation animations."""
    print("🎬 BEAP Single Operation GIF Generator")
    print("=" * 40)
    print("Creating clean educational animations...")
    print()
    
    # Create each animation
    create_structure_animation()
    create_insert_animation()
    create_search_animation()
    create_extract_animation()
    create_minmax_animation()
    
    print("\n🎉 All animations created!")
    print("\n📁 Generated files:")
    print("   🏗️ structure_demo.gif - BEAP formation")
    print("   🔧 insert_demo.gif - Insertion with bubble-up")
    print("   🔍 search_demo.gif - Search algorithm")
    print("   🗑️ extract_demo.gif - Extraction with heapify")
    print("   🏆 minmax_demo.gif - Min/Max operations")
    print("\n💡 Each GIF shows clear step-by-step progression")
    print("📖 Perfect for presentations and teaching!")

if __name__ == "__main__":
    main() 