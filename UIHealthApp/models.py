from django.db import models

# Create your models here.

def validate_length(phone):
    if not (phone.isdigit() and len(phone) == 10):
        raise ValidateError('%(phone)s must be 10 digits', params={'phone':phone})
def IDVarifier(id):
    if not (id.isdigit() and len(id) == 9):
        raise ValidateError('%(id)s must be 9 digits', params={'id':id})
class Patient(models.Model):
    ssn = models.CharField(primary_key = True, max_length = 9)
    address = models.CharField(max_length = 50,default = '123 fake st')
    age = models.IntegerField(default = 0)
    gender = models.CharField(default = 'None')
    race = models.CharField(default = 'None')
    medicalHistory = models.CharField(max_length = 200, default = 'None')
    occupationalClass = models.CharField(max_length = 100, default = 'None')
    phoneNumber = models.CharField(max_length = 10,validators = [validate_length], default = '1234567890')
class Nurse(models.Model):
    employeeID = models.CharField(primary_key = True, max_length = 9, validators = [IDVarifier],default = '123456789')
    address = models.CharField(max_length = 50, default = '124 fake st')
    age = models.IntegerField(default = 0)
    phoneNumber = models.CharField(max_length = 10,validators = [validate_length], default = '1234567890')
    gender = models.CharField(default = 'None')
    name = models.CharField(default = 'None')
class Vaccine(models.Model):
    vaccineID = models.CharField(primary_key = True, max_length = 9, validators = [IDVarifier],default = '123456789')
    companyName = models.CharField(max_length = 50, default = 'Fake Company')
    name = models.CharField(max_length = 50, default = 'vaccine')
    doses = models.IntegerField(default = 0)
    availability = models.IntegerField(default = 0)
    onHold = models.IntegerField(default = 0)
    textDesc = models.CharField(max_length = 200, default = 'None')
class VaccinationScheduling(models.Model):
    patientID = models.ForeignKey("Patient", max_length = 9, validators = [IDVarifier],default = '123456789')
    nurseID = models.ForeignKey("Nurse", max_length = 9, validators = [IDVarifier],default = '123456789')
    timeSlot = models.DateField()
    vaccineID = models.ForeignKey("Vaccine", max_length = 9, validators = [IDVarifier],default = '123456789')
class vaccinationRecord(models.Model):
    patientID = models.ForeignKey("Patient", max_length = 9, validators = [IDVarifier],default = '123456789')
    nurseID = models.ForeignKey("Nurse", max_length = 9, validators = [IDVarifier],default = '123456789')
    vaccineID = models.ForeignKey("Vaccine", max_length = 9, validators = [IDVarifier],default = '123456789')
    doses = models.IntegerField(default = 0)