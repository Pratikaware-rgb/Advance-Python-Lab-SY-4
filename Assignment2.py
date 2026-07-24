def add_border(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
    return wrapper
class Report:
    report_count = 0
    def __init__(self, title, content):
        self.title = title
        self.content = content
        Report.report_count += 1
    @classmethod
    def create_template(cls):
        title = input("Enter Report Title: ")
        content = input("Enter Report Content: ")
        return cls(title, content)
    def __str__(self):
        return f"Report Title : {self.title}\nReport Content : {self.content}"
    def __len__(self):
        return len(self.content)

class ReportFormatter:

    @staticmethod
    def uppercase(text):
        return text.upper()

    @staticmethod
    def lowercase(text):
        return text.lower()

    @staticmethod
    def titlecase(text):
        return text.title()

@add_border
def display_report(report, style):
    print("DYNAMIC REPORT")
    print("Title :", report.title)
    print("Content :", style(report.content))
    print("Characters :", len(report))

print("------ Dynamic Report Generator ------")

report = Report.create_template()

print("\nChoose Formatting Style")
print("1. Uppercase")
print("2. Lowercase")
print("3. Title Case")

choice = input("Enter your choice: ")

if choice == "1":
    format_style = ReportFormatter.uppercase
elif choice == "2":
    format_style = ReportFormatter.lowercase
elif choice == "3":
    format_style = ReportFormatter.titlecase
else:
    print("Invalid choice! Default format applied.")
    format_style = lambda x: x

display_report(report, format_style)

print("\nTotal Reports Created:", Report.report_count)
