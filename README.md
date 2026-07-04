# 🦸 AI Alter Ego Generator

An AI-powered web application built with **Django** and **Groq LLM** that generates a unique superhero alter ego based on the user's name and hobby.

---

## 🚀 Features

- ✨ AI-generated superhero identity
- 🎭 Unique avatar emoji
- ⚡ Super power generation
- 💪 Three superhero strengths
- 👿 Arch enemy generation
- 🔥 Catchphrase generation
- ⚠ Weakness generation
- 🌍 Mission generation
- 📋 Copy result to clipboard
- 📄 Download Alter Ego as PDF
- 🔄 Reset form
- 🎨 Modern responsive UI

---

## 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3
- JavaScript
- Groq API
- ReportLab (PDF Generation)

---

## 📂 Project Structure

```
AI_Alter_Ego/
│
├── alterego/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── config/
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Alter_Ego.git
```

Move into the project

```bash
cd AI_Alter_Ego
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GROQ_API_KEY=your_groq_api_key_here
```

> Never upload your `.env` file to GitHub.

---

## ▶️ Run the Project

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000
```

---

## 📄 PDF Export

The application allows users to download their generated superhero profile as a PDF using ReportLab.

---

## 📸 Screenshots

Add screenshots here after deployment.

Example:

```
screenshots/home.png

screenshots/result.png
```

---

## 🌟 Future Improvements

- AI image generation
- Multiple superhero themes
- Dark / Light mode
- User login
- Save previous alter egos
- Share on social media
- Voice input
- Multi-language support

---

## 👨‍💻 Author

Jessica Shalyn

---

## 📜 License

This project is developed for educational and portfolio purposes.