from docx import Document

document = Document("Info.docx")
paragraph = document.paragraphs[0]
print(paragraph.text)