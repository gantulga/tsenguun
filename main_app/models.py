from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name='Ангиллын нэр', default="")
    description = models.TextField(null=True, blank=True, verbose_name='Тайлбар')
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name="children", verbose_name='Эцэг ангилал')

    def __str__(self):
        return "{}".format(self.name)
    
    class Meta:
        verbose_name_plural = "Ангилал"

class Article(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Гарчиг', default="")
    content = models.TextField(null=True, blank=True, verbose_name='Мэдээний агуулга')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="articles", verbose_name='Ангилал')

    def __str__(self):
        return "{}".format(self.title)
    
    class Meta:
        verbose_name_plural = "Мэдээ"