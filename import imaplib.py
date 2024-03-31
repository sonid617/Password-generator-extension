import fitz  # PyMuPDF
import shutil
import os

def identify_bad_words(text, bad_words):
    for word in bad_words:
        if word.lower() in text.lower():
            return True
    return False

def process_pdf(file_path, bad_words, destination_folder):
    # Open the PDF file
    pdf_document = fitz.open(file_path)

    # Iterate through each page of the PDF
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text = page.get_text()

        # Identify bad words in the text
        if identify_bad_words(text, bad_words):
            print(f"Bad words found in {file_path}. Moving to {destination_folder}")
            move_to_folder(file_path, destination_folder)
            break

    # Close the PDF document
    pdf_document.close()

def move_to_folder(file_path, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move the file to the destination folder
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

if __name__ == "__main__":
    # Define the path to the PDF file, bad words list, and destination folder
    pdf_file_path = "C:/Users/ASUS/OneDrive/Desktop/i will kill you dishank.txt"
    bad_words = ["kill", "rape", "badword3"]  # Add your list of bad words
    destination_folder = "C:/Users/ASUS/OneDrive/Desktop/task"

    # Process the PDF file
    process_pdf(pdf_file_path, bad_words, destination_folder)


