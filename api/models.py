from django.db import models


DEPTS = (('Echo', 'Echo'), ('Xray', 'Xray'))

CATEGORY_CHOICES = (
    ('Echo-General', 'Echo-General'),
    ('Echo Special', 'Echo-Special'),
    ('Xray-General', 'Xray-General'),
    ('Xray-Special', 'Xray-Special'))


class RadiDept(models.Model):
    name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.name.upper())


class RadiTestCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True, choices=CATEGORY_CHOICES)
    department = models.ForeignKey(RadiDept, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.category_name.upper())

    def save(self, *args, **kwargs):
        self.category_name = (str(self.category_name)).upper()
        super(RadiTestCategory, self).save(*args, **kwargs)


class RadiTestType(models.Model):
    type_name = models.CharField(max_length=15, unique=True, default='')
    cost = models.IntegerField(default='')
    category = models.ForeignKey(RadiTestCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type_name)

    def save(self, *args, **kwargs):
        self.type_name = (str(self.type_name)).upper()
        super(RadiTestType, self).save(*args, **kwargs)
