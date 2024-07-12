import os
import sys
import django


sys.path.append(r'C:\Users\user\Desktop\recent_work\it_vaccancy_alert')
os.environ['DJANGO_SETTINGS_MODULE'] = 'it_vaccancy.settings'
django.setup()


from image_gen.models import JobListing, Company,AdditionalInfo



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
            if not self.job_data:
                print ("job_data has not been loaded. Call load_job_listing() first.")
            
            job_scipt = '\n'
            job_scipt += f'{job.company.name.capitalize()} is #hiring {job.position}\n\n'
            if job.Employement_type:
                job_scipt += f'Job Type : {job.Employement_type}\n'
            if job.Employement_type:
                job_scipt += f'Location : {job.company.address}\n'
            if job.Employement_type:
                job_scipt += f'Exprience : {job.experience}\n'
            if job.Employement_type:
                job_scipt += f'Exprience : {job.experience}\n'

            print(job_scipt)
        except Exception as e:
            print(e)

        



    def generate_job_script(self):
        try:
            self.create_script_content()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    job_listing_id = 2
    generator = JobScript(job_listing_id)
    generator.generate_job_script()