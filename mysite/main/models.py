from django.db import models
from datetime import *

class Clients(models.Model):
    """Клиенты"""
    surname = models.CharField("Фамилия клиента", max_length=15, primary_key=True)
    name = models.CharField("Имя клиента", max_length=15)
    birthdate = models.DateField("Дата рождения клиента")
    phonenumber = models.CharField("Номер телефона клиента", max_length=12)
    gender = models.CharField("Пол клиента", max_length=5)
    document=models.CharField("Тип документа", max_length=15)
    document_series=models.CharField("Серия паспорта", max_length=4)
    document_number=models.CharField("Номер паспорта", max_length=6)

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class RoomsCategory(models.Model):
    """Категория номеров""" 
    room=models.CharField("Номер комнаты", max_length=3,primary_key=True)
    category=models.CharField("Категория номера", max_length=10)
    apartement=models.CharField("Количество комнат", max_length=1)
    price = models.IntegerField("Цена")

    def __str__(self):
        return f' {self.room} {self.price}'
    
    class Meta:
        verbose_name = "Категории Номера"
        verbose_name_plural = "Категории номеров"

class RoomsCondition(models.Model):
    """Состояние Номера"""
    room=models.ForeignKey(RoomsCategory, verbose_name="Номер", on_delete=models.SET_NULL, null=True)
    client=models.ForeignKey(Clients, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    checkin = models.DateField("Дата приезда")
    checkout = models.DateField("Дата отъезда")
    def __str__(self):
        return f'{self.room} {self.client}  '

    class Meta:
        verbose_name = "Состояние Номера"
        verbose_name_plural = "Состояние Номеров"
class Post(models.Model):
    """Должнсоть"""
    post_name=models.CharField("Название должности", max_length=20)
    def __str__(self):
        return f' {self.post_name}'
    
    class Meta:
        verbose_name = "Название должности"
        verbose_name_plural = "Название должностей"
class Employess(models.Model):
    """Сотрудники"""
    salary=models.IntegerField("Зарпалата")
    post=models.ForeignKey(Post, verbose_name="Должность", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f' {self.post} {self.salary} '
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
class Payment(models.Model):
    """Способ оплаты"""
    client=models.ForeignKey(Clients, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    payment_form=models.CharField("Форма оплаты", max_length=20)
    room_category=models.ForeignKey(RoomsCategory, verbose_name="цена", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f' {self.client} {self.room_category} '
    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способ оплаты"
