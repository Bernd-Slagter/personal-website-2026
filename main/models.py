from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('tools', 'Tools & Platforms'),
        ('soft', 'Soft Skills'),
        ('language', 'Languages'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='technical')
    proficiency = models.IntegerField(default=80, help_text='0-100 percentage')
    icon = models.CharField(max_length=100, blank=True, help_text='FontAwesome class e.g. fa-python')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    technologies = models.CharField(max_length=500, help_text='Comma-separated list')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    featured = models.BooleanField(default=False)
    created_date = models.DateField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-featured', 'order', '-created_date']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True, help_text='Leave blank if current')
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f'{self.degree} — {self.institution}'

    def get_period(self):
        end = self.end_year if self.end_year else 'Present'
        return f'{self.start_year} – {end}'


class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.title} at {self.organization}'

    def get_period(self):
        if self.is_current:
            return f'{self.start_date.strftime("%b %Y")} – Present'
        end = self.end_date.strftime('%b %Y') if self.end_date else ''
        return f'{self.start_date.strftime("%b %Y")} – {end}'


class Interest(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, help_text='FontAwesome class')
    description = models.CharField(max_length=300, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'
