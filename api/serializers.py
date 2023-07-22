from rest_framework import serializers
from .models import ProcessedPDF


class ProcessedPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedPDF
        fields = "__all__"


class PDFSerializer(serializers.Serializer):
    pdf_file = serializers.CharField()
