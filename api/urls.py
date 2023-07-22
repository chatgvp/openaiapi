from django.urls import path
from . import views

urlpatterns = [
    path("pdf-to-json/", views.PdfToJsonView.as_view(), name="pdf_to_json"),
    # path("llama2/", views.llama2_classification, name="llama2_classification"),
    path("", views.home),
]
