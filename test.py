from weasyprint import HTML

html_content = """
<html>
<head><title>Test PDF</title></head>
<body><h1>Hello, World!</h1></body>
</html>
"""

HTML(string=html_content).write_pdf('output.pdf')