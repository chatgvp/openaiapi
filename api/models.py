from django.db import models


class ProcessedPDF(models.Model):
    pdf_file = models.FileField(upload_to="pdf_files/")
    json_file = models.FileField(upload_to="json_files/")
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Processed PDF: {self.pdf_file.name}"
