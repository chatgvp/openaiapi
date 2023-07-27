import json
from django.shortcuts import render
import PyPDF2
import openai
from rest_framework.views import APIView
from rest_framework.response import Response

api_key = "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"
openai.api_key = api_key


def algorithm(job_title, job_qualifications, candidate1):
    json_format = """
                {
                "job_title": "",
                "job_qualifications": "",
                "candidate1": {
                    "name":"",
                    "strengths": [],
                    "weaknesses": [],
                    "qualification_percentage": ""
                },
                "summary": ""
                }
                """

    chatgpt_prompt = (
        "Evaluate the candidate's qualifications for the position of "
        + job_title
        + " based on the provided job qualifications.\n\n"
        + "Candidate:\n"
        + candidate1
        + "\n\n"
        + "Position: "
        + job_title
        + "\n\n"
        + "Job Qualifications:"
        + job_qualifications
        + "\n\n"
        + "If the candidate does not meet the qualifications: provide a detailed explanation of their strengths and weaknesses, and assign a low qualification percentage.\n"
        + "Do not recommend the candidate for the position if they do not meet the minimum qualifications.\n If the candidate does meet the qualifications: Provide a detailed explanation of why they are well-suited for the role and assign a high qualification percentage."
        + "Also provide a summary of the why the candidate got their qualification percentage limited to 280 characters"
        + "Please completely follow and enter all fields using this JSON format:\n"
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
        print(request)
        if "candidate1" in request.FILES:
            num_files_uploaded = len(request.FILES)
            print(num_files_uploaded)
            print(request.FILES)
            job_title = request.POST.get("job_title")
            job_qualifications = request.POST.get("job_qualifications")
            candidate1 = request.FILES["candidate1"]
            pdf_reader1 = PyPDF2.PdfReader(candidate1)
            print(pdf_reader1)
            # print(len(candidate1))
            candidate_text1 = ""
            for page in pdf_reader1.pages:
                candidate_text1 += page.extract_text()
            response_data = algorithm(job_title, job_qualifications, candidate_text1)
            # cleaned_string = response_data.replace("\n", "")
            json_object = json.loads(response_data)
            return Response(json_object, content_type="application/json")

        else:
            return Response(
                {"error": "Both candidate1 and candidate2 PDF files must be uploaded."},
                status=400,
            )


def home(request):
    return render(request, "home.html")
