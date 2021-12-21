from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.urls import reverse
from pytils.translit import slugify
from django.utils.safestring import mark_safe
from django.utils.timezone import now


# from django.utils.text import slugify


class Author(models.Model):
	"""
	Модель для авторов статей
	"""

	name = models.CharField("Имя автора", max_length=100)
	b_date = models.DateField("Дата рождения автора", null=True)
	slug = models.SlugField("Slug", max_length=255, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Author, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'
		ordering = ['b_date', 'name']

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'slug': self.slug})

	def __str__(self):
		return self.name


class Tag(models.Model):
	"""
	Теги статьи
	"""
	tag_name = models.CharField("Тег", max_length=100)

	def __str__(self):
		return self.tag_name


class Article(models.Model):
	"""
	Статьи авторов
	"""
	title = models.CharField("SEO заголовок", max_length=80)
	description = models.CharField("Описание", max_length=140)
	h1_title = models.CharField("Заголовок", max_length=200)
	content = RichTextField("Контент")
	author = models.ForeignKey(
		Author,
		verbose_name="Автор",
		on_delete=models.CASCADE
	)
	published_date = models.DateField("Дата публикации", default=now)
	is_active = models.BooleanField("Вкл/Выкл", default=False)
	views_amount = models.PositiveIntegerField("Количество просмотров", default=0)
	preview = models.ImageField("Превью", upload_to="images/news&blogs/", null=True)
	tags = models.ManyToManyField(
		Tag,
		verbose_name="Теги",
		related_name='tag'
	)
	slug = models.SlugField("Slug", max_length=255, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)

	def admin_image(self):

		if self.preview:
			return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>'.format(self.preview.url))
		else:
			return 'Image Not Found'

	admin_image.short_description = 'preview'
	admin_image.allow_tags = True

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"

		ordering = ["-published_date"]

	def get_absolute_url(self):
		return reverse('blog', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title


class Profile(models.Model):
	"""
	Модельпрофиля пользователя
	"""
	user = models.OneToOneField(
		User,
		verbose_name="User profile",
		on_delete=models.CASCADE
	)
	is_author = models.BooleanField("Is author?", default=False)
	avatar = models.ImageField(
		"Avatar",
		upload_to='avatars/',
		default="avatars/default_user.jpg",
		blank=True
	)
	# bio = RichTextField("Description")
	slug = models.SlugField("Slug url", max_length=255, blank=True)

	def __str__(self):
		return f'{self.user.get_full_name()}'

	class Meta:
		verbose_name = "Профиль"
		verbose_name_plural = "Профили"
		ordering = ['user']

	def get_absolute_url(self):
		return reverse('profile-detail', kwargs={'slug': self.slug})

	def admin_image(self):

		if self.avatar:
			return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="50" /></a>'.format(self.avatar.url))
		else:
			return 'Image Not Found'

	admin_image.short_description = 'Avatar'
	admin_image.allow_tags = True

	def get_user_name(self):
		return self.user.get_full_name()

	get_user_name.short_description = 'Имя Фамилия'

	def get_staff_status(self):
		if self.user.is_staff:
			img = mark_safe('<img src="/static/admin/img/icon-yes.svg" />')
		else:
			img = mark_safe('<img src="/static/admin/img/icon-no.svg" />')
		return img

	get_staff_status.short_description = 'Персонал'
	get_staff_status.allow_tags = True

	def get_active_status(self):
		if self.user.is_active:
			img = mark_safe('<img src="/static/admin/img/icon-yes.svg" />')
		else:
			img = mark_safe('<img src="/static/admin/img/icon-no.svg" />')
		return img

	get_active_status.short_description = 'Профиль активный?'
	get_active_status.allow_tags = True

	def save(self, *args, **kwargs):
		self.slug = f'{self.user_id}-{self.user.username}'  # показать slugify
		super(Profile, self).save(*args, **kwargs)


class Comment(models.Model):
	"""
	Модель комментариев
	"""
	user = models.ForeignKey(
		User,
		verbose_name="",
		on_delete=models.CASCADE,
		related_name='user_comment'
	)
	article = models.ForeignKey(Article, verbose_name="", on_delete=models.CASCADE, related_name="comment_article")
	text = models.TextField("")
	published_date = models.DateField("", editable=False, auto_now=True)

	def __str__(self):
		return f'{self.user}-{self.article_id}'

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"
		ordering = ['-published_date']


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()
