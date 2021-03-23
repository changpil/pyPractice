class Document:
    text = ""
    def __str__(self):
        return self.text

import abc
class DocumentCommand(abc.ABC):
    document = None

    @abc.abstractmethod
    def execute(cls):
        pass

    @abc.abstractmethod
    def undo(cls):
        pass

class AddStrCommand(DocumentCommand):
    text = None
    def __init__(self, doc, txt):
        self.text = txt
        DocumentCommand.document = doc

    def execute(cls):
        DocumentCommand.document.text += cls.text

    def undo(cls):
        idx = DocumentCommand.document.text.find(cls.text)
        DocumentCommand.document.text = DocumentCommand.document.text[:idx]


doc = Document()
addingTexts = [AddStrCommand(doc,"hello\n"), AddStrCommand(doc,"My anme is Chang\n"),  AddStrCommand(doc,"I hope you have a good day")]
for c in addingTexts:
    c.execute()
print(doc)
print()
addingTexts[-1].undo()
print(doc)

