


# 📚 Citation Style Detector Web App 

A simple web app built with **Flask** and **Tailwind CSS** that helps researchers detect citation styles from multiple references. Paste your citations, view each style in tabs, and get a quick summary — all with a clean and responsive interface! 🚀

---

## ✨ Features

- 🔍 Detects popular citation styles like APA, MLA, Chicago, IEEE using regex patterns  
- 📝 Paste multiple citations at once (one per line)  
- 🗂️ Tabbed interface to browse citations individually  
- 📊 Summary showing counts of each detected citation style  
- 🎨 Stylish UI powered by Tailwind CSS CDN (no build tools needed)  

---

## 💻 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/lakhimself/citation-style-detector.git
   cd citation-style-detector

3. Install dependencies:

   ```bash
   pip install Flask
   ```

---

## 🚀 Usage

1. Run the app:

   ```bash
   python app.py
   ```

2. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

3. Paste your citations (one per line).

4. Click **Detect Styles**.

5. Click tabs to view each citation and its detected style.

---

## 🗂️ Project Structure

```
citation-style-detector/
│
├── app.py               # Flask backend
├── patterns.py          # Citation regex patterns
├── templates/
│   └── index.html       # Frontend with tab UI
└── README.md            # This file
```

---

## 📷 Screenshot



---

## 🧠 How It Works

* Regex-based detection of common citation formats
* Tab UI for easy citation navigation
* Tailwind CSS for modern, responsive styling

---
