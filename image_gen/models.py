from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_year_format(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError(
            _('Year must be a valid integer.'),
            params={'value': value},
        )


class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    established_date = models.CharField(max_length=4, validators=[validate_year_format], blank=True, null=True, help_text='Enter the year in YYYY format')
    size = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.established_date:
            try:
                int(self.established_date)
            except ValueError:
                raise ValidationError(_('Invalid year format. Please enter a valid year in YYYY format.'))
        super().save(*args, **kwargs)

    def established_year(self):
        return self.established_date

    def clean(self):
        super().clean()
        if self.established_date and len(self.established_date) != 4:
            raise ValidationError(_('Year must be in YYYY format.'))


class JobListing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=100, help_text='2-3 Years', null=True, blank=True)
    Employement_type  = models.CharField(max_length=50, choices=[
        ('Full-Time', 'Full-Time'), 
        ('On-site Full-Time', 'On-site Full-Time'), 
        ('Remote Full-Time', 'Remote Full-Time'), 
        ('On-site Part-Time', 'On-site Part-Time'), 
        ('Remote Part-Time', 'Remote Part-Time'), 
        ('Hybrid Full-Time', 'Hybrid Full-Time'), 
        ('Part-Time', 'Part-Time'), 
        ('Remote', 'Remote'), 
        ('Internship', 'Internship')
    ])
    Seniority_level = models.CharField(max_length=50, choices=[
        ('Junior', 'Junior'), 
        ('Mid-Level', 'Mid-Level'), 
        ('Senior', 'Senior'), 
        ('Team Lead', 'Team Lead'),
        ('Project Manager', 'Project Manager')
    ], blank=True, null=True,)
    salary = models.CharField(max_length=100, default='Negotiable/Not Disclosed')
    deadline = models.DateTimeField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    application_link = models.URLField(blank=True, null=True)
    application_email = models.EmailField(blank=True, null=True)
    no_of_vaccancy = models.CharField(max_length=5,blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)

    vac_img = models.ImageField(upload_to='vaccancy', null=True, blank=True)
    # qualifications = models.ManyToManyField('Qualifications', related_name='qualifications')
    # responsbilities = models.ManyToManyField('Responsbilities', related_name='responsbilities')
    # skills = models.ManyToManyField('Skill', related_name='skills')

    # jobmetrics
    Job_views = models.PositiveIntegerField(default=0)
    application_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.position} at {self.company.name}"
    
    def generate_hashtags(self):
        hashtags = set()
        if self.position:
            hashtags.add(f'{self.position.lower().replace(" ", "")}')

        default_hashtags = Hashtag.objects.filter(is_default=True)
        for hashtag in default_hashtags:
            hashtags.add(hashtag.name)

        obj_hashtags = list()
        for hashtag in hashtags:
            hashtag_obj, _ =Hashtag.objects.get_or_create(name=hashtag)
            obj_hashtags.append(hashtag_obj.name)

        return obj_hashtags
    
    class Meta:
        ordering = ['-id']


class AdditionalInfo(models.Model):
    content = models.TextField()
    title = models.ForeignKey('JobInfoTitle', on_delete=models.RESTRICT, blank=True, null=True)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='add_info')

    def __str__(self):
        return self.title.title
      
    
class JobInfoTitle(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    

class Qualifications(models.Model):
    content = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.content[:100]}...'
    
class Responsbilities(models.Model):
    content = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.content[:100]}...'
    
class AboutJob(models.Model):
    job = models.ForeignKey(JobListing, blank=True, null=True, related_name='about_job', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.content[:100]}...'
    
class Skill(models.Model):
    TYPES = [
        ('Technical', 'Technical'),
        ('soft', 'Technical'),
    ]
    skills_type = models.CharField(max_length=50, choices=TYPES, null=True, blank=True, default='Technical')
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content[:100]}'


class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

    