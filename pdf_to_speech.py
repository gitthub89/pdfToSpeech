import PyPDF2
import pyttsx3

print(PyPDF2.__file__)


def pdf_to_speech(file_path):
    # Open the PDF file
    pdf_file = open(file_path, 'rb')

    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize the text to speech engine
    engine = pyttsx3.init()

    # Read each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Use the speech engine to say the text and run the speech engine
        engine.say(text)
        engine.runAndWait()

    # Close the PDF file
    pdf_file.close()


# Call the function with the path to your PDF file
pdf_to_speech('path to pdf file.pdf')
