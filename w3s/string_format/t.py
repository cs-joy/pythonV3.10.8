from docx import Document

document = Document("D:\id\Important Info.docx")
paragraph = document.paragraphs[0]
print(paragraph.text)