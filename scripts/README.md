# Helper Scripts

This directory contains helper scripts to work with the GitHub Dorking patterns more effectively.

## Scripts in this Directory

### [dorking_helper.py](dorking_helper.py)
A cross-platform Python script that provides utilities to search, filter, and organize dorks.

Usage:
```bash
# Show all dorks
python dorking_helper.py

# Search for dorks containing a keyword
python dorking_helper.py --search "aws"

# Use regex to find matching dorks
python dorking_helper.py --regex "filename:.*config"

# Show dorks in a specific category
python dorking_helper.py --category api_keys

# List all categories
python dorking_helper.py --list-categories

# Count total dorks
python dorking_helper.py --count
```

### [dorking_helper.bat](dorking_helper.bat)
A Windows batch script for easy access to dorking patterns on Windows systems.

Usage:
1. Double-click the script or run it from Command Prompt
2. Select an option from the menu
3. Follow the prompts

### [dorking_helper.sh](dorking_helper.sh)
A shell script for Linux/Mac users to work with dorking patterns.

Usage:
1. Make the script executable: `chmod +x dorking_helper.sh`
2. Run the script: `./dorking_helper.sh`
3. Select an option from the menu

## Requirements

- Python 3.x (for dorking_helper.py)
- Windows (for dorking_helper.bat)
- Linux/Mac with bash (for dorking_helper.sh)

## Legal Reminder

These scripts are for educational and ethical security research purposes only. Users are responsible for ensuring they have proper authorization before searching for sensitive information in any repositories.