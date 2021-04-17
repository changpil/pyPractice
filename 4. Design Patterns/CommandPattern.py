class Document:
    text = ""
    def __str__(self):
        return self.text

import abc
class DocumentCommand(abc.ABC):
    doc = None
    @abc.abstractmethod
    def execute(self):
        pass
    @abc.abstractmethod
    def undo(self):
        pass

class AddStrCommand(DocumentCommand):
    def __init__(self, doc, txt):
        self.text = txt
        self.doc = doc
    def execute(self):
        self.doc.text += self.text
    def undo(self):
        return DeleteStrCommand(self.doc, self.text)

class DeleteStrCommand(DocumentCommand):
    def __init__(self, doc, txt):
        self.text = txt
        self.doc = doc
    def execute(self):
        idx = self.doc.text.find(self.text)
        self.doc.text = self.doc.text[:idx]
    def undo(self):
        return AddStrCommand(self.doc, self.text)

doc = Document()
addingTexts = [AddStrCommand(doc,"hello\n"), AddStrCommand(doc,"My name is Chang\n"),  AddStrCommand(doc,"I hope you have a good day")]
for c in addingTexts:
    c.execute()
print("#"*5)
print(doc)
print("#"*5)
addingTexts[-1].undo().execute()
print(doc)
print("#"*5)

d = DeleteStrCommand(doc,"My name is Chang\n")
d.execute()
print(doc)
print("#"*5)
d.undo().execute()
print(doc)
print("#"*5)