# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from pathlib import Path
# from datetime import datetime
# import time

# # ==== Configuration ====
# SAVE_DIR = Path("gmail_archive")
# NUM_EMAILS_TO_CAPTURE = 20
# WAIT_BETWEEN_ACTIONS = 2

# # Path to your local Chrome profile (adjust this if needed)
# CHROME_PROFILE_PATH = "/Users/YOUR_USERNAME/Library/Application Support/Google/Chrome"
# PROFILE_NAME = "Default"  # or "Profile 1", "Profile 2", etc.

# # ==== Setup ====
# SAVE_DIR.mkdir(exist_ok=True)
# chrome_options = Options()
# chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
# chrome_options.add_argument(f"--profile-directory={PROFILE_NAME}")
# chrome_options.add_argument("--start-maximized")

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://mail.google.com")

# input("👉 Make sure Gmail is open and visible, then press ENTER to begin...")

# def sanitize_filename(text):
#     return "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in text).strip().replace(" ", "_")

# def get_email_metadata():
#     try:
#         from_email = driver.find_element(By.CSS_SELECTOR, "span.gD").get_attribute("email")
#         to_email = driver.find_element(By.CSS_SELECTOR, "span.g2").get_attribute("email")
#         subject = driver.find_element(By.CSS_SELECTOR, "h2.hP").text.strip()
#         date_str = driver.find_element(By.CSS_SELECTOR, "span.g3, span.gH .gK").get_attribute("title")
#     except Exception as e:
#         print("⚠️ Error extracting metadata:", e)
#         from_email = to_email = subject = date_str = "unknown"
#     return from_email, to_email, subject, date_str

# def screenshot_email(index):
#     try:
#         email_rows = driver.find_elements(By.CSS_SELECTOR, "tr.zA")
#         if index >= len(email_rows):
#             print("✅ Reached end of available emails.")
#             return False

#         email_rows[index].click()
#         time.sleep(WAIT_BETWEEN_ACTIONS)

#         from_email, to_email, subject, date_str = get_email_metadata()

#         try:
#             dt = datetime.strptime(date_str, "%b %d, %Y, %I:%M %p")
#         except:
#             dt = datetime.now()

#         filename = f"{sanitize_filename(from_email)}_{sanitize_filename(to_email)}_{dt.strftime('%Y%m%d_%H%M')}_{sanitize_filename(subject[:30])}.png"
#         screenshot_path = SAVE_DIR / filename

#         driver.save_screenshot(str(screenshot_path))
#         print(f"📸 Saved: {screenshot_path}")

#         driver.back()
#         time.sleep(WAIT_BETWEEN_ACTIONS)
#         return True
#     except Exception as e:
#         print(f"❌ Error processing email {index}: {e}")
#         return False

# print(f"\n📩 Beginning capture of {NUM_EMAILS_TO_CAPTURE} emails...\n")
# for i in range(NUM_EMAILS_TO_CAPTURE):
#     if not screenshot_email(i):
#         break

# driver.quit()
# print(f"\n✅ Done! Screenshots saved in: {SAVE_DIR.resolve()}")
# import os
# from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# # === Paths ===
# chrome_profile_path = "/Users/justinlandess/Library/Application Support/Google/Chrome for Testing"
# profile_name = "Default"
# screenshot_folder = "gmail_screenshots"

# # === Create output folder if it doesn't exist ===
# os.makedirs(screenshot_folder, exist_ok=True)

# # === Configure Chrome Options ===
# options = Options()
# options.add_argument(f"--user-data-dir={chrome_profile_path}")
# options.add_argument(f"--profile-directory={profile_name}")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")  # Optional: stops annoying popups

# # === Start Chrome Driver ===
# driver = webdriver.Chrome(options=options)

# # === Navigate to Gmail ===
# driver.get("https://mail.google.com")

# # === Wait for Gmail to fully load ===
# print("Waiting for Gmail to load...")
# time.sleep(10)  # Adjust this if Gmail is slow to load

# # === Screenshot ===
# now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# filename = f"gmail_{now}.png"
# filepath = os.path.join(screenshot_folder, filename)

# driver.save_screenshot(filepath)
# print(f"✅ Screenshot saved to: {filepath}")

# === Optional: Keep the browser open or close it ===
# driver.quit()


# import os
# import fitz  # PyMuPDF
# import re
# from datetime import datetime
# import shutil

# pdf_folder = os.path.expanduser("~/Desktop/gmail_pdf")
# output_folder = os.path.expanduser("~/Desktop/organized_emails")
# os.makedirs(output_folder, exist_ok=True)

# # === Regex Patterns ===
# date_pattern = re.compile(r"Date:\s*(\d{1,2} [A-Za-z]{3,9} \d{4})")
# from_pattern = re.compile(r"From:\s*(.+?)\s*<(.+?)>")
# to_pattern = re.compile(r"To:\s*(.+?)\s*<(.+?)>")

# def extract_email_metadata(pdf_path):
#     with fitz.open(pdf_path) as doc:
#         text = ""
#         for page in doc:
#             text += page.get_text()
#         # Extract date
#         date_match = date_pattern.search(text)
#         date_obj = None
#         if date_match:
#             try:
#                 date_obj = datetime.strptime(date_match.group(1), "%d %B %Y")
#             except ValueError:
#                 try:
#                     date_obj = datetime.strptime(date_match.group(1), "%d %b %Y")
#                 except ValueError:
#                     pass
#         # Extract sender and recipient
#         from_match = from_pattern.search(text)
#         to_match = to_pattern.search(text)

#         sender = from_match.group(1).strip() if from_match else "UnknownSender"
#         recipient = to_match.group(1).strip() if to_match else "UnknownRecipient"

#         return date_obj, sender.replace(" ", "_"), recipient.replace(" ", "_")

# for filename in os.listdir(pdf_folder):
#     if filename.lower().endswith(".pdf"):
#         full_path = os.path.join(pdf_folder, filename)
#         date_obj, sender, recipient = extract_email_metadata(full_path)
        
#         if date_obj:
#             date_str = date_obj.strftime("%Y-%m-%d")
#             new_filename = f"{date_str}_{sender}_to_{recipient}.pdf"
#         else:
#             new_filename = f"UnknownDate_{sender}_to_{recipient}.pdf"
        
#         new_path = os.path.join(output_folder, new_filename)
#         shutil.copy(full_path, new_path)
#         print(f"✅ Saved: {new_filename}")


# import os
# import fitz  # PyMuPDF
# import re

# pdf_folder = "/Users/justinlandess/Desktop/gmail_pdf"
# output_folder = "/Users/justinlandess/Desktop/organized_emails"
# os.makedirs(output_folder, exist_ok=True)

# # Patterns to search for
# date_pattern = re.compile(r"Date:\s*(.*)")
# from_pattern = re.compile(r"From:\s*(.*)")
# to_pattern = re.compile(r"To:\s*(.*)")

# # Enumerate files
# for i, filename in enumerate(os.listdir(pdf_folder), 1):
#     if filename.endswith(".pdf"):
#         filepath = os.path.join(pdf_folder, filename)
#         doc = fitz.open(filepath)
#         text = ""
#         for page in doc:
#             text += page.get_text()
        
#         # Try to extract metadata
#         date_match = date_pattern.search(text)
#         from_match = from_pattern.search(text)
#         to_match = to_pattern.search(text)

#         # Clean values
#         email_date = date_match.group(1).split()[0] if date_match else "UnknownDate"
#         email_date = email_date.replace(",", "").strip()
#         sender = from_match.group(1).split("<")[0].strip() if from_match else "UnknownSender"
#         recipient = to_match.group(1).split("<")[0].strip() if to_match else "UnknownRecipient"

#         # Normalize date
#         try:
#             from datetime import datetime
#             parsed_date = datetime.strptime(email_date, "%b %d %Y")  # "Mar 11 2025"
#             email_date = parsed_date.strftime("%Y-%m-%d")
#         except:
#             pass

#         # Create new filename
#         new_filename = f"{email_date}_{sender}_to_{recipient}.pdf"
#         new_filepath = os.path.join(output_folder, new_filename)

#         # Save a copy
#         doc.save(new_filepath)
#         doc.close()

#         print(f"✅ [{i}] Saved: {new_filename}")
import os
import fitz  # PyMuPDF
import re
from datetime import datetime

pdf_folder = "/Users/justinlandess/Desktop/gmail_pdf"
output_folder = "/Users/justinlandess/Desktop/organized_emails"
os.makedirs(output_folder, exist_ok=True)

# Patterns to search for
date_pattern = re.compile(r"Date:\s*(.*)")
from_pattern = re.compile(r"From:\s*(.*)")
to_pattern = re.compile(r"To:\s*(.*)")

# Month mapping (for converting full month names)
month_map = {
    "January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
    "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"
}

# Enumerate files
for i, filename in enumerate(os.listdir(pdf_folder), 1):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_folder, filename)
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Try to extract metadata
        date_match = date_pattern.search(text)
        from_match = from_pattern.search(text)
        to_match = to_pattern.search(text)

        # Clean values
        email_date = date_match.group(1) if date_match else "UnknownDate"
        sender = from_match.group(1).split("<")[0].strip() if from_match else "UnknownSender"
        recipient = to_match.group(1).split("<")[0].strip() if to_match else "UnknownRecipient"

        # Parse full date and time
        try:
            if email_date != "UnknownDate":
                # Format: "February 13, 2025 at 12:08 AM"
                date_time_parts = email_date.split(" at ")
                date_part = date_time_parts[0]
                time_part = date_time_parts[1] if len(date_time_parts) > 1 else "00:00 AM"
                
                # Parse date
                month_name, day, year = date_part.split(" ")
                day = day.replace(",", "").zfill(2)
                month = month_map.get(month_name, "UnknownMonth")
                
                # Parse time
                time_obj = datetime.strptime(time_part, "%I:%M %p")  # "12:08 AM" format
                time_str = time_obj.strftime("%H-%M-%S")  # Convert to "HH-MM-SS"

                email_date = f"{year}-{month}-{day}_{time_str}"
        except Exception as e:
            email_date = "UnknownDate"
            print(f"Error parsing date for {filename}: {e}")

        # Create new filename
        new_filename = f"{email_date}_{sender}_to_{recipient}.pdf"
        new_filepath = os.path.join(output_folder, new_filename)

        # Save a copy
        doc.save(new_filepath)
        doc.close()

        print(f"✅ [{i}] Saved: {new_filename}")
