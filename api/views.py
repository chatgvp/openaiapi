from django.shortcuts import render
import PyPDF2
import openai
from rest_framework.views import APIView
from rest_framework.response import Response

api_key = "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"
openai.api_key = api_key


def algorithm(job_title, job_qualifications, candidate1, candidate2):
    json_format = """
    {
    "job_title": "",
    "job_qualifications": "qualifications you just enter",
    "candidate1": {
        "name":"",
        "strengths": [],
        "qualification_percentage": ""
    },"candidate2": {
        "name": "",
        "strengths": [],
        "qualification_percentage": ""
    }
    "comparison": ""
    }
    """
    chatgpt_prompt = (
        candidate1
        + " compare to "
        + candidate2
        + " in the Position of: "
        + job_title
        + " Job Qualifications: "
        + job_qualifications
        + "follow this JSON format"
        + json_format
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chatgpt_prompt},
        ],
        temperature=0,
        max_tokens=1000,
    )
    return response["choices"][0]["message"]["content"]


class PdfToJsonView(APIView):
    def post(self, request, *args, **kwargs):
        if "candidate1" in request.FILES and "candidate2" in request.FILES:
            job_title = request.POST.get("job_title")
            job_qualifications = request.POST.get("job_qualifications")

            candidate1 = request.FILES["candidate1"]
            candidate2 = request.FILES["candidate2"]
            pdf_reader1 = PyPDF2.PdfReader(candidate1)
            candidate_text1 = ""
            for page in pdf_reader1.pages:
                candidate_text1 += page.extract_text()
            pdf_reader2 = PyPDF2.PdfReader(candidate2)
            candidate_text2 = ""
            for page in pdf_reader2.pages:
                candidate_text2 += page.extract_text()
            response_data = algorithm(
                job_title, job_qualifications, candidate_text1, candidate_text2
            )
            return Response(response_data, content_type="application/json")
        else:
            return Response(
                {"error": "Both candidate1 and candidate2 PDF files must be uploaded."},
                status=400,
            )


def home(request):
    return render(request, "home.html")
