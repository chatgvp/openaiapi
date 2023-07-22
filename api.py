import os
import openai

json_format = '''
{
  "job_title": "",
  "job_qualifications": [],
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
'''
Job_Title = ""
Job_Qualification = ""
candidate1 = ""
candidate2 = ""
chatgpt_promt = candidate1 +"compare to "+ candidate2+" with "+ "Job Title:" + Job_Title +"Job Qualifications:"+"use this format" + json_format

# Now you can use the variable 'json_data' wherever needed, for example, parsing it using the 'json' module:

import json

parsed_data = json.loads(json_format)
print(parsed_data)  # This will output the parsed JSON data as a Python dictionary


# api_key = "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"
# openai.api_key = api_key

# response = openai.Completion.create(
#     engine="text-davinci-002", 
#     prompt="",
#     temperature=0,
#     max_tokens=1000,
#     stop=None,
# )

# print(response.choices[0].text.strip())