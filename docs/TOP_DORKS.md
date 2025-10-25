# Top GitHub Dorking Patterns

This file contains some of the most effective and commonly used GitHub dorking patterns for security research.

## Critical Security Dorks

These dorks are most likely to reveal sensitive information:

1. `filename:.env`
2. `filename:.htpasswd`
3. `filename:wp-config.php`
4. `filename:.git-credentials`
5. `filename:id_rsa`
6. `extension:sql mysql dump`
7. `extension:pem private`
8. `extension:ppk private`

## API Key Dorks

Patterns that often reveal API keys and secrets:

1. `extension:json api_key`
2. `"api_key" language:json`
3. `"aws_access_key_id" language:python`
4. `filename:.npmrc _auth`
5. `filename:.dockercfg auth`
6. `"aws_secret_access_key" language:python`
7. `filename:credentials aws_access_key_id`
8. `"github_token"`
9. `"firebase" "config"`

## Configuration File Dorks

Search for configuration files that may contain sensitive data:

1. `filename:config.json auths`
2. `filename:database.yml`
3. `filename:settings.py SECRET_KEY`
4. `filename:secrets.yml password`
5. `filename:server.cfg rcon password`
6. `filename:shadow path:etc`
7. `filename:pgpass`
8. `filename:.s3cfg`

## Cloud Service Dorks

Patterns specific to cloud platforms:

1. `HEROKU_API_KEY language:json`
2. `HEROKU_API_KEY language:shell`
3. `"aws_access_key_id" language:javascript`
4. `"aws_secret_access_key" language:javascript`
5. `filename:firebase.json`
6. `"rds.amazonaws.com password"`
7. `filename:aws.yml`
8. `filename:azure.yml`

## Database Dorks

Patterns that may reveal database credentials:

1. `"DB_PASSWORD" language:php`
2. `"DB_PASSWORD" language:python`
3. `"DB_PASSWORD" language:yaml`
4. `"database_password" language:yaml`
5. `filename:database.yml password`
6. `filename:db.conf`
7. `filename:dbconfig.php`
8. `"mysql dump password"`

## Communication Service Dorks

Patterns for communication platforms:

1. `SLACK_WEBHOOK_URL`
2. `"slack_token"`
3. `"twilio" "token"`
4. `"sendgrid" "api"`
5. `"mailgun" "key"`

## Development Tool Dorks

Patterns for development tools and environments:

1. `filename:.bashrc password`
2. `filename:.bash_profile aws`
3. `filename:.zshrc aws`
4. `filename:.ssh/config`
5. `filename:robomongo.json`
6. `filename:filezilla.xml Pass`
7. `filename:recentservers.xml Pass`
8. `filename:ventrilo_srv.ini`

## Usage Tips

1. Combine dorks for better results:
   ```
   filename:.env AWS_SECRET
   ```

2. Use exclusions to filter out test data:
   ```
   extension:sql mysql dump NOT test
   ```

3. Target specific languages when appropriate:
   ```
   "api_key" language:python
   ```

## Legal Disclaimer

These dorks are for educational and ethical security research purposes only. Always ensure you have proper authorization before searching for sensitive information in any repositories.