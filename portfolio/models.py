from django.db import models

CATEGORIES = (
    ('Website', 'Website'),
    ('Web App', 'Web App'),
)

class Portfolio(models.Model):
    created_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    categories = models.CharField(max_length=50, choices=CATEGORIES, default='Website')
    img = models.ImageField(upload_to='static/assets/img/portfolio/')

    def __str__(self):
        return f"{self.name}"

