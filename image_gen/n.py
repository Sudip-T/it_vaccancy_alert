def format_post():
    post = f"""
Cloco Nepal is #hiring Flutter Developer
    
🚀 Position: flutter developer
Employment Type: full-time
Location: 'kathmandu'
Experience: 'job.experience'
    
🔑 Roles Available:
"""
    roles = [
        "Develop mobile applications using Flutter",
        "Collaborate with cross-functional teams to define, design, and ship new features",
        "Unit-test code for robustness, including edge cases, usability, and general reliability",
        "Work on bug fixing and improving application performance",
        "Continuously discover, evaluate, and implement new technologies to maximize development efficiency"
    ]
    
    for idx, role in enumerate(roles, start=1):
        post += f"- {role}\n"

    # Optionally add more content here, if needed

    # post += f"""
    # 💼 Key Responsibilities:

    
    # 🔗 Apply Now!
    # {job.application_link if job.application_link else 'https://www.linkedin.com/jobs/search/'}
    # """
    return post

print(format_post())

