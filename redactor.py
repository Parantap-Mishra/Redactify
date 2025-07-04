import re #regex module
import os
import uuid
import pandas as pd #reads csv file
import spacy

nlp = spacy.load("en_core_web_sm")

# Regex patterns
REGEX_PATTERNS = [
    (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[REDACTED]'),  # EMAIL
    (r'\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b', '[REDACTED]'),                # phone numbers
    (r'(?i)(name|username)\s*[:=]?\s*[A-Za-z0-9_.-]+', r'\1: [REDACTED]'),  # labelled names & usernames
    (r'\b\d{2}[-/]\d{2}[-/]\d{4}\b', '[REDACTED]')                      # DD-MM-YYYY / DD/MM/YYYY

]

# regex redaction
def regex(text):
    for pattern, repl in REGEX_PATTERNS:
        text = re.sub(pattern, repl, text) #replaces pattern with replacement txt in 'text'
    return text

# spacy redaction
def sp(text):
    doc = nlp(text)
    for ent in doc.ents: #looping through all entities in the text
        if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]:
            text = text.replace(ent.text, "[REDACTED]")
    return text

# Main function
def redact_file(file_path):
    file_ext = os.path.splitext(file_path)[-1].lower()
    
    # Redacted file path
    redacted_filename = f"redacted_{uuid.uuid4()}{file_ext}"
    redacted_path = os.path.join("uploads", redacted_filename)

    if file_ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        text = regex(text)
        text = sp(text)

        with open(redacted_path, 'w', encoding='utf-8') as f:
            f.write(text)

    elif file_ext == ".csv":
        df = pd.read_csv(file_path, dtype=str)
        df = df.fillna("")

        for col in df.columns:
            df[col] = df[col].apply(lambda x: sp(regex(str(x))))

        df.to_csv(redacted_path, index=False) #writes redacted data into csv

    else:
        raise ValueError("Unsupported file type!")

    return redacted_path
