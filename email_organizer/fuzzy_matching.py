import os
import fitz  # PyMuPDF
import re
from datetime import datetime
from difflib import SequenceMatcher

# === Folders ===
pdf_folder = input("enter source folder: \nExample:\n\/Users/justinlandess/Desktop/gmail_pdf\nenter source folder: ")
output_folder = input("Example: /Users/justinlandess/Desktop/organized_emails\nEnter output folder: ")

# === Create output folder if it doesn't exist ===
os.makedirs(output_folder, exist_ok=True)

# === Keyword list ===
keywords = keywords = [
    "Jonathan","$","bonus","share","share's",
    "contribution", "stock", "payment",
    "differred", "obligation", "vlad",
    "promise","action","secret","confidential",
    "performance","termination","vest","purchase",
    "wrongful"
    ]

# === Regex patterns ===
date_pattern = re.compile(r"Date:\s*(.*)")
from_pattern = re.compile(r"From:\s*(.*)")
to_pattern = re.compile(r"To:\s*(.*)")

# === Month mapping ===
month_map = {
    "January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
    "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"
}

# === Fuzzy match helper ===
def fuzzy_contains(text, keyword, threshold=0.85):
    words = text.split()
    for word in words:
        ratio = SequenceMatcher(None, word.lower(), keyword.lower()).ratio()
        if ratio >= threshold:
            return True
    return False

# === Enumerate files ===
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

        email_date = date_match.group(1) if date_match else "UnknownDate"
        sender = from_match.group(1).split("<")[0].strip() if from_match else "UnknownSender"
        recipient = to_match.group(1).split("<")[0].strip() if to_match else "UnknownRecipient"

        # Parse full date and time
        try:
            if email_date != "UnknownDate":
                date_time_parts = email_date.split(" at ")
                date_part = date_time_parts[0]
                time_part = date_time_parts[1] if len(date_time_parts) > 1 else "00:00 AM"

                month_name, day, year = date_part.split(" ")
                day = day.replace(",", "").zfill(2)
                month = month_map.get(month_name, "UnknownMonth")

                time_obj = datetime.strptime(time_part, "%I:%M %p")
                time_str = time_obj.strftime("%H-%M-%S")

                email_date = f"{year}-{month}-{day}_{time_str}"
        except Exception as e:
            email_date = "UnknownDate"
            print(f"Error parsing date for {filename}: {e}")

        # Check for fuzzy keyword matches
        matches = [kw for kw in keywords if fuzzy_contains(text, kw)]

        # Sanitize sender name for folder use
        safe_sender = sender.replace(" ", "_").replace("/", "-")
        sender_folder = os.path.join(output_folder, safe_sender)
        os.makedirs(sender_folder, exist_ok=True)

        # Create new filename
        new_filename = f"{email_date}_{sender}_to_{recipient}.pdf"
        new_filepath = os.path.join(sender_folder, new_filename)

        # Save to sender folder
        doc.save(new_filepath)

        if matches:
            for kw in matches:
                keyword_folder = os.path.join(sender_folder, kw.lower().replace(" ", "_"))
                os.makedirs(keyword_folder, exist_ok=True)
                matched_filepath = os.path.join(keyword_folder, new_filename)
                doc.save(matched_filepath)
            print(f"✅ [{i}] Saved + keyword match ({', '.join(matches)}) → {new_filename}")
        else:
            print(f"✅ [{i}] Saved: {new_filename}")

        doc.close()
