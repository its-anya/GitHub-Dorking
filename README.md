# GitHub Dorking

A comprehensive collection of GitHub dorking patterns for security research and penetration testing.

## What is GitHub Dorking?

GitHub Dorking is the practice of using advanced search operators (dorks) to find sensitive information, vulnerabilities, and misconfigurations in GitHub repositories. These dorks can help security researchers identify:

- API keys and secrets
- Passwords and credentials
- Configuration files with sensitive data
- Vulnerable code patterns
- Internal documentation

## Repository Organization

This repository is organized into the following directories:

- `docs/` - Documentation and guides
- `scripts/` - Helper scripts for working with dorks
- Root directory contains the main dorking file and essential project files

## Usage

The [GitHub Dorking.txt](GitHub%20Dorking.txt) file contains hundreds of dorking patterns organized by categories:

- API Keys and Secrets
- Authentication Credentials
- Configuration Files
- Database Connections
- Cloud Service Keys
- And many more

### Documentation

See the [docs/](docs/) directory for comprehensive guides:
- [GitHub Dorking Guide](docs/GITHUB_DORKING_GUIDE.md) - Complete usage guide
- [Dork Categories Explained](docs/DORK_CATEGORIES_EXPLAINED.md) - Detailed category explanations
- [Responsible Dorking](docs/RESPONSIBLE_DORKING.md) - Ethical usage guidelines
- [Top Dorks](docs/TOP_DORKS.md) - Most effective dorking patterns
- [Usage Guide](docs/USAGE.md) - Detailed usage instructions

### Helper Scripts

See the [scripts/](scripts/) directory for helper tools:
- [dorking_helper.py](scripts/dorking_helper.py) - Cross-platform Python script
- [dorking_helper.bat](scripts/dorking_helper.bat) - Windows batch script
- [dorking_helper.sh](scripts/dorking_helper.sh) - Linux/Mac shell script

### Example Dorks

```
filename:.env DB_USERNAME NOT homestead
extension:sql mysql dump
filename:wp-config.php
filename:.htpasswd
filename:.aws/credentials
```

## Legal Disclaimer

This repository is for educational and ethical security research purposes only. Users are responsible for ensuring they have proper authorization before searching for sensitive information in any repositories. Misuse of these techniques may constitute unauthorized access to computer systems, which is illegal.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest new dorking patterns or improvements to existing ones.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.