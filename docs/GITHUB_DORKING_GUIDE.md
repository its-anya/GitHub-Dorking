# Complete Guide to GitHub Dorking Patterns

This guide explains how to use each pattern in the GitHub Dorking.txt file for security research purposes.

## Legal Disclaimer

This guide is for educational and ethical security research only. Always ensure you have proper authorization before searching for sensitive information in any repositories. Unauthorized access to computer systems is illegal.

## How to Use GitHub Dorks

1. Go to https://github.com
2. Use the search bar at the top
3. Enter any pattern from this guide
4. Press Enter to see results

## Pattern Categories and Examples

### 1. API Keys and Secrets

These patterns search for API keys, secrets, and tokens from various services.

Examples:
- `"api_key"` - Finds files containing the term "api_key"
- `"aws_access_key_id"` - Locates AWS access keys
- `"github_token"` - Finds GitHub tokens
- `"firebase" "config"` - Finds Firebase configuration files

Usage: These help identify exposed API credentials that could be misused.

### 2. Authentication Credentials

Patterns that look for usernames, passwords, and authentication information.

Examples:
- `"password"` - Finds files containing passwords
- `"passwd"` - Alternative password search
- `"credentials"` - General credentials search
- `"db_password"` - Database passwords

Usage: These can reveal login credentials that should be kept secure.

### 3. Configuration Files

Search patterns for configuration files that may contain sensitive settings.

Examples:
- `filename:.env` - Finds .env files (often contain secrets)
- `filename:config` - Finds configuration files
- `filename:settings` - Finds settings files
- `filename:wp-config.php` - WordPress configuration files

Usage: Configuration files often contain database credentials, API keys, and other sensitive information.

### 4. Database Connections

Dorks targeting database connection strings and credentials.

Examples:
- `"database_password"` - Database passwords
- `"mysql dump"` - MySQL database dumps
- `"postgresql"` - PostgreSQL connections
- `"mongodb"` - MongoDB connections

Usage: These can expose database credentials that could lead to data breaches.

### 5. Cloud Services

Patterns specific to cloud platforms like AWS, Azure, Google Cloud, etc.

Examples:
- `"aws_secret"` - AWS secrets
- `"azure"` - Azure configurations
- `"google cloud"` - Google Cloud configurations
- `"herokuapp"` - Heroku configurations

Usage: Cloud service credentials can provide access to entire infrastructure environments.

### 6. File Extensions

Dorks that search for specific file extensions that may contain sensitive information.

Examples:
- `extension:pem` - Finds .pem files (often private keys)
- `extension:ppk` - Finds .ppk files (PuTTY private keys)
- `extension:sql` - Finds .sql files (database dumps)
- `extension:cfg` - Finds .cfg files (configuration files)

Usage: Certain file types are more likely to contain sensitive data.

### 7. Specific Filenames

Patterns that search for files with specific names known to contain sensitive data.

Examples:
- `filename:.htpasswd` - Finds .htpasswd files
- `filename:id_rsa` - Finds private SSH keys
- `filename:.bashrc` - Finds bash configuration files
- `filename:robomongo.json` - Finds Robomongo configuration files

Usage: These target files that are known to contain sensitive information.

### 8. Communication Services

Dorks for finding credentials related to messaging and communication platforms.

Examples:
- `"slack_token"` - Slack API tokens
- `"twilio" "token"` - Twilio API tokens
- `"sendgrid" "api"` - SendGrid API keys
- `"mailgun" "key"` - Mailgun API keys

Usage: These can expose communication service credentials that could be used for spam or phishing.

### 9. Development Tools

Patterns for development tools and their configuration files.

Examples:
- `filename:.npmrc _auth` - NPM authentication tokens
- `filename:.dockercfg auth` - Docker configuration files
- `filename:filezilla.xml Pass` - FileZilla configuration files
- `filename:recentservers.xml Pass` - Recent server connection files

Usage: Development tools often store credentials in configuration files.

### 10. Financial Services

Dorks that may reveal financial service API keys or credentials.

Examples:
- `"stripe" "key"` - Stripe API keys
- `"paypal" "client"` - PayPal client credentials
- `"braintree" "key"` - Braintree API keys

Usage: These can expose payment processing credentials that could lead to financial fraud.

## Advanced Search Techniques

### Combining Terms
You can combine multiple terms for more specific searches:
- `filename:.env AWS_SECRET` - Finds .env files containing AWS secrets
- `extension:sql mysql dump password` - Finds SQL dumps with passwords
- `filename:config.json "api_key"` - Finds config.json files with API keys

### Exclusion Patterns
You can exclude terms to filter results:
- `extension:sql mysql dump NOT test` - Finds SQL dumps but excludes test files
- `"password" NOT example` - Finds password references but excludes examples

### Language Filters
You can filter by programming language:
- `"api_key" language:python` - Finds API keys in Python files
- `"password" language:javascript` - Finds passwords in JavaScript files

## Responsible Usage Guidelines

1. Only search in repositories you own or have permission to access
2. Do not use these techniques for unauthorized access
3. Report vulnerabilities responsibly through proper channels
4. Be aware of legal implications in your jurisdiction

## Common Use Cases

1. **Security Auditing**: Checking your own repositories for accidentally committed secrets
2. **Penetration Testing**: As part of authorized security assessments
3. **Research**: Studying common security misconfigurations
4. **Education**: Learning about secure development practices

## Tools Integration

These dorking patterns can be used with:
1. GitHub Advanced Search
2. Google Dorking (site:github.com)
3. Automated tools like GitDorker
4. Custom scripts for automated searching

## Conclusion

GitHub dorking is a powerful technique for finding sensitive information in public repositories. When used responsibly, it can help improve security by identifying and fixing vulnerabilities before they can be exploited by malicious actors.

Always remember to use these techniques ethically and legally, and to report any vulnerabilities you find through appropriate channels.