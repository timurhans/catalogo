from django.db import models

# Create your models here.

class Page(models.Model):
    ordem = models.IntegerField(null=False, blank=False,unique=True)
    img = models.FileField(upload_to = 'static/pages/', null=False, blank=False)
    def __str__(self):
        return str('pg'+str(self.ordem))
        
class Like(models.Model):
    cnpj      = models.CharField(max_length=10, null=False, blank=False)
    ip      = models.CharField(max_length=10, null=False, blank=False)
    page        = models.ForeignKey(Page, null=False, blank=False, on_delete=models.CASCADE)
    liked      = models.BooleanField(default=False)
    def __str__(self):
        return str(self.cnpj+'-'+self.ip)

