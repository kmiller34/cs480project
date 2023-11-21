from django.db import models

# Create your models here.

def validate_length(phone):
    if not (phone.isdigit() and len(phone) == 10):
        raise ValidateError('%(phone)s must be 10 digits', params={'phone':phone})
def IDVarifier(identity):
    if not (identity.isdigit() and len(identity) == 9):
        raise ValidateError('%(id)s must be 9 digits', params={'identity':id})
class Patient(models.Model):
    name = models.CharField(max_length = 50, default = "None")
    ssn = models.CharField(primary_key = True, max_length = 9)
    address = models.CharField(max_length = 50,default = '123 fake st')
    age = models.IntegerField(default = 0)
    gender = models.CharField(default = 'None', max_length = 6)
    race = models.CharField(default = 'None', max_length = 10)
    medicalHistory = models.CharField(max_length = 200, default = 'None')
    occupationalClass = models.CharField(max_length = 100, default = 'None')
    phoneNumber = models.CharField(max_length = 10,validators = [validate_length], default = '1234567890')
    username = models.ForeignKey("Credentials",max_length = 10, default = "default", on_delete=models.SET_DEFAULT)
class Nurse(models.Model):
    employeeID = models.CharField(primary_key = True, max_length = 9, validators = [IDVarifier],default = '123456789')
    address = models.CharField(max_length = 50, default = '124 fake st')
    age = models.IntegerField(default = 0)
    phoneNumber = models.CharField(max_length = 10,validators = [validate_length], default = '1234567890')
    gender = models.CharField(default = 'None', max_length = 6)
    name = models.CharField(default = 'None', max_length = 20)
    username = models.ForeignKey("Credentials",max_length = 10, default = "default", on_delete=models.SET_DEFAULT)
class Vaccine(models.Model):
    vaccineID = models.CharField(primary_key = True, max_length = 9, validators = [IDVarifier],default = '123456789')
    companyName = models.CharField(max_length = 50, default = 'Fake Company')
    name = models.CharField(max_length = 50, default = 'vaccine')
    doses = models.IntegerField(default = 0)
    availability = models.IntegerField(default = 0)
    onHold = models.IntegerField(default = 0)
    textDesc = models.CharField(max_length = 200, default = 'None')
class VaccinationScheduling(models.Model):
    vaccID = models.AutoField(primary_key = True, default = 1)
    patientID = models.ForeignKey("Patient", max_length = 9,default = '123456789',on_delete=models.SET_DEFAULT)
    nurseID = models.ForeignKey("Nurse", max_length = 9,default = '123456789',on_delete=models.SET_DEFAULT)
    timeSlot = models.CharField(max_length = 30, default = "None")
    # vaccineID = models.ForeignKey("Vaccine", max_length = 9, validators = [IDVarifier],default = '123456789',on_delete=models.SET_DEFAULT)
class VaccinationRecord(models.Model):
    recordID = models.AutoField(primary_key = True, default = 1)
    patientID = models.ForeignKey("Patient", max_length = 9,default = '123456789',on_delete=models.SET_DEFAULT)
    nurseID = models.ForeignKey("Nurse", max_length = 9,default = '123456789',on_delete=models.SET_DEFAULT)
    vaccineID = models.ForeignKey("Vaccine", max_length = 9,default = '123456789',on_delete=models.SET_DEFAULT)
    doses = models.IntegerField(default = 0)
class Credentials(models.Model):
    password = models.CharField(max_length = 30)
    username = models.CharField(primary_key = True, max_length = 10,default = "default")
    position = models.CharField(max_length = 10)