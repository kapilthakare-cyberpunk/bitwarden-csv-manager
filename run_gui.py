#!/usr/bin/env python3
"""
Bitwarden CSV Manager - GUI Launcher
Simple script to launch the GUI application
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from gui_app import main
    main()
except ImportError as e:
    print(f"Error importing GUI application: {e}")
    print("Make sure you have pandas installed: pip install pandas")
    sys.exit(1)
except Exception as e:
    print(f"Error running application: {e}")
    sys.exit(1)
