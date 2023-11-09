from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UIHealthApp.models import Patient,Nurse,Vaccine,VaccinationScheduling,VaccinationRecord, Credentials
from UIHealthApp.serializers import PatientSerializer,NurseSerializer,VaccineSerializer,VaccinationSchedulingSerializer,VaccinationRecordSerializer, CredentialsSerializer

# Create your views here.

@csrf_exempt
def patientApi(request, id = 0):
    if request.method == 'GET':
        patient = Patient.objects.all()
        patient_serializer = PatientSerializer(patient,many=True)
        return JsonResponse(patient_serializer.data,safe=False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        patient_data=JSONParser().parse(request)
        patient=Patient.objects.get(PatientID=patient_data['PatientID'])
        patient_serializer=PatientSerializer(patient,data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        patient=Patient.objects.get(PatientID=id)
        patient.delete()
        return JsonResponse("Deleted Success")

@csrf_exempt
def nurseApi(request, id = 0):
    if request.method == 'GET':
        nurse = Nurse.objects.all()
        nurse_serializer = NurseSerializer(nurse,many=True)
        return JsonResponse(nurse_serializer.data,safe=False)
    elif request.method == 'POST':
        nurse_data = JSONParser().parse(request)
        nurse_serializer = NurseSerializer(data=nurse_data)
        if nurse_serializer.is_valid():
            nurse_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        nurse_data=JSONParser().parse(request)
        nurse=Nurse.objects.get(NurseID=nurse_data['NurseID'])
        nurse_serializer=NurseSerializer(nurse,data=nurse_data)
        if nurse_serializer.is_valid():
            nurse_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        nurse=Nurse.objects.get(NurseID=id)
        nurse.delete()
        return JsonResponse("Deleted Success")

@csrf_exempt
def vaccineApi(request, id = 0):
    if request.method == 'GET':
        vaccine = Vaccine.objects.all()
        vaccine_serializer = VaccineSerializer(vaccine,many=True)
        return JsonResponse(vaccine_serializer.data,safe=False)
    elif request.method == 'POST':
        vaccine_data = JSONParser().parse(request)
        vaccine_serializer = VaccineSerializer(data=vaccine_data)
        if vaccine_serializer.is_valid():
            vaccine_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        vaccine_data=JSONParser().parse(request)
        vaccine=Vaccine.objects.get(VaccineID=vaccine_data['VaccineID'])
        vaccine_serializer=VaccineSerializer(vaccine,data=vaccine_data)
        if vaccine_serializer.is_valid():
            vaccine_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        vaccine=Vaccine.objects.get(VaccineID=id)
        vaccine.delete()
        return JsonResponse("Deleted Success")

@csrf_exempt
def vaccinationRecordApi(request, id = 0):
    if request.method == 'GET':
        vaccinationRecord = VaccinationRecord.objects.all()
        vaccinationRecord_serializer = VaccinationRecordSerializer(vaccinationRecord,many=True)
        return JsonResponse(vaccinationRecord_serializer.data,safe=False)
    elif request.method == 'POST':
        vaccinationRecord_data = JSONParser().parse(request)
        vaccinationRecord_serializer = VaccinationRecordSerializer(data=vaccinationRecord_data)
        if vaccinationRecord_serializer.is_valid():
            vaccinationRecord_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        vaccinationRecord_data=JSONParser().parse(request)
        vaccinationRecord=VaccinationRecord.objects.get(VacciantionRecordID=vaccinationRecord_data['VaccinationRecordID'])
        vaccinationRecord_serializer=VaccinationRecordSerializer(vaccinationRecord,data=vaccinationRecord_data)
        if vaccinationRecord_serializer.is_valid():
            vaccinationRecord_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        vaccinationRecord=VaccinationRecord.objects.get(VaccinationRecordID=id)
        vaccinationRecord.delete()
        return JsonResponse("Deleted Success")

@csrf_exempt
def vaccinationSchedulingApi(request, id = 0):
    if request.method == 'GET':
        vaccinationScheduling = VaccinationScheduling.objects.all()
        vaccinationScheduling_serializer = VaccinationSchedulingSerializer(vaccinationScheduling,many=True)
        return JsonResponse(vaccinationScheduling_serializer.data,safe=False)
    elif request.method == 'POST':
        vaccinationScheduling_data = JSONParser().parse(request)
        vaccinationScheduling_serializer = VaccinationSchedulingSerializer(data=vaccinationScheduling_data)
        if vaccinationScheduling_serializer.is_valid():
            vaccinationScheduling_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        vaccinationScheduling_data=JSONParser().parse(request)
        vaccinationScheduling=VaccinationScheduling.objects.get(VaccinationSchedulingID=vaccinationScheduling_data['VaccinationSchedulingID'])
        vaccinationScheduling_serializer=VaccinationSchedulingSerializer(vaccinationScheduling,data=vaccinationScheduling_data)
        if vaccinationScheduling_serializer.is_valid():
            vaccinationScheduling_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        vaccinationScheduling=VaccinationScheduling.objects.get(VaccinationSchedulingID=id)
        vaccinationScheduling.delete()
        return JsonResponse("Deleted Success")

@csrf_exempt
def credentialsApi(request, id = 0):
    if request.method == 'GET':
        credentials = Credentials.objects.all()
        credentials_serializer = CredentialsSerializer(credentials,many=True)
        return JsonResponse(credentials_serializer.data,safe=False)
    elif request.method == 'POST':
        credentials_data = JSONParser().parse(request)
        credentials_serializer = CredentialsSerializer(data=credentials_data)
        if credentials_serializer.is_valid():
            credentials_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        credentials_data=JSONParser().parse(request)
        credentials=Credentials.objects.get(CredentialsID=credentials_data['CredentialsID'])
        credentials_serializer=CredentialsSerializer(credentials,data=credentials_data)
        if credentials_serializer.is_valid():
            credentials_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        credentials=Credentials.objects.get(CredentialsID=id)
        credentials.delete()
        return JsonResponse("Deleted Success")
