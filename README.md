# GitHub Dorking

A comprehensive collection of GitHub dorking patterns for security research and penetration testing.

## What is GitHub Dorking?

GitHub Dorking is the practice of using advanced search operators (dorks) to find sensitive information, vulnerabilities, and misconfigurations in GitHub repositories. These dorks can help security researchers identify:

- API keys and secrets
- Passwords and credentials
- Configuration files with sensitive data
- Vulnerable code patterns
- Internal documentation

## Usage

The [GitHub Dorking.txt](GitHub%20Dorking.txt) file contains hundreds of dorking patterns organized by categories:

- API Keys and Secrets
- Authentication Credentials
- Configuration Files
- Database Connections
- Cloud Service Keys
- And many more

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