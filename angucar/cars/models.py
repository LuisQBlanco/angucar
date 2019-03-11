from django.db import models

class EqipBase(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car/%y/%m/')
    price = models.PositiveIntegerField()

    class Meta:
        abstract = True
    


class Engine(EqipBase):
    pass


class Wheels(EqipBase):
    pass


class Interior(EqipBase):
    pass


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.PositiveIntegerField()
    engines = models.ManyToManyField(Engine)
    wheels = models.ManyToManyField(Wheels)
    interiors = models.ManyToManyField(Interior)