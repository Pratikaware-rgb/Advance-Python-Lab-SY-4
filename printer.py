class Printer:

    object = None

    def __new__(cls):

        if cls.object is None:
            cls.object = super().__new__(cls)

        return cls.object

    def print_document(self, name):
        print("Printing:", name)


# Create objects
printer1 = Printer()
printer2 = Printer()

# Print documents
printer1.print_document("Assignment.pdf")
printer2.print_document("Report.docx")

# Verify only one object exists
print(printer1 is printer2)
