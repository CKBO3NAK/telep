
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)
class Article(models.Model):

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('showArticle', kwargs={'pk':self.pk})

class Images(models.Model):
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/img',
                              verbose_name='Image')


