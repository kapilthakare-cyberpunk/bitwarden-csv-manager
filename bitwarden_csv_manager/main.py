import pandas as pd
import os

def load_data(file_path):
    """Loads data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

def filter_data(df, column, value):
    """Filters the DataFrame based on a column and value."""
    return df[df[column].str.contains(value, case=False, na=False)]

def export_data(df, file_path):
    """Exports the DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)
    print(f"Data exported successfully to {file_path}")

def get_user_filter(df):
    """Gets filtering criteria from the user."""
    print("\nAvailable columns:")
    for col in df.columns:
        print(f"- {col}")
    
    column = input("Enter the column to filter by: ")
    if column not in df.columns:
        print("Invalid column.")
        return None, None
        
    value = input(f"Enter the value to search for in '{column}': ")
    return column, value

def main():
    """Main function to run the application."""
    print("⚠️  SECURITY WARNING: Never commit actual password files to version control!")
    print("Place your Bitwarden export CSV file in this directory and update the filename below.\n")
    
    # Update this filename to match your actual Bitwarden export
    csv_file = 'your_bitwarden_export.csv'  # ← Change this to your file's name
    
    if not os.path.exists(csv_file):
        print(f"❌ File '{csv_file}' not found!")
        print("\n📋 Instructions:")
        print("1. Export your data from Bitwarden as CSV")
        print("2. Place the file in this directory") 
        print("3. Update the 'csv_file' variable in this script with the correct filename")
        print("4. NEVER commit the actual password file to git!")
        return
    
    df = load_data(csv_file)

    if df is not None:
        print("CSV file loaded successfully.")
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Filter data and export")
            print("2. Export entire database in ideal format")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                column, value = get_user_filter(df)
                
                if column and value:
                    filtered_df = filter_data(df, column, value)
                    print(f"\nFound {len(filtered_df)} results:")
                    print(filtered_df)
                    
                    if not filtered_df.empty:
                        export = input("\nExport these results to a new CSV? (y/n): ").lower()
                        if export == 'y':
                            export_filename = input("Enter a filename for the export (e.g., 'export.csv'): ")
                            export_data(filtered_df, export_filename)
            
            elif choice == '2':
                ideal_format_file = 'ideal_bitwarden_export.csv'
                output_filename = 'formatted_export.csv'
                
                try:
                    ideal_df = pd.read_csv(ideal_format_file)
                    ideal_columns = ideal_df.columns.tolist()
                    
                    # Reindex the dataframe with the ideal columns
                    # This will add missing columns with NaN and reorder existing ones.
                    formatted_df = df.reindex(columns=ideal_columns)
                    
                    export_data(formatted_df, output_filename)
                except FileNotFoundError:
                    print(f"Error: Ideal format file '{ideal_format_file}' not found.")

            elif choice == '3':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
