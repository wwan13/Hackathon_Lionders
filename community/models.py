from django.db import models
from users import models as user_models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Community(models.Model):
    user = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()

    def get_user(self):
        return User.objects.get(pk=self.user_id)

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