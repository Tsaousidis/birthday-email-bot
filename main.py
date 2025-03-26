
from datetime import datetime
import pandas as pd
import random
import smtplib
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        # Create a tuple from today's month and day
        now = datetime.now()
        today = (now.month, now.day)

        # Read the birthdays.csv
        data = pd.read_csv("birthdays.csv")
        birthdays = {(row["month"], row["day"]): row for (_, row) in data.iterrows()}

        if today in birthdays:
            birthday_person = birthdays[today]

            # Pick a random letter and replace the [NAME] with the person's actual name from birthdays.csv
            file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            try:
                with open(file_path) as letter_file:
                    contents = letter_file.read().replace("[NAME]", birthday_person["name"])
            except FileNotFoundError:
                logging.error(f"Letter template {file_path} not found.")
                return  
            
            try:
                # Send the letter to that person's email address
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL, 
                        to_addrs=birthday_person["email"], 
                        msg=f"Subject:Happy Birthday!\n\n{contents}"
                        )
                    logging.info(f"Email sent successfully to {birthday_person['email']}")
            except smtplib.SMTPException as e:
                logging.error(f"Failed to send email: {e}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main() # Start the game


