import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import os
from pathlib import Path


class BitwardenCSVManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitwarden CSV Manager")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.input_file = None
        self.output_file = None
        self.df = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=10, padx=20, fill='x')
        
        title_label = ttk.Label(
            title_frame,
            text="🔐 Bitwarden CSV Manager",
            font=("Helvetica", 18, "bold")
        )
        title_label.pack()
        
        subtitle_label = ttk.Label(
            title_frame,
            text="Format and filter your password exports safely",
            font=("Helvetica", 10)
        )
        subtitle_label.pack()
        
        # Security warning
        warning_frame = ttk.LabelFrame(self.root, text="⚠️ Security Notice", padding=10)
        warning_frame.pack(pady=10, padx=20, fill='x')
        
        warning_text = (
            "• Your password data stays LOCAL on your computer\n"
            "• Files are processed locally - nothing is uploaded to the internet\n"
            "• Always keep your password files secure and private"
        )
        warning_label = ttk.Label(warning_frame, text=warning_text, foreground='red')
        warning_label.pack(anchor='w')
        
        # File input section
        input_frame = ttk.LabelFrame(self.root, text="📁 Select Your Bitwarden Export", padding=10)
        input_frame.pack(pady=10, padx=20, fill='x')
        
        input_button_frame = ttk.Frame(input_frame)
        input_button_frame.pack(fill='x')
        
        self.select_button = ttk.Button(
            input_button_frame,
            text="Browse for CSV File",
            command=self.select_input_file,
            width=20
        )
        self.select_button.pack(side='left', padx=(0, 10))
        
        self.input_label = ttk.Label(input_button_frame, text="No file selected")
        self.input_label.pack(side='left', anchor='w')
        
        # Action buttons section
        action_frame = ttk.LabelFrame(self.root, text="🔧 Actions", padding=10)
        action_frame.pack(pady=10, padx=20, fill='x')
        
        button_frame = ttk.Frame(action_frame)
        button_frame.pack()
        
        self.preview_button = ttk.Button(
            button_frame,
            text="👀 Preview Data",
            command=self.preview_data,
            state='disabled',
            width=15
        )
        self.preview_button.pack(side='left', padx=5)
        
        self.filter_button = ttk.Button(
            button_frame,
            text="🔍 Filter Data",
            command=self.open_filter_window,
            state='disabled',
            width=15
        )
        self.filter_button.pack(side='left', padx=5)
        
        self.format_button = ttk.Button(
            button_frame,
            text="✨ Format for Bitwarden",
            command=self.format_for_bitwarden,
            state='disabled',
            width=18
        )
        self.format_button.pack(side='left', padx=5)
        
        # Results section
        results_frame = ttk.LabelFrame(self.root, text="📊 Data Preview", padding=10)
        results_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Create treeview for data display
        self.tree_frame = ttk.Frame(results_frame)
        self.tree_frame.pack(fill='both', expand=True)
        
        # Scrollbars
        tree_scroll_v = ttk.Scrollbar(self.tree_frame, orient='vertical')
        tree_scroll_h = ttk.Scrollbar(self.tree_frame, orient='horizontal')
        
        self.tree = ttk.Treeview(
            self.tree_frame,
            yscrollcommand=tree_scroll_v.set,
            xscrollcommand=tree_scroll_h.set
        )
        
        tree_scroll_v.config(command=self.tree.yview)
        tree_scroll_h.config(command=self.tree.xview)
        
        tree_scroll_v.pack(side='right', fill='y')
        tree_scroll_h.pack(side='bottom', fill='x')
        self.tree.pack(side='left', fill='both', expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Select a CSV file to begin")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief='sunken')
        status_bar.pack(side='bottom', fill='x', padx=5, pady=2)
        
    def select_input_file(self):
        """Open file dialog to select input CSV file."""
        file_path = filedialog.askopenfilename(
            title="Select Bitwarden CSV Export",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            self.input_file = file_path
            self.input_label.config(text=f"Selected: {os.path.basename(file_path)}")
            self.load_data()
            
    def load_data(self):
        """Load the selected CSV file."""
        try:
            self.df = pd.read_csv(self.input_file)
            self.status_var.set(f"Loaded {len(self.df)} records from {os.path.basename(self.input_file)}")
            
            # Enable buttons
            self.preview_button.config(state='normal')
            self.filter_button.config(state='normal')
            self.format_button.config(state='normal')
            
            # Auto-preview first few rows
            self.display_data(self.df.head(10))
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")
            self.status_var.set("Error loading file")
            
    def display_data(self, df):
        """Display data in the treeview."""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if df.empty:
            return
            
        # Configure columns
        self.tree['columns'] = list(df.columns)
        self.tree['show'] = 'headings'
        
        # Configure column headings and widths
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, minwidth=50)
            
        # Insert data
        for index, row in df.iterrows():
            # Truncate long values for display
            display_row = []
            for value in row:
                str_val = str(value) if pd.notna(value) else ""
                if len(str_val) > 50:
                    str_val = str_val[:47] + "..."
                display_row.append(str_val)
            self.tree.insert('', 'end', values=display_row)
            
    def preview_data(self):
        """Show data preview."""
        if self.df is not None:
            self.display_data(self.df)
            self.status_var.set(f"Showing all {len(self.df)} records")
        else:
            messagebox.showwarning("No Data", "Please select a file first.")
            
    def open_filter_window(self):
        """Open filter dialog window."""
        if self.df is None:
            messagebox.showwarning("No Data", "Please select a file first.")
            return
            
        FilterWindow(self.root, self.df, self.apply_filter)
        
    def apply_filter(self, filtered_df):
        """Apply filter results."""
        self.display_data(filtered_df)
        self.status_var.set(f"Filtered to {len(filtered_df)} records")
        
        # Ask if user wants to save filtered results
        if messagebox.askyesno("Save Filtered Data", "Would you like to save the filtered results?"):
            self.save_data(filtered_df, "filtered_export.csv")
            
    def format_for_bitwarden(self):
        """Format the data for perfect Bitwarden compatibility."""
        if self.df is None:
            messagebox.showwarning("No Data", "Please select a file first.")
            return
            
        try:
            # Define ideal Bitwarden column order
            ideal_columns = [
                'folder', 'favorite', 'type', 'name', 'notes', 'fields',
                'reprompt', 'login_uri', 'login_username', 'login_password', 'login_totp'
            ]
            
            # Create formatted dataframe
            formatted_df = pd.DataFrame()
            
            for col in ideal_columns:
                if col in self.df.columns:
                    formatted_df[col] = self.df[col]
                else:
                    formatted_df[col] = ""  # Add missing columns as empty
                    
            # Clean up the data
            formatted_df = formatted_df.fillna("")  # Replace NaN with empty strings
            
            # Show preview
            self.display_data(formatted_df.head(10))
            self.status_var.set(f"Formatted {len(formatted_df)} records for Bitwarden import")
            
            # Save formatted data
            output_file = filedialog.asksaveasfilename(
                title="Save Formatted CSV",
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv")],
                initialvalue="bitwarden_formatted_export.csv"
            )
            
            if output_file:
                formatted_df.to_csv(output_file, index=False)
                messagebox.showinfo(
                    "Success",
                    f"Formatted CSV saved successfully!\n\n"
                    f"File: {os.path.basename(output_file)}\n"
                    f"Records: {len(formatted_df)}\n\n"
                    f"This file is ready for import into Bitwarden."
                )
                self.status_var.set(f"Saved formatted export: {os.path.basename(output_file)}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to format data:\n{str(e)}")
            
    def save_data(self, df, default_name):
        """Save dataframe to CSV file."""
        output_file = filedialog.asksaveasfilename(
            title="Save CSV",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialvalue=default_name
        )
        
        if output_file:
            df.to_csv(output_file, index=False)
            messagebox.showinfo("Success", f"Data saved to {os.path.basename(output_file)}")


class FilterWindow:
    def __init__(self, parent, df, callback):
        self.df = df
        self.callback = callback
        
        # Create window
        self.window = tk.Toplevel(parent)
        self.window.title("Filter Data")
        self.window.geometry("400x300")
        self.window.grab_set()  # Make modal
        
        self.setup_filter_ui()
        
    def setup_filter_ui(self):
        """Set up filter dialog UI."""
        # Title
        title_label = ttk.Label(self.window, text="🔍 Filter Your Data", font=("Helvetica", 14, "bold"))
        title_label.pack(pady=10)
        
        # Column selection
        col_frame = ttk.LabelFrame(self.window, text="Select Column", padding=10)
        col_frame.pack(pady=10, padx=20, fill='x')
        
        self.column_var = tk.StringVar()
        self.column_combo = ttk.Combobox(col_frame, textvariable=self.column_var, state='readonly')
        self.column_combo['values'] = list(self.df.columns)
        self.column_combo.pack(fill='x')
        
        # Search value
        search_frame = ttk.LabelFrame(self.window, text="Search Value", padding=10)
        search_frame.pack(pady=10, padx=20, fill='x')
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(fill='x')
        
        # Options
        options_frame = ttk.LabelFrame(self.window, text="Options", padding=10)
        options_frame.pack(pady=10, padx=20, fill='x')
        
        self.case_sensitive_var = tk.BooleanVar()
        case_check = ttk.Checkbutton(options_frame, text="Case sensitive", variable=self.case_sensitive_var)
        case_check.pack(anchor='w')
        
        # Buttons
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=20)
        
        filter_button = ttk.Button(button_frame, text="Apply Filter", command=self.apply_filter)
        filter_button.pack(side='left', padx=5)
        
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.window.destroy)
        cancel_button.pack(side='left', padx=5)
        
    def apply_filter(self):
        """Apply the filter and return results."""
        column = self.column_var.get()
        search_value = self.search_var.get()
        
        if not column or not search_value:
            messagebox.showwarning("Missing Information", "Please select a column and enter a search value.")
            return
            
        try:
            # Apply filter
            case_sensitive = self.case_sensitive_var.get()
            filtered_df = self.df[
                self.df[column].astype(str).str.contains(
                    search_value, 
                    case=case_sensitive, 
                    na=False
                )
            ]
            
            if filtered_df.empty:
                messagebox.showinfo("No Results", "No records match your filter criteria.")
                return
                
            # Return results
            self.callback(filtered_df)
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply filter:\n{str(e)}")


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = BitwardenCSVManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
