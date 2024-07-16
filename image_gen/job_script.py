import os
import sys
import django


sys.path.append(r'C:\Users\user\Desktop\recent_work\it_vaccancy_alert')
os.environ['DJANGO_SETTINGS_MODULE'] = 'it_vaccancy.settings'
django.setup()


from image_gen.models import JobListing, Company,AdditionalInfo, JobInfoTitle

# for obj in AdditionalInfo.objects.all():
    # JobInfoTitle.objects.create(title=obj.header)

class JobScript:
    def __init__(self, job_id):
        self.job_id = job_id
        self.job_data = self.load_job()

    def load_job(self):
        try:
            return JobListing.objects.get(id=self.job_id)
        except JobListing.DoesNotExist:
            raise ValueError(f"JobListing with id {self.job_id} does not exist.")
        
    def create_script_content(self):
        try:
            job = self.job_data
            # dat = self.job_data.add_info.all()
            # for data in dat:
            #     print(data.content)
            if not self.job_data:
                print ("job_data has not been loaded. Call load_job_listing() first.")
            
            job_script = '\n'
            job_script += f'{job.company.name} is #hiring {job.position} 📢\n\n'
            if job.Employement_type:
                job_script += f'\U0001F680 Job Type : {job.Employement_type}\n'
            if job.Employement_type:
                job_script += f'\U0001F4CD Location : {job.company.address}\n'
            if job.experience:
                job_script += f'\U0001F4BB Experience : {job.experience}'
            job_script += '\n\n'
            additional_info = job.add_info.all()
            for info in additional_info:
                if info.title.title == 'Qualifications':
                    job_script += 'Qualifications:\n'
                    job_script += '\n'.join(f'\u2705 {line.strip()}' for line in info.content.split('\n')) + '\n\n'
                elif info.title.title == 'Responsibilities':
                    job_script += 'Responsibilities:\n'
                    # job_script += '\n'.join(f'{line}' for line in info.content.split('\n'))
                    job_script += '\n'.join(f'\u2705 {line.strip()}' for line in info.content.split('\n')) + '\n\n'
            if job.application_email:
                job_script += '\U0001F517 How to Apply\n'
                job_script += f'Interest candidates are encouraged to submit their resume to {job.application_email} or apply through the link in the comment section below\n\n\n'
            else:
                job_script += '\U0001F517 How to Apply\n'
                job_script += 'Apply through the link in the comment section below\n\n'
            
            hashtags = job.generate_hashtags()
            for hashtag in job.generate_hashtags():
                job_script += f'#{hashtag} '
            
            if job.application_link:
                job_script += f'\n\n\n{job.application_link}'
            return job_script
            
        except Exception as e:
            print(e)


    def generate_job_script(self):

        try:
            job_script = self.create_script_content()
            with open('image_gen/new_vaccancy.txt', 'w', encoding='utf-8') as file:
                file.write(job_script)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    job_listing_id = 25
    generator = JobScript(job_listing_id)
    generator.generate_job_script()




import os
import sys
import django

# Adjust the path to your Django project settings
sys.path.append(r'C:\Users\user\Desktop\recent_work\it_vaccancy_alert')
os.environ['DJANGO_SETTINGS_MODULE'] = 'it_vaccancy.settings'

# Initialize Django
django.setup()

# Import necessary modules after Django setup
from rest_framework.test import APIClient
from image_gen.models import JobListing

class JobScript:
    def __init__(self, job_id):
        self.job_id = job_id
        self.job_data = self.load_job()

    def load_job(self):
        client = APIClient()
        response = client.get(f'http://localhost:8000/api/v1/joblistings/{self.job_id}/')  # Adjust the endpoint URL as per your API configuration
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError(f"JobListing with id {self.job_id} does not exist.")
        else:
            raise ValueError(f"Failed to load JobListing with id {self.job_id}. Status code: {response.status_code}")

    def create_script_content(self):
        try:
            job = self.job_data
            if not self.job_data:
                print ("job_data has not been loaded. Call load_job_listing() first.")
            
            job_script = '\n'
            job_script += f'{job["company"]["name"].capitalize()} is #hiring {job["position"]}\n\n'
            if job["Employement_type"]:
                job_script += f'Job Type : {job["Employement_type"]}\n'
            if job["Employement_type"]:
                job_script += f'Location : {job["company"]["address"]}\n'
            if job["experience"]:
                job_script += f'Experience : {job["experience"]}\n\n'
            if job["qualifications"]:
                job_script += f'Qualifications :\n'
                if len(job["qualifications"]) >= 2:
                    for qualification in job["qualifications"]:
                        job_script += f'- {qualification["content"]}\n'
                else:
                    job_script += f'- {job["qualifications"][0]}\n'
                job_script += '\n'
            if job["responsbilities"]:
                job_script += f'Responsbilities :\n'
                if len(job["responsbilities"]) >= 2:
                    for qualification in job["responsbilities"]:
                        job_script += f'- {qualification}\n'
                else:
                    job_script += f'- {job["responsbilities"][0]}\n'
                job_script += '\n'
            
            if job['application_email']:
                job_script += 'How to Apply\n'
                job_script += f'Interest candidates are encouraged to submit their resume to {job['application_email']} or apply through the link in the comment section below\n\n'
            else:
                job_script += 'Apply through the link in the comment section below'

            return job_script
        except Exception as e:
            print(e)

    def generate_job_script(self):
        try:
            job_script = self.create_script_content()
            with open('image_gen/new_vaccancy.txt', 'w') as file:
                file.write(job_script)
            print(job_script)
        except Exception as e:
            print(e)

# if __name__ == "__main__":
#     job_listing_id = 9
#     generator = JobScript(job_listing_id)
#     generator.generate_job_script()

