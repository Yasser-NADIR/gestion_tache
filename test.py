from weasyprint import HTML
import io
html_content = """
<html>
<head><title>Test PDF</title></head>
<body><h1>Hello, World!</h1></body>
</html>
"""

buffer = io.BytesIO()

HTML(string=html_content).write_pdf(buffer)
buffer.getvalue()