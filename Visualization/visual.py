import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import math
import sys
import os
from PIL import Image
import io

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Paper and Summary'))
from Implementation import beap

class BeapEducationalVisualizer:
    """
    Educational visualization system for BEAP operations.
    Creates step-by-step animations suitable for academic presentations and teaching.
    """
    
    def __init__(self, figsize=(12, 8)):
        self.beap = beap()
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.frames = []  # Store frames for animation
        self.current_step = 0
        
        # Colors for different states
        self.colors = {
            'normal': '#87CEEB',       # Sky blue
            'highlighted': '#FFD700',   # Gold
            'comparing': '#FF6B6B',     # Red
            'moving': '#98FB98',        # Pale green
            'found': '#90EE90',         # Light green
            'removed': '#FFA07A'        # Light salmon
        }
        
        # Animation settings
        self.pause_duration = 1.5
        self.animation_speed = 800  # milliseconds per frame
        
    def reset_demo(self):
        """Reset the visualizer for a new demo."""
        self.beap = beap()
        self.frames = []
        self.current_step = 0
        if hasattr(self, 'ax'):
            self.ax.clear()
        
    def get_beap_layout_position(self, index):
        """Calculate position for beap node in triangular layout."""
        if index >= len(self.beap.beap_list):
            return 0, 0
            
        height = self.beap.getheight(index)
        left_range, right_range = self.beap.getrange(height)
        position_in_level = index - left_range
        level_width = right_range - left_range + 1
        
        # Create triangular beap layout
        x = position_in_level - level_width/2 + 6
        y = -height * 1.2 + 5
        
        return x, y
    
    def draw_frame(self, title="", highlighted_nodes=None, arrows=None, annotations=None, count_step=True):
        """Draw a single frame of the visualization."""
        self.ax.clear()
        self.ax.set_xlim(-1, 13)
        self.ax.set_ylim(-8, 6)
        self.ax.set_aspect('equal')
        
        # Set title with step counter - only increment if count_step is True
        if count_step:
            self.current_step += 1
            full_title = f"Step {self.current_step}: {title}"
        else:
            full_title = title
        self.ax.set_title(full_title, fontsize=14, fontweight='bold', pad=20)
        
        if not self.beap.beap_list:
            self.ax.text(6, 0, "Empty BEAP", fontsize=16, ha='center', va='center',
                        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray"))
            self.ax.axis('off')
            return
        
        # Draw connections first (behind nodes)
        self._draw_connections()
        
        # Draw nodes
        for i, value in enumerate(self.beap.beap_list):
            x, y = self.get_beap_layout_position(i)
            
            # Determine node color
            color = self.colors['normal']
            if highlighted_nodes:
                if i in highlighted_nodes:
                    if 'comparing' in highlighted_nodes[i]:
                        color = self.colors['comparing']
                    elif 'moving' in highlighted_nodes[i]:
                        color = self.colors['moving']
                    elif 'found' in highlighted_nodes[i]:
                        color = self.colors['found']
                    else:
                        color = self.colors['highlighted']
            
            # Draw node circle
            circle = Circle((x, y), 0.3, facecolor=color, edgecolor='black', linewidth=2)
            self.ax.add_patch(circle)
            
            # Add value text
            self.ax.text(x, y, str(value), fontsize=12, ha='center', va='center', 
                        fontweight='bold')
            
            # Add index label below node
            self.ax.text(x, y-0.5, f"[{i}]", fontsize=8, ha='center', va='center', 
                        color='gray')
        
        # Draw arrows if specified
        if arrows:
            for arrow in arrows:
                self._draw_arrow(arrow['from'], arrow['to'], arrow.get('color', 'red'),
                               arrow.get('style', 'arc3,rad=0.1'))
        
        # Add annotations
        if annotations:
            for i, annotation in enumerate(annotations):
                self.ax.text(0.5, 4.5 - i*0.5, annotation, fontsize=10, 
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
        
        # Add beap structure info
        self._add_structure_info()
        
        self.ax.axis('off')
        
        # Save frame with improved buffer handling
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        
        # Create PIL image from buffer data
        frame_data = buf.getvalue()
        frame = Image.open(io.BytesIO(frame_data))
        # Convert to RGB if needed and make a copy
        if frame.mode != 'RGB':
            frame = frame.convert('RGB')
        frame = frame.copy()  # Make a copy to avoid buffer issues
        
        self.frames.append(frame)
        buf.close()
        
        plt.pause(0.01)  # Reduced pause time
    
    def _draw_connections(self):
        """Draw parent-child connections in the beap."""
        for i in range(len(self.beap.beap_list)):
            height = self.beap.getheight(i)
            left_child = i + height
            right_child = i + height + 1
            
            parent_x, parent_y = self.get_beap_layout_position(i)
            
            # Draw to left child
            if left_child < len(self.beap.beap_list):
                child_x, child_y = self.get_beap_layout_position(left_child)
                self.ax.plot([parent_x, child_x], [parent_y-0.3, child_y+0.3], 
                           'gray', linewidth=1.5, alpha=0.7)
            
            # Draw to right child
            if right_child < len(self.beap.beap_list):
                child_x, child_y = self.get_beap_layout_position(right_child)
                self.ax.plot([parent_x, child_x], [parent_y-0.3, child_y+0.3], 
                           'gray', linewidth=1.5, alpha=0.7)
    
    def _draw_arrow(self, from_idx, to_idx, color='red', style='arc3,rad=0.1'):
        """Draw an arrow between two nodes."""
        from_x, from_y = self.get_beap_layout_position(from_idx)
        to_x, to_y = self.get_beap_layout_position(to_idx)
        
        arrow = FancyArrowPatch((from_x, from_y), (to_x, to_y),
                               connectionstyle=style, 
                               arrowstyle='->', 
                               mutation_scale=20, 
                               color=color, 
                               linewidth=2)
        self.ax.add_patch(arrow)
    
    def _add_structure_info(self):
        """Add information about the beap structure."""
        info_text = f"BEAP Size: {len(self.beap.beap_list)}\n"
        if self.beap.beap_list:
            min_val = self.beap.min_beap()
            max_val = self.beap.max_beap()
            info_text += f"Min: {min_val}\nMax: {max_val}"
        
        self.ax.text(10.5, 4, info_text, fontsize=9, va='top',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
    
    def animate_insert(self, value):
        """Animate the insertion process."""
        print(f"Animating insertion of {value}")
        
        # Initial state - don't count as a step
        self.draw_frame(f"Inserting {value} - Initial State", count_step=False)
        
        # Add element to end
        original_size = len(self.beap.beap_list)
        self.beap.beap_list.append(value)
        self.beap.beap_size = len(self.beap.beap_list)
        
        self.draw_frame(f"Added {value} at position {original_size}", 
                       highlighted_nodes={original_size: 'highlighted'},
                       annotations=[f"Element {value} added at the end"])
        
        # Bubble up process
        i = original_size
        while i > 0:
            parent_idx = self.beap.max_parent(i)
            if parent_idx >= 0 and self.beap.beap_list[i] < self.beap.beap_list[parent_idx]:
                # Show comparison
                self.draw_frame(f"Comparing {value} with parent", 
                               highlighted_nodes={i: 'comparing', parent_idx: 'comparing'},
                               arrows=[{'from': i, 'to': parent_idx}],
                               annotations=[f"Compare {self.beap.beap_list[i]} < {self.beap.beap_list[parent_idx]} = True"])
                
                # Perform swap
                self.beap.beap_list[i], self.beap.beap_list[parent_idx] = \
                    self.beap.beap_list[parent_idx], self.beap.beap_list[i]
                
                self.draw_frame(f"Swapped positions", 
                               highlighted_nodes={i: 'moving', parent_idx: 'moving'},
                               annotations=[f"Swapped elements at positions {i} and {parent_idx}"])
                
                i = parent_idx
            else:
                break
        
        # Final state
        self.draw_frame(f"Insertion complete", 
                       highlighted_nodes={i: 'found'},
                       annotations=[f"Element {value} found its final position"])
    
    def animate_search(self, value):
        """Animate the search process."""
        print(f"Animating search for {value}")
        
        if self.beap.beap_size == 0:
            self.draw_frame("Search in empty BEAP", annotations=["BEAP is empty!"])
            return None
        
        # Initial state - don't count as a step
        self.draw_frame(f"Searching for {value}", annotations=[f"Looking for value {value}"], count_step=False)
        
        # Search implementation with visualization
        length = self.beap.beap_size - 1
        height = self.beap.getheight(length)
        left_range, _ = self.beap.getrange(height)
        right_parent = left_range - height + 1
        
        search_path = []
        step_count = 0
        
        while step_count < 20:  # Prevent infinite loops
            search_path.append(left_range)
            step_count += 1
            
            current_value = self.beap.beap_list[left_range]
            
            if value < current_value:
                self.draw_frame(f"Value {value} < {current_value}, going up", 
                               highlighted_nodes={left_range: 'comparing'},
                               annotations=[f"{value} < {current_value}: Move to parent level"])
                
                left_range = right_parent
                height_index = self.beap.getheight(left_range)
                right_parent = left_range - height_index + 1
                
            elif value > current_value:
                self.draw_frame(f"Value {value} > {current_value}, going right", 
                               highlighted_nodes={left_range: 'comparing'},
                               annotations=[f"{value} > {current_value}: Move to right child"])
                
                height_i = self.beap.getheight(left_range)
                rc_leftrange = left_range + height_i + 1
                
                if rc_leftrange <= length:
                    left_range = rc_leftrange
                    height_i = self.beap.getheight(left_range)
                    right_parent = left_range - height_i + 1
                else:
                    self.draw_frame(f"Value {value} not found", 
                                   highlighted_nodes={idx: 'comparing' for idx in search_path},
                                   annotations=[f"No right child available", f"Value {value} not in BEAP"])
                    return None
            else:
                self.draw_frame(f"Found {value}!", 
                               highlighted_nodes={left_range: 'found'},
                               annotations=[f"Found {value} at position {left_range}"])
                return left_range
            
            if left_range == 0:
                self.draw_frame(f"Reached root, {value} not found", 
                               highlighted_nodes={0: 'comparing'},
                               annotations=[f"Reached root", f"Value {value} not in BEAP"])
                return None
        
        return None
    
    def animate_extract(self, value):
        """Animate the extraction process."""
        print(f"Animating extraction of {value}")
        
        if self.beap.beap_size == 0:
            self.draw_frame("Extract from empty BEAP", annotations=["BEAP is empty!"])
            return None
        
        # Find the element first
        index = self.animate_search(value)
        if index is None:
            return None
        
        length = self.beap.beap_size - 1
        
        # Show target
        self.draw_frame(f"Target found at position {index}", 
                       highlighted_nodes={index: 'found'},
                       annotations=[f"Target {value} at position {index}"])
        
        # Swap with last element if needed
        if index != length:
            self.draw_frame(f"Swapping with last element", 
                           highlighted_nodes={index: 'moving', length: 'moving'},
                           arrows=[{'from': index, 'to': length}],
                           annotations=[f"Swap positions {index} and {length}"])
            
            self.beap.beap_list[index], self.beap.beap_list[length] = \
                self.beap.beap_list[length], self.beap.beap_list[index]
        
        # Remove last element
        removed_value = self.beap.beap_list.pop()
        self.beap.beap_size = len(self.beap.beap_list)
        
        self.draw_frame(f"Removed {removed_value}", 
                       annotations=[f"Removed {removed_value} from BEAP"])
        
        # Restore heap property if needed
        if index < len(self.beap.beap_list):
            self.animate_heapify_down(index)
        
        return removed_value
    
    def animate_heapify_down(self, start_index):
        """Animate the heapify down process."""
        i = start_index
        array = self.beap.beap_list
        
        while True:
            height = self.beap.getheight(i)
            left_child = i + height
            
            if left_child >= len(array):
                break
            
            right_child = left_child + 1
            
            # Find minimum child
            min_child = left_child
            if right_child < len(array) and array[right_child] < array[left_child]:
                min_child = right_child
            
            # Show comparison
            children = [left_child]
            if right_child < len(array):
                children.append(right_child)
            
            highlighted = {i: 'comparing'}
            for child in children:
                highlighted[child] = 'comparing'
            
            self.draw_frame(f"Comparing parent with children", 
                           highlighted_nodes=highlighted,
                           annotations=[f"Parent: {array[i]}", f"Min child: {array[min_child]}"])
            
            if array[min_child] < array[i]:
                # Swap needed
                self.draw_frame(f"Swapping parent with child", 
                               highlighted_nodes={i: 'moving', min_child: 'moving'},
                               arrows=[{'from': i, 'to': min_child}],
                               annotations=[f"Swap {array[i]} and {array[min_child]}"])
                
                array[i], array[min_child] = array[min_child], array[i]
                i = min_child
                
                self.draw_frame(f"After swap", 
                               highlighted_nodes={i: 'highlighted'},
                               annotations=["Heap property restored at this level"])
            else:
                break
        
        self.draw_frame("Heapify complete", annotations=["BEAP property fully restored"])
    
    def animate_min_max(self):
        """Animate finding min and max values."""
        print("Animating min/max operations")
        
        if self.beap.beap_size == 0:
            self.draw_frame("Min/Max in empty BEAP", annotations=["BEAP is empty!"])
            return None, None
        
        # Find minimum (always at root)
        min_val = self.beap.beap_list[0]
        self.draw_frame("Finding minimum", 
                       highlighted_nodes={0: 'found'},
                       annotations=[f"Minimum is always at root: {min_val}"])
        
        # Find maximum (search leaf nodes)
        max_val = None
        max_idx = None
        leaf_nodes = []
        
        for i in range(len(self.beap.beap_list) - 1, -1, -1):
            height = self.beap.getheight(i)
            left_child = i + height
            if left_child >= len(self.beap.beap_list):
                leaf_nodes.append(i)
                if max_val is None or self.beap.beap_list[i] > max_val:
                    max_val = self.beap.beap_list[i]
                    max_idx = i
            else:
                break
        
        # Show leaf nodes
        highlighted = {idx: 'comparing' for idx in leaf_nodes}
        self.draw_frame("Searching leaf nodes for maximum", 
                       highlighted_nodes=highlighted,
                       annotations=["Maximum must be in a leaf node"])
        
        # Show maximum
        self.draw_frame("Maximum found", 
                       highlighted_nodes={max_idx: 'found'},
                       annotations=[f"Maximum value: {max_val} at position {max_idx}"])
        
        return min_val, max_val
    
    def create_operation_demo(self, operations):
        """Create a complete demo with multiple operations."""
        print("Creating BEAP operations demo...")
        
        # Don't reset frames here - let caller control this
        # self.frames = []
        # self.current_step = 0
        
        plt.ion()
        
        # Initial empty state - don't count this as a step
        self.draw_frame("BEAP Data Structure Demo", annotations=["Starting with empty BEAP"], count_step=False)
        
        for op_type, value in operations:
            if op_type == 'insert':
                self.animate_insert(value)
            elif op_type == 'search':
                self.animate_search(value)
            elif op_type == 'extract':
                self.animate_extract(value)
            elif op_type == 'min_max':
                self.animate_min_max()
        
        # Final state - don't count this as a step either
        self.draw_frame("Demo Complete", annotations=["All operations completed"], count_step=False)
        
        plt.ioff()
        
    def save_as_gif(self, filename="beap_operations.gif", duration=1500):
        """Save the animation as a GIF file."""
        if not self.frames:
            print("No frames to save!")
            return
        
        print(f"Saving {len(self.frames)} frames as {filename}...")
        
        # Save as GIF
        self.frames[0].save(
            filename,
            save_all=True,
            append_images=self.frames[1:],
            duration=duration,
            loop=0
        )
        
        print(f"Animation saved as {filename}")
    
    def save_individual_frames(self, directory="beap_frames"):
        """Save individual frames as PNG files."""
        import os
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        for i, frame in enumerate(self.frames):
            filename = os.path.join(directory, f"frame_{i:03d}.png")
            frame.save(filename)
        
        print(f"Saved {len(self.frames)} frames to {directory}/")

def create_demo_animation():
    """Create a demonstration animation of BEAP operations."""
    visualizer = BeapEducationalVisualizer()
    
    # Define a sequence of operations to demonstrate
    operations = [
        ('insert', 5),
        ('insert', 2),
        ('insert', 8),
        ('insert', 1),
        ('insert', 9),
        ('insert', 3),
        ('min_max', None),
        ('search', 3),
        ('search', 7),  # Not found
        ('extract', 1),
        ('extract', 8),
        ('min_max', None),
    ]
    
    # Create the demo
    visualizer.create_operation_demo(operations)
    
    # Save as GIF
    visualizer.save_as_gif("beap_educational_demo.gif", duration=2000)
    
    # Also save individual frames
    visualizer.save_individual_frames("beap_frames")
    
    print("\nDemo complete! Generated:")
    print("- beap_educational_demo.gif (animated GIF)")
    print("- beap_frames/ (individual PNG frames)")

if __name__ == "__main__":
    create_demo_animation()
