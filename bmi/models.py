from django.db import models


class People(models.Model):
    ssn = models.CharField(max_length=10, verbose_name='身分證字號')
    pname = models.CharField(max_length=30, verbose_name='姓名')
    h = models.IntegerField(verbose_name='身高 (公分)')
    w = models.IntegerField(verbose_name='體重 (公斤)')
    photo = models.ImageField(upload_to="people/", null=True, blank=True)

    def __str__(self):
        return self.pname

    class Meta:
        ordering = ['h']        


class Level(models.Model):
    title = models.CharField(max_length=10)
    low_bound = models.DecimalField(max_digits=5, decimal_places=2)
    up_bound = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{}, {}-{}".format(self.title, self.low_bound, self.up_bound)

    class Meta:
        verbose_name = "BMI 健康指標"
