#!/bin/bash

# GitHub Dorking Helper Script for Linux/Mac

# Check if required files exist
if [[ ! -f "GitHub Dorking.txt" ]]; then
    echo "Error: GitHub Dorking.txt file not found!"
    echo "Please ensure you're running this script from the correct directory."
    exit 1
fi

echo "GitHub Dorking Helper"
echo "===================="
echo

echo "Select an option:"
echo "1. List all dorks"
echo "2. Search for dorks containing a keyword"
echo "3. Show dork categories"
echo "4. Count total dorks"
echo "5. Open GitHub Dorking.txt in default editor"
echo

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo
        echo "All GitHub Dorking Patterns:"
        echo "=========================="
        cat "GitHub Dorking.txt"
        ;;
    2)
        read -p "Enter keyword to search for: " keyword
        echo
        echo "Dorks containing '$keyword':"
        echo "========================"
        grep -i "$keyword" "GitHub Dorking.txt"
        ;;
    3)
        echo
        echo "Dork Categories:"
        echo "==============="
        echo "API Keys and Secrets"
        echo "Authentication Credentials"
        echo "Configuration Files"
        echo "Database Connections"
        echo "Cloud Services"
        echo "Communication Services"
        echo "Development Tools"
        echo "Financial Services"
        echo "Social Media"
        echo "File Types"
        echo "Filename Based"
        echo "Path Based"
        echo "Content Based"
        echo "Framework Specific"
        ;;
    4)
        echo
        count=$(wc -l < "GitHub Dorking.txt")
        echo "Total dorks: $count"
        ;;
    5)
        # Try different editors based on availability
        if command -v nano &> /dev/null; then
            nano "GitHub Dorking.txt"
        elif command -v vim &> /dev/null; then
            vim "GitHub Dorking.txt"
        elif command -v vi &> /dev/null; then
            vi "GitHub Dorking.txt"
        else
            echo "No suitable text editor found. Please open GitHub Dorking.txt manually."
        fi
        ;;
    *)
        echo "Invalid choice. Please run the script again and select 1-5."
        ;;
esac

echo
read -p "Press Enter to continue..."