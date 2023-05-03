from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=9)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'name: {self.name}\nphone: {self.phone}\nemail: {self.email}'


class Flight(models.Model):
    flight_id = models.IntegerField()
    takeoff_date_time = models.IntegerField()
    takeoff_airport = models.CharField(max_length=255)
    landing_data_time = models.IntegerField()
    landing_airport = models.CharField(max_length=255)
    airplane_id = models.IntegerField()


class Purchase(models.Model):
    purchase_id = models.IntegerField()
    purchase_date = models.IntegerField()


class Seat_type(models.Model):
    seat_type_id = models.IntegerField()
    name = models.CharField(max_length=255)


class Passenger(models.Model):
    passenger_id = models.IntegerField()
    dni = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)


class Boarding_pass(models.Model):
    boarding_pass_id = models.IntegerField()
    purchase_id = models.IntegerField()
    passenger_id = models.IntegerField()
    seat_type_id = models.IntegerField()
    seat_id = models.IntegerField()
    flight_id = models.IntegerField()


class Seat(models.Model):
    seat_id = models.IntegerField()
    seat_column = models.CharField(max_length=255)
    seat_row = models.IntegerField()
    seat_type_id = models.IntegerField()
    airplane_id = models.IntegerField()


class Airplane(models.Model):
    airplane_id = models.IntegerField()
    name = models.CharField(max_length=255)
