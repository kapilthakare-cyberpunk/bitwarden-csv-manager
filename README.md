# Bitwarden CSV Data Management Tool

This project provides both command-line and GUI tools to manage and filter data from Bitwarden CSV exports. It helps you format, filter, and export password data safely and efficiently.

## ⚠️ SECURITY WARNING

**NEVER commit actual password files to version control!** This tool is designed to work with your personal Bitwarden exports locally. Your actual password database should remain private and secure.

## 🎯 Features

- **🖥️ User-Friendly GUI** - Easy-to-use graphical interface
- **💻 Command-Line Interface** - For advanced users and automation
- **🔍 Smart Filtering** - Filter data by any column with case-insensitive search
- **✨ Perfect Formatting** - Auto-format exports for seamless Bitwarden import
- **🔒 Local Processing** - All data stays on your computer
- **📊 Data Preview** - View your data before processing
- **⚡ Fast Performance** - Handle large datasets efficiently

## 🚀 Quick Start (GUI - Recommended)

1. **Install dependencies:**
   ```bash
   pip install pandas
   ```

2. **Launch the GUI:**
   ```bash
   python gui_app.py
   ```
   Or use the launcher:
   ```bash
   python run_gui.py
   ```

3. **Use the application:**
   - Click "Browse for CSV File" to select your Bitwarden export
   - Preview your data
   - Use "Filter Data" to search and filter entries
   - Click "Format for Bitwarden" to create a perfectly formatted export

## 💻 Command Line Usage

For advanced users who prefer the command line:

1. **Update the filename** in `app.py`:
   ```python
   csv_file = 'your_actual_export_filename.csv'  # Update this line
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

## 📋 Requirements

- Python 3.7+
- pandas library
- tkinter (included with Python)

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/kapilthakare-cyberpunk/bitwarden-csv-manager.git

# Navigate to the directory
cd bitwarden-csv-manager

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python gui_app.py
```

## 📁 Files Structure

- `gui_app.py` - **Main GUI application** (recommended)
- `app.py` - Command-line version
- `run_gui.py` - Simple GUI launcher
- `requirements.txt` - Python dependencies
- `sample_bitwarden_export.csv` - Example file format (safe dummy data)
- `ideal_bitwarden_export.csv` - Template for ideal export format

## 🎯 GUI Features

### 🔍 Filter Data
- Search by any column (name, folder, URI, etc.)
- Case-sensitive or case-insensitive search
- Instant preview of filtered results
- Save filtered data to new CSV

### ✨ Format for Bitwarden
- Automatically reorder columns for perfect Bitwarden compatibility
- Handle missing columns gracefully
- Clean up data formatting
- Ready-to-import CSV output

### 📊 Data Preview
- View your password data safely
- Truncated display for security
- Column-based browsing
- Real-time record counts

## 🔒 Security Best Practices

- ✅ Use this tool locally only
- ✅ Keep your actual password exports out of version control
- ✅ Use strong, unique passwords for your Bitwarden vault
- ✅ Enable two-factor authentication on your Bitwarden account
- ✅ The GUI shows security warnings
- ❌ Never share your actual password database
- ❌ Never commit real password files to git repositories
- ❌ Never upload password files to online services

## 🆘 Troubleshooting

### GUI Won't Start
```bash
# Make sure you have tkinter installed (usually comes with Python)
python -c "import tkinter; print('tkinter available')"

# Install pandas if missing
pip install pandas
```

### "No module named pandas"
```bash
pip install pandas
```

### File Won't Load
- Ensure your CSV file is a valid Bitwarden export
- Check that the file isn't corrupted
- Verify file permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
