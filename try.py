import json

def get_candidate_info(candidate_num):
    name = input(f"Enter name of candidate {candidate_num}: ")
    strengths = input("Enter candidate's strengths (comma-separated): ").split(",")
    qualification_percentage = input(f"Enter qualification percentage for candidate {candidate_num}: ")
    return {
        "name": name,
        "strengths": strengths,
        "qualification_percentage": qualification_percentage
    }

def main():
    job_title = input("Enter job title: ")
    job_qualifications = input("Enter job qualifications (comma-separated): ").split(",")
    candidate1 = get_candidate_info(1)
    candidate2 = get_candidate_info(2)
    comparison = input("Enter comparison details: ")

    job_data = {
        "job_title": job_title,
        "job_qualifications": job_qualifications,
        "candidates": [candidate1, candidate2],
        "comparison": comparison
    }

    json_format = json.dumps(job_data, indent=2)
    print(json_format)

if __name__ == "__main__":
    main()
