# GitHub Dorking Categories Explained

This document provides detailed explanations of each category of dorks found in the GitHub Dorking.txt file, with examples and usage instructions.

## 1. API Keys and Secrets

These dorks search for API keys, secrets, and tokens from various services.

### Common Patterns:
- `"api_key"` - General API key search
- `"aws_access_key_id"` - AWS access keys
- `"github_token"` - GitHub tokens
- `"firebase" "config"` - Firebase configuration files

### Usage:
1. Go to GitHub search
2. Enter the pattern
3. Review results for exposed credentials
4. Report findings through proper channels

### Example:
Searching for `"api_key"` might reveal configuration files containing:
```
API_KEY=sk-1234567890abcdef1234567890abcdef
```

## 2. Authentication Credentials

Patterns that look for usernames, passwords, and authentication information.

### Common Patterns:
- `"password"` - General password search
- `"passwd"` - Alternative password search
- `"credentials"` - General credentials search
- `"db_password"` - Database passwords

### Usage:
These patterns help identify login credentials that should be kept secure.

### Example:
Searching for `"password"` might reveal:
```
DB_PASSWORD=supersecretpassword123
```

## 3. Configuration Files

Search patterns for configuration files that may contain sensitive settings.

### Common Patterns:
- `filename:.env` - Environment configuration files
- `filename:config` - General configuration files
- `filename:wp-config.php` - WordPress configuration
- `filename:.htpasswd` - Apache password files

### Usage:
Configuration files often contain database credentials, API keys, and other sensitive information.

### Example:
Searching for `filename:.env` might reveal:
```
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=secretpassword
API_KEY=sk-1234567890abcdef
```

## 4. Database Connections

Dorks targeting database connection strings and credentials.

### Common Patterns:
- `"database_password"` - Database passwords
- `"mysql dump"` - MySQL database dumps
- `"postgresql"` - PostgreSQL connections
- `"mongodb"` - MongoDB connections

### Usage:
These can expose database credentials that could lead to data breaches.

### Example:
Searching for `"mysql dump"` might reveal:
```
-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: production_db
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

--
-- Current Database: `production_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `production_db` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `production_db`;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin123'),(2,'user','password123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
```

## 5. Cloud Services

Patterns specific to cloud platforms like AWS, Azure, Google Cloud, etc.

### Common Patterns:
- `"aws_secret"` - AWS secrets
- `"azure"` - Azure configurations
- `"google cloud"` - Google Cloud configurations
- `HEROKU_API_KEY` - Heroku API keys

### Usage:
Cloud service credentials can provide access to entire infrastructure environments.

### Example:
Searching for `HEROKU_API_KEY` might reveal:
```
HEROKU_API_KEY=12345678-1234-1234-1234-1234567890ab
```

## 6. File Extensions

Dorks that search for specific file extensions that may contain sensitive information.

### Common Patterns:
- `extension:pem` - Private key files
- `extension:ppk` - PuTTY private keys
- `extension:sql` - SQL database dumps
- `extension:cfg` - Configuration files

### Usage:
Certain file types are more likely to contain sensitive data.

### Example:
Searching for `extension:pem` might reveal private SSH keys:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2K... (truncated for security)
-----END RSA PRIVATE KEY-----
```

## 7. Specific Filenames

Patterns that search for files with specific names known to contain sensitive data.

### Common Patterns:
- `filename:id_rsa` - Private SSH keys
- `filename:.bashrc` - Bash configuration files
- `filename:robomongo.json` - Robomongo configuration
- `filename:filezilla.xml` - FileZilla configuration

### Usage:
These target files that are known to contain sensitive information.

### Example:
Searching for `filename:id_rsa` might reveal:
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,1234567890ABCDEF1234567890ABCDEF

... (private key data) ...
-----END RSA PRIVATE KEY-----
```

## 8. Communication Services

Dorks for finding credentials related to messaging and communication platforms.

### Common Patterns:
- `"slack_token"` - Slack API tokens
- `"twilio" "token"` - Twilio API tokens
- `"sendgrid" "api"` - SendGrid API keys
- `"mailgun" "key"` - Mailgun API keys

### Usage:
These can expose communication service credentials that could be used for spam or phishing.

### Example:
Searching for `"slack_token"` might reveal:
```
SLACK_TOKEN=xoxb-123456789012-1234567890123-1234567890abcdef12345678
```

## 9. Development Tools

Patterns for development tools and their configuration files.

### Common Patterns:
- `filename:.npmrc _auth` - NPM authentication tokens
- `filename:.dockercfg auth` - Docker configuration files
- `filename:settings.py SECRET_KEY` - Django secret keys
- `filename:secrets.yml password` - Secrets configuration

### Usage:
Development tools often store credentials in configuration files.

### Example:
Searching for `filename:.npmrc _auth` might reveal:
```
//registry.npmjs.org/:_authToken=npm_1234567890abcdef1234567890abcdef1234567890
```

## 10. Financial Services

Dorks that may reveal financial service API keys or credentials.

### Common Patterns:
- `"stripe" "key"` - Stripe API keys
- `"paypal" "client"` - PayPal client credentials
- `"braintree" "key"` - Braintree API keys

### Usage:
These can expose payment processing credentials that could lead to financial fraud.

### Example:
Searching for `"stripe" "key"` might reveal:
```
STRIPE_SECRET_KEY=sk_test_1234567890abcdef1234567890abcdef
STRIPE_PUBLISHABLE_KEY=pk_test_1234567890abcdef1234567890abcdef
```

## Advanced Techniques

### Combining Multiple Terms
You can combine multiple terms for more specific searches:
- `filename:.env AWS_SECRET` - Finds .env files containing AWS secrets
- `extension:sql mysql dump password` - Finds SQL dumps with passwords

### Using Language Filters
You can filter by programming language:
- `"api_key" language:python` - Finds API keys in Python files
- `"password" language:javascript` - Finds passwords in JavaScript files

### Excluding Terms
You can exclude terms to filter results:
- `extension:sql mysql dump NOT test` - Finds SQL dumps but excludes test files
- `"password" NOT example` - Finds password references but excludes examples

## Responsible Usage

Always remember:
1. Only search in repositories you own or have permission to access
2. Do not use these techniques for unauthorized access
3. Report vulnerabilities responsibly through proper channels
4. Be aware of legal implications in your jurisdiction

## Conclusion

Understanding these categories helps you effectively use GitHub dorking for legitimate security research. Each category targets specific types of sensitive information, making it easier to identify potential vulnerabilities in code repositories.