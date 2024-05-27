from django.db import models

# Create your models here.

City_Choices =(
    ('Bengaluru','Bengaluru'),
    ('Bhubaneswar','Bhubaneswar'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Jaipur','Jaipur'),
    ('Kolkata','Kolkata'),
    ('Mangaluru','Mangaluru'),
    ('Mysuru','Mysuru'),
    ('Patiala','Patiala'),
    ('Pune','Pune'),
    ('Salem','Salem'),
    ('Vijayawada','Vijayawada'),
)


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=City_Choices,default='Bengaluru')
    location = models.CharField(max_length=100)
    contact = models.IntegerField()
    
    def __str__(self):
        return self.name


# class CentreOfExcellence(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='centres')

#     def __str__(self):
#         return self.name

# class Specialty(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     centre = models.ForeignKey(CentreOfExcellence, on_delete=models.CASCADE, related_name='specialties')

#     def __str__(self):
#         return self.name

# class Doctor(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='doctors')
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Patient(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     dob = models.DateField()
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Appointment(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
#     date = models.DateTimeField()
#     reason = models.TextField()

#     def __str__(self):
#         return f"Appointment for {self.patient} with {self.doctor} on {self.date}"

# class MedicalRecord(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
#     description = models.TextField()
#     date = models.DateField()

#     def __str__(self):
#         return f"Medical Record of {self.patient} on {self.date}"

# class Billing(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='billings')
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField()

#     def __str__(self):
#         return f"Billing for {self.patient} on {self.date}"

# class Service(models.Model):
#     name = models.CharField(max_length=100)
#     specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='services')
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Feedback(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='feedbacks')
#     comments = models.TextField()
#     rating = models.IntegerField()
#     date = models.DateField()

#     def __str__(self):
#         return f"Feedback from {self.patient} on {self.date}"
