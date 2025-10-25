# Usage Guide

This guide explains how to effectively use the GitHub dorking patterns in this repository.

## Manual Usage

### On GitHub

1. Go to [GitHub](https://github.com)
2. Use the search bar at the top
3. Enter any dorking pattern from the list
4. Press Enter to see results

Example:
```
filename:.env DB_USERNAME NOT homestead
```

### On GitHub Search Page

1. Go to [GitHub Search](https://github.com/search)
2. Enter your dork in the search box
3. Refine results using filters

## Using the Helper Script

The repository includes a Python helper script to work with the dorking patterns:

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

## Best Practices

### Responsible Usage

1. Only search in repositories you own or have permission to access
2. Do not use these techniques for unauthorized access
3. Report vulnerabilities responsibly through proper channels
4. Be aware of legal implications in your jurisdiction

### Effective Searching

1. Combine multiple dorks for better results:
   ```
   filename:.env AWS_SECRET
   ```

2. Use exclusion patterns to filter results:
   ```
   extension:sql mysql dump NOT test
   ```

3. Target specific file types:
   ```
   extension:json api_key
   ```

### Common Patterns

1. **API Keys**: Look for service-specific keys
2. **Configuration Files**: Search for config files that might contain secrets
3. **Database Credentials**: Find database connection strings
4. **Private Keys**: Identify private key files
5. **Environment Files**: Locate .env files with credentials

## Tools Integration

These dorking patterns can be used with:

1. **GitHub Advanced Search**
2. **Google Dorking** (site:github.com)
3. **Automated tools** like GitDorker
4. **Custom scripts** for automated searching

## Legal Disclaimer

Use these dorking patterns responsibly and ethically. Unauthorized access to computer systems is illegal. Always ensure you have proper authorization before searching for sensitive information in any repositories.