#!/usr/bin/env python3
"""
GitHub Dorking Helper Script

This script helps users work with the GitHub dorking patterns
by providing utilities to search, filter, and organize dorks.
"""

import argparse
import re
import sys
from typing import List, Dict


def load_dorks(file_path: str) -> List[str]:
    """Load dorking patterns from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Filter out empty lines and comments
            dorks = [line.strip() for line in f.readlines() 
                    if line.strip() and not line.startswith('#')]
        return dorks
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def filter_dorks(dorks: List[str], keyword: str) -> List[str]:
    """Filter dorks containing a specific keyword."""
    return [dork for dork in dorks if keyword.lower() in dork.lower()]


def categorize_dorks(dorks: List[str]) -> Dict[str, List[str]]:
    """Categorize dorks based on common patterns."""
    categories = {
        'api_keys': [],
        'passwords': [],
        'config_files': [],
        'database': [],
        'cloud': [],
        'tokens': [],
        'credentials': [],
        'extensions': [],
        'filenames': [],
        'other': []
    }
    
    for dork in dorks:
        dork_lower = dork.lower()
        if any(term in dork_lower for term in ['api', 'key', 'secret', 'token']) and 'api' in dork_lower:
            categories['api_keys'].append(dork)
        elif any(term in dork_lower for term in ['pass', 'pwd', 'secret']):
            categories['passwords'].append(dork)
        elif 'filename:' in dork_lower:
            categories['filenames'].append(dork)
        elif 'extension:' in dork_lower:
            categories['extensions'].append(dork)
        elif any(term in dork_lower for term in ['config', 'settings', 'env']):
            categories['config_files'].append(dork)
        elif any(term in dork_lower for term in ['database', 'db_', 'db.', 'mysql', 'postgres']):
            categories['database'].append(dork)
        elif any(term in dork_lower for term in ['aws', 'azure', 'cloud', 's3', 'gcp']):
            categories['cloud'].append(dork)
        elif 'token' in dork_lower:
            categories['tokens'].append(dork)
        elif any(term in dork_lower for term in ['credential', 'auth', 'login']):
            categories['credentials'].append(dork)
        else:
            categories['other'].append(dork)
    
    return categories


def search_dorks(dorks: List[str], pattern: str) -> List[str]:
    """Search for dorks matching a regex pattern."""
    try:
        regex = re.compile(pattern, re.IGNORECASE)
        return [dork for dork in dorks if regex.search(dork)]
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="GitHub Dorking Helper")
    parser.add_argument('--file', '-f', default='GitHub Dorking.txt',
                        help='Path to dorking patterns file')
    parser.add_argument('--search', '-s', 
                        help='Search for dorks containing keyword')
    parser.add_argument('--regex', '-r',
                        help='Search for dorks matching regex pattern')
    parser.add_argument('--category', '-c',
                        help='Show dorks from a specific category')
    parser.add_argument('--list-categories', action='store_true',
                        help='List all available categories')
    parser.add_argument('--count', action='store_true',
                        help='Show count of dorks')
    
    args = parser.parse_args()
    
    dorks = load_dorks(args.file)
    
    if args.count:
        print(f"Total dorks: {len(dorks)}")
        return
    
    if args.list_categories:
        categories = categorize_dorks(dorks)
        print("Available categories:")
        for category in categories.keys():
            print(f"  - {category} ({len(categories[category])} dorks)")
        return
    
    if args.search:
        filtered_dorks = filter_dorks(dorks, args.search)
        print(f"Dorks containing '{args.search}':")
        for dork in filtered_dorks:
            print(dork)
        return
    
    if args.regex:
        matched_dorks = search_dorks(dorks, args.regex)
        print(f"Dorks matching pattern '{args.regex}':")
        for dork in matched_dorks:
            print(dork)
        return
    
    if args.category:
        categories = categorize_dorks(dorks)
        if args.category in categories:
            print(f"Dorks in category '{args.category}':")
            for dork in categories[args.category]:
                print(dork)
        else:
            print(f"Category '{args.category}' not found.")
            print("Available categories:")
            for category in categories.keys():
                print(f"  - {category}")
        return
    
    # Default: show all dorks
    print("All GitHub Dorking Patterns:")
    for dork in dorks:
        print(dork)


if __name__ == "__main__":
    main()