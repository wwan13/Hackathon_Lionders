from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Community(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Community.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Community, self).save(*args, **kwargs)