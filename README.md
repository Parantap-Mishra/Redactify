## Redactify: Basic Idea

The Data Minimization Scanner is a Python + Flask-based web application that allows users to upload .txt or .csv files containing personal or sensitive information. The tool intelligently scans and redacts personally identifiable information (PII) such as names, emails, phone numbers, addresses, and organizations

| Type of PII             | Method     | Tool               |
| ----------------------- | ---------- | ------------------ |
| Email Addresses         | Pattern    | Regex              |
| Phone Numbers           | Pattern    | Regex              |
| Usernames (label-based) | Pattern    | Regex              |
| Names                   | Contextual | `spaCy` (`PERSON`) |
| Organizations           | Contextual | `spaCy` (`ORG`)    |
| Locations / Addresses   | Contextual | `spaCy` (`GPE`)    |
| Dates / DOB             | Contextual | `spaCy` (`DATE`)   |



App Workflow

1. User Uploads File (.txt or .csv)

2. File is read and scanned for PII using:
   - Regex for structured patterns (emails, phones, etc.)
   - spaCy NLP for contextual PII (names, orgs, dates, etc.)
3. Detected information is replaced with [REDACTED]
4. A cleaned file is generated and returned for download.

