from pypdf import PdfReader


def extract_resume_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":

    resume = extract_resume_text(
        "data/documents/sample.pdf"
    )

    print(resume[:1000])