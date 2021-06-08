from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=5)


class ServicesForWomen(models.Model):
    # class Meta():
    #     verbose_name_plural = "Услуги для женщин"
    title = models.CharField(max_length=128, verbose_name="Название услуги")
    price = models.CharField(max_length=100, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} {self.price} руб."

class ServicesForMen(models.Model):
    # class Meta():
    #     verbose_name_plural = "Услуги для мужчин"
    title = models.CharField(max_length=128, verbose_name="Название услуги")
    price = models.CharField(max_length=100, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} {self.price} руб."

class ServicesForChildren(models.Model):
    # class Meta():
    #     verbose_name_plural = "Услуги для детей "
    title = models.CharField(max_length=128, verbose_name="Название услуги")
    price = models.CharField(max_length=100, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} {self.price} руб."


class ManicurePedicure(models.Model):
    # class Meta():
    #     verbose_name_plural = "Маникюр-Педикюр"
    title = models.CharField(max_length=128, verbose_name="Название услуги")
    price = models.CharField(max_length=100, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} {self.price} руб."


class CosmetologyServices(models.Model):
    # class Meta():
    #     verbose_name_plural = "Косметологические услуги"
    title = models.CharField(max_length=128, verbose_name="Название услуги")
    price = models.CharField(max_length=100, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} {self.price} руб."


class GiftCertificates(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название услуги")
    price = models.CharField(max_length=100, verbose_name="Цена")

    def __str__(self):
        return f"{self.title} {self.price} руб."

class Reviews(models.Model):
    name = models.CharField('Имя', max_length=50)
    review_text = models.TextField('Текст отзыва')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name, self.review_text, self.date

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

