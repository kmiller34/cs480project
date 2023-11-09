from rest_framework import serializers
from UIHealthApp.models import Patient, Vaccine, Nurse, VaccinationScheduling, VaccinationRecord, Credentials

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields=('ssn','address','age','gender','race','medicalHistory','occupationalClass','phoneNumber', 'username')

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ('employeeID', 'address', 'age', 'phoneNumber', 'gender', 'name','username')

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine 
        fields = ('vaccineID', 'companyName', 'name', 'doses', 'availability', 'onHold', 'textDesc')

class VaccinationSchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationScheduling 
        fields = ('patientID', 'nurseID', 'timeSlot', 'vaccineID')

class VaccinationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord 
        fields = ('patientID', 'nurseID', 'vaccineID', 'doses')

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ('password', 'username', 'postion')

        