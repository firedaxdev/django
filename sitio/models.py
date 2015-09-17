from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField
from django.db.models import permalink
from redactor.fields import RedactorField

# Create your models here.
class Categoria(models.Model):
	titulo = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(editable=False, db_index=True)

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Categoria, self).save(*args, **kwargs)

	@permalink
	def get_absolute_url(self):
		return "categoria/%i" % self.slug

class Entrada(models.Model):
	titulo = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(editable=False, unique=True)
	contenido = RedactorField(verbose_name=u'Contenido',
    redactor_options={'lang': 'es', 'focus': 'true'},
    upload_to='/media/',
    allow_file_upload=True,
    allow_image_upload=True)
	categoria = models.ForeignKey(Categoria)
	publicado = models.DateField(db_index=True, auto_now_add=True)
	def __str__(self):
		return self.titulo


	@permalink
	def get_absolute_url(self):
		return "entrada/$i" % self.slug

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*args, **kwargs)
