from django.db import models

class Customer(models.Model):
    f_name = models.CharField('Vardas', max_length=200)
    l_name = models.CharField('Pavardė', max_length=200)
    email = models.CharField('El. paštas', max_length=200)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

    class Meta:
        verbose_name = 'Vartotojas'
        verbose_name_plural = 'Vartotojai'

class Order(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    date = models.DateField('Užsakymo data', null=True, blank=True)
    status_id = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.customer_id} {self.date} {self.status_id}'

    class Meta:
        ordering = ['date']
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

class Status(models.Model):
    name = models.CharField('Užsakymo būsena', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Užsakymo būsena'
        verbose_name_plural = 'Užsakymų būsenos'

class ProductOrder(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.CharField('Kiekis', max_length=200)

    def __str__(self):
        return f'{self.order_id} {self.product_id} {self.quantity}'

    class Meta:
        verbose_name = 'Prekių užsakymas'
        verbose_name_plural = 'Prekių užsakymai'

class Product(models.Model):
    name = models.CharField('Prekės pavadinimas', max_length=200)
    price = models.CharField('Kaina', max_length=200)

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Produktas'
        verbose_name_plural = 'Produktai'