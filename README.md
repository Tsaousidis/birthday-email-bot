# 🎉 Birthday Email Automation Bot

This Python script automatically sends personalized birthday emails based on a list of birthdays stored in a CSV file. It randomly selects a letter template, replaces the placeholder with the recipient's name, and sends an email to wish them a happy birthday!

## ✨ Features
- Reads birthdays from a CSV file
- Randomly selects one of three pre-written email templates
- Sends personalized birthday emails automatically
- Uses environment variables for secure email credentials
- Implements logging and error handling

## 📌 Setup & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Tsaousidis/birthday-email-bot.git
cd birthday-email-bot
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install the required package:
```bash
pip install pandas python-dotenv
```

### 3️⃣ Configure Email Credentials
Create a `.env` file in the project root and add:
```plaintext
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_email_password
```
💡 *Tip: Do not share your `.env` file! Add it to `.gitignore`.*

### 4️⃣ Prepare Your Data
- Edit `birthdays.csv` with columns: `name`, `email`, `month`, `day`
- Ensure `letter_templates/letter_1.txt`, `letter_2.txt`, and `letter_3.txt` exist.

### 5️⃣ Run the Script
```bash
python main.py
```

## 🛠️ Requirements
- Python 3+
- `pandas`
- `dotenv`

## 🚀 Technologies Used
- **Python** for scripting
- **pandas** for CSV handling
- **smtplib** for sending emails
- **dotenv** for secure credential management

## 👨‍💻 Created by [Tsaousidis](https://github.com/Tsaousidis)  
🎉 Have fun using this bot! Let me know your thoughts and suggestions! 🎉

