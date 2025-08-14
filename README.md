# Bitwarden CSV Data Management Tool

This project is a Python application to manage and filter data from Bitwarden CSV exports. It provides functionalities to load, filter, and export password data in various formats.

## Features

- Load data from Bitwarden CSV export files
- Filter data based on user-defined criteria (by any column)
- Export filtered data to new CSV files
- Reformat exports to match ideal Bitwarden import format
- Interactive command-line interface

## Requirements

- Python 3.7+
- pandas

## Setup

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Ensure your Bitwarden export file is named `bitwarden_export_final_backup_20250807131034.csv` or update the filename in `app.py`

3. Run the application:

   ```bash
   python app.py
   ```

## Usage

The application provides three main options:

1. **Filter and Export**: Search through your password database by any column (name, login_uri, folder, etc.) and export matching results
2. **Export in Ideal Format**: Reformat your entire database to match the ideal Bitwarden import structure
3. **Exit**: Close the application

## Files

- `app.py` - Main application script
- `requirements.txt` - Python dependencies
- `bitwarden_export_final_backup_20250807131034.csv` - Your Bitwarden export (input)
- `ideal_bitwarden_export.csv` - Template for ideal export format
- `formatted_export.csv` - Output file for reformatted exports
