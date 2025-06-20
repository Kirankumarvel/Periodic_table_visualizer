"""
Complete GUI implementation for the periodic table visualizer
"""
import tkinter as tk
from tkinter import ttk
from .data import get_element, get_all_elements, get_category_color

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Periodic Table Visualizer")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Create main container with scrollbar
        self.container = tk.Frame(root)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Initialize the interface
        self.create_widgets()
        self.display_periodic_table()
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main frame
        self.main_frame = tk.Frame(self.scrollable_frame, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Periodic table frame
        self.table_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.table_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Element details frame
        self.details_frame = tk.Frame(self.main_frame, bg="#f0f0f0", 
                                    relief=tk.RIDGE, borderwidth=2)
        self.details_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
        # Search frame
        search_frame = tk.Frame(self.details_frame, bg="#f0f0f0")
        search_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(search_frame, text="Search:", bg="#f0f0f0").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", self.on_search_changed)
        
        # Details display
        self.details_text = tk.Text(self.details_frame, wrap=tk.WORD, 
                                  height=10, state=tk.DISABLED,
                                  font=("Arial", 10))
        self.details_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def display_periodic_table(self):
        """Display the complete periodic table."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Main table (periods 1-7)
        for period in range(1, 8):
            self._create_period_row(period)

        # Special rows for lanthanides and actinides
        self.add_special_elements_row("Lanthanides", 57, 71)
        self.add_special_elements_row("Actinides", 89, 103)

    def _create_period_row(self, period):
        """Helper to create a row for a given period."""
        period_frame = tk.Frame(self.table_frame, bg="#f0f0f0")
        period_frame.pack(side=tk.TOP, fill=tk.X)

        # Add empty space for proper alignment in periods 6-7
        if period >= 6:
            tk.Frame(period_frame, width=100, height=50, bg="#f0f0f0").pack(side=tk.LEFT)

        for group in range(1, 19):
            # Skip positions where no elements exist
            if (period == 1 and group > 2) or (period == 2 and group > 18):
                continue

            element = self._find_element_by_period_group(period, group)
            self.create_element_button(period_frame, element)

    def _find_element_by_period_group(self, period, group):
        """Helper to find an element by period and group."""
        for elem in get_all_elements():
            if "period" in elem and "group" in elem:
                if elem["period"] == period and elem["group"] == group:
                    return elem
        return None
    
    def add_special_elements_row(self, label_text, start_num, end_num):
        """Add a row for special elements with label."""
        special_frame = tk.Frame(self.table_frame, bg="#f0f0f0")
        special_frame.pack(side=tk.TOP, fill=tk.X, pady=(10, 0))
        
        # Add label
        tk.Label(special_frame, text=label_text+":", bg="#f0f0f0", 
                font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
        
        # Add elements
        for atomic_num in range(start_num, end_num+1):
            element = get_element(atomic_num)
            self.create_element_button(special_frame, element)
    
    def create_element_button(self, parent, element):
        """Create a button for an element."""
        if element is None:
            # Empty space for alignment
            tk.Frame(parent, width=50, height=50, bg="#f0f0f0").pack(side=tk.LEFT, padx=2, pady=2)
            return
        
        bg_color = get_category_color(element["category"])
        btn = tk.Button(
            parent,
            text=f"{element['atomic_number']}\n{element['symbol']}",
            bg=bg_color,
            fg="#000000",
            width=5,
            height=3,
            relief=tk.RAISED,
            command=lambda e=element: self.show_element_details(e),
            font=("Arial", 9, "bold")
        )
        btn.pack(side=tk.LEFT, padx=2, pady=2)
    
    def show_element_details(self, element):
        """Display detailed information about an element."""
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)
        
        # Format the details
        details = f"""\
{'='*50}
{element['name']} ({element['symbol']}) - Atomic Number: {element['atomic_number']}
{'='*50}

Atomic Weight: {element['atomic_weight']}
Category: {element['category']}
Group: {element['group'] if element['group'] else 'N/A'}
Period: {element['period']}
Block: {element['block']}
State at STP: {element['state']}

Physical Properties:
  • Melting Point: {element['melting_point']} °C
  • Boiling Point: {element['boiling_point']} °C
  • Density: {element['density']} g/cm³

Electronic Configuration:
  • {element['electron_config']}
  • Electronegativity: {element['electronegativity'] if element['electronegativity'] else 'N/A'}

Discovery:
  • Discovered by: {element['discoverer']}
  • Year: {element['year']}
"""
        self.details_text.insert(tk.END, details)
        self.details_text.config(state=tk.DISABLED)
    
    def on_search_changed(self, event):
        """Handle search functionality."""
        query = self.search_var.get().strip().lower()
        
        if not query:
            self.display_periodic_table()
            return
        
        # Search by symbol or name
        found_elements = []
        for elem in get_all_elements():
            if query in elem["symbol"].lower() or query in elem["name"].lower():
                found_elements.append(elem)
        
        # Clear the table and show only matching elements
        for widget in self.table_frame.winfo_children():
            widget.destroy()
            
        if not found_elements:
            tk.Label(self.table_frame, text="No elements found", bg="#f0f0f0").pack()
            return
        
        # Display found elements in a grid
        row_frame = tk.Frame(self.table_frame, bg="#f0f0f0")
        row_frame.pack()
        
        for i, element in enumerate(found_elements):
            if i > 0 and i % 8 == 0:
                row_frame = tk.Frame(self.table_frame, bg="#f0f0f0")
                row_frame.pack()
            self.create_element_button(row_frame, element)