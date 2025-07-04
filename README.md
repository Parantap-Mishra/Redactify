## 🛡️ Redactify – Data Minimization Scanner

**Redactify** is a local Flask-based web application that scans `.txt` and `.csv` files for sensitive information and redacts it using a combination of **regular expressions** and **NLP (spaCy)**. It helps organizations minimize data exposure by only retaining essential information.

> 🧠 Example Use Case: Hospitals or clinics can use Redactify to remove patient-identifiable data from medical records before sharing them for research or AI model training.

---

### ✨ Features

* 🔍 Detects and redacts:

  * Names, organizations, locations, and dates using spaCy's NER
  * Emails, phone numbers, usernames, and formatted dates using regex
* 📄 Supports `.txt` and `.csv` files
* ⚡ Instant download of redacted file
* 🎨 Aesthetic and professional UI with drag-and-drop + file picker
* 📦 Comes with pre-configured virtual environment (`env/`)

---

### 📂 Folder Structure

```
Redactify/
├── app.py
├── redactor.py
├── uploads/                # Uploaded and redacted files
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── env/                   # Virtual environment (already configured)
├── README.md
```

---

### 🚀 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/redactify.git
   cd redactify
   ```

2. **Activate the virtual environment**

   ```bash
   # Windows
   env\Scripts\activate

   # macOS/Linux
   source env/bin/activate
   ```

3. **Run the Flask server**

   ```bash
   python app.py
   ```

4. **Open your browser** and go to
   [http://localhost:5000](http://localhost:5000)

---

### ⚙️ Dependencies (Preinstalled in `env/`)

* Flask
* spaCy (`en_core_web_sm`)
* pandas
* re (built-in)

To download the spaCy model again (if needed):

```bash
python -m spacy download en_core_web_sm
```

---

### 🧠 Learning Goals

This project was built not just to demonstrate utility but also to:

* Practice secure file handling
* Learn NLP-based entity recognition
* Implement privacy-aware design thinking
* Understand regex and named entity offsets

---

### 📌 Future Scope

* This is a **basic version** of Redactify.
* Future versions may support:

  * Image-based redaction using OCR
  * Docx and PDF file types
  * Scan summary reports (entities redacted, counts, etc.)
  * Integration with cloud storage (optional)

---

### 👨‍💻 Created By

**Parantap Mishra**
[GitHub](https://github.com/parantap-mishra) · [LinkedIn](https://linkedin.com/in/parantap-mishra)
