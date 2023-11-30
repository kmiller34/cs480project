from django.db import connection
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
        if(id == 0):
            patient = Patient.objects.raw("select * from UIHealthApp_patient")
        else:
            patient = Patient.objects.raw("select * from UIHealthApp_patient where ssn = %s", [id])
        patient_serializer = PatientSerializer(patient,many=True)
        return JsonResponse(patient_serializer.data,safe=False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)

        cursor = connection.cursor()
        print(patient_data)
        sql_insert_query = """
            insert into UIHealthApp_patient
            (ssn, name, address, age, gender, race, medicalHistory, occupationalClass, phoneNumber, username_id)
            values
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        ssn = patient_data['ssn']
        name = patient_data['name']
        address = patient_data['address']
        age = patient_data['age']
        gender = patient_data['gender']
        race = patient_data['race']
        medicalHistory = patient_data['medicalHistory']
        occupationalClass = patient_data['occupationalClass']
        phoneNumber = patient_data['phoneNumber']
        username = patient_data['username_id']
    
        with connection.cursor() as cursor:
            cursor.execute(sql_insert_query, (ssn, name, address, age, gender, race, medicalHistory, occupationalClass, phoneNumber, username))

        return JsonResponse("Added Successfully", safe=False)
            
    elif request.method=='PUT':
        patient_data=JSONParser().parse(request)
        print("hello")
        print(patient_data)
        ssn =patient_data['ssn']
        update_query = """
            update UIHealthApp_patient
            set ssn = %s,
                name = %s,
                address = %s,
                age = %s,
                gender = %s,
                race = %s,
                medicalHistory = %s,
                occupationalClass = %s,
                phoneNumber = %s,
                username_id = %s
            where ssn = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(update_query, (patient_data['ssn'], patient_data['name'], patient_data['address'], patient_data['age'], patient_data['gender'], patient_data['race'], patient_data['medicalHistory'], patient_data['occupationalClass'], patient_data['phoneNumber'], patient_data['username_id'], ssn))
        if cursor.rowcount > 0:
            return JsonResponse("Update Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        patient_data=JSONParser().parse(request)
        print(patient_data)
        ssn = patient_data['ssn']
        with connection.cursor() as cursor:
            delete_query = "delete from UIHealthApp_patient where ssn = %s"
            cursor.execute(delete_query, (ssn,))
            if cursor.rowcount > 0:
                return JsonResponse({"message": "Deleted Successfully"}, safe = False)
            else:
                return JsonResponse({"message": "Failed To Delete"}, safe = False)

@csrf_exempt
def nurseApi(request, id = 0):
    print(id)
    if request.method == 'GET':
        if id == 0:
            nurse = Nurse.objects.raw("select * from UIHealthApp_nurse")
        else:
            nurse = Nurse.objects.raw("select * from UIHealthApp_nurse where employeeID = %s", [id])
        nurse_serializer = NurseSerializer(nurse,many=True)
        return JsonResponse(nurse_serializer.data,safe=False)
    elif request.method == 'POST':
        nurse_data = JSONParser().parse(request)
        print(nurse_data)
        cursor = connection.cursor()
        sql_insert_query = """
            insert into UIHealthApp_nurse
            (employeeID, address, age, phoneNumber,gender, name, username_id)
            values
            (%s, %s, %s, %s, %s, %s, %s)
        """

        employeeID = nurse_data['employeeID']
        address = nurse_data['address']
        age = nurse_data['age']
        gender = nurse_data['gender']
        name = nurse_data['name']
        phoneNumber = nurse_data['phoneNumber']
        username_id = nurse_data['username_id']
    
        with connection.cursor() as cursor:
            cursor.execute(sql_insert_query, (employeeID, address, age, phoneNumber, gender, name, username_id))

        return JsonResponse("Added Successfully", safe=False)

    elif request.method=='PUT':
        nurse_data=JSONParser().parse(request)
        print("hello")
        #employeeID=nurse_data['employeeID']
        if id == 0:
            update_query = """
                update UIHealthApp_nurse
                set employeeID = %s,
                    name = %s,
                    age = %s,
                    gender = %s
                where employeeID = %s
            """
            with connection.cursor() as cursor:
                cursor.execute(update_query, (nurse_data['employeeID'], nurse_data['name'], nurse_data['age'], nurse_data['gender'], employeeID))
        else:
            
            update_query = """
                update UIHealthApp_nurse
                set address = %s,
                    phoneNumber = %s
                where employeeID = %s
            """
            with connection.cursor() as cursor:
                cursor.execute(update_query, (nurse_data['address'], nurse_data['phoneNumber'], id))
        
        if cursor.rowcount > 0:
            return JsonResponse("Update Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employeeID = id
        with connection.cursor() as cursor:
            delete_query = "delete from UIHealthApp_nurse where employeeID = %s"
            cursor.execute(delete_query, (employeeID,))
            if cursor.rowcount > 0:
                return JsonResponse({"message": "Deleted Successfully"}, safe = False)
            else:
                return JsonResponse({"message": "Failed To Delete"}, safe = False)

@csrf_exempt
def vaccineApi(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            vaccine = Vaccine.objects.raw("select * from UIHealthApp_vaccine")
        else:
            vaccine = Vaccine.objects.raw("select * from UIHealthApp_vaccine where vaccineID = %s", [id])
        vaccine_serializer = VaccineSerializer(vaccine,many=True)
        return JsonResponse(vaccine_serializer.data,safe=False)
    elif request.method == 'POST':
        vaccine_data = JSONParser().parse(request)
        cursor = connection.cursor()
        sql_insert_query = """
            insert into UIHealthApp_vaccine
            (vaccineID, companyName, name, doses,availability, onHold, textDesc)
            values
            (%s, %s, %s, %s, %s, %s, %s)
        """

        vaccineID = vaccine_data['vaccineID']
        companyName = vaccine_data['companyName']
        name = vaccine_data['name']
        doses = vaccine_data['doses']
        availability = vaccine_data['availability']
        onHold = vaccine_data['onHold']
        textDesc = vaccine_data['textDesc']
    
        with connection.cursor() as cursor:
            cursor.execute(sql_insert_query, (vaccineID, companyName, name, doses, availability, onHold, textDesc))
        return JsonResponse("Added Successfully", safe=False)
    elif request.method=='PUT':
        vaccine_data=JSONParser().parse(request)
        vaccineID =vaccine_data['vaccineID']
        update_query = """
            update UIHealthApp_vaccine
            set vaccineID = %s,
                companyName = %s,
                name = %s,
                doses = %s,
                availability = %s,
                onHold = %s,
                textDesc = %s
            where vaccineID = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(update_query, (vaccine_data['vaccineID'], vaccine_data['companyName'], vaccine_data['name'], vaccine_data['doses'], vaccine_data['availability'], vaccine_data['onHold'], vaccine_data['textDesc'], vaccineID))
        if cursor.rowcount > 0:
            return JsonResponse("Update Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        
        vaccineID = id
        with connection.cursor() as cursor:
            delete_query = "delete from UIHealthApp_vaccine where vaccineID = %s"
            cursor.execute(delete_query, (vaccineID,))
            if cursor.rowcount > 0:
                return JsonResponse({"message": "Deleted Successfully"}, safe = False)
            else:
                return JsonResponse({"message": "Failed To Delete"}, safe = False)

@csrf_exempt
def vaccinationRecordApi(request, id = 0):

    if request.method == 'GET':
        sql_get_query = """
            select 
            UIHealthApp_vaccinationRecord.recordID,
            UIHealthApp_vaccinationRecord.doses,
            UIHealthApp_vaccinationRecord.timeSlot,
            UIHealthApp_patient.name,
            UIHealthApp_nurse.name,
            UIHealthApp_vaccine.name
            from UIHealthApp_vaccinationRecord join UIHealthApp_patient ON UIHealthApp_patient.ssn = UIHealthApp_vaccinationRecord.patientID_id
            join UIHealthApp_nurse ON UIHealthApp_nurse.employeeID = UIHealthApp_vaccinationRecord.nurseID_id
            join UIHealthApp_vaccine ON UIHealthApp_vaccine.vaccineID = UIHealthApp_vaccinationRecord.vaccineID_id
        """

        with connection.cursor() as cursor:
            cursor.execute(sql_get_query)
            result = cursor.fetchall()

        # Assuming you have a list of dictionaries from the query result
        data = [
            {
                'recordID': row[0],
                'doses': row[1],
                'timeSlot': row[2],
                'patient_name': row[3],
                'nurse_name': row[4],
                'vaccine_name': row[5],
            }
            for row in result
        ]

        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        vaccineRecord_data = JSONParser().parse(request)
        print(vaccineRecord_data)
        cursor = connection.cursor()
        sql_insert_query = """
            insert into UIHealthApp_vaccinationRecord
            (doses, timeSlot, nurseID_id, patientID_id,vaccineID_id, recordID)
            values
            (%s, %s, %s, %s, %s, %s)
        """

        sql_update_hold = """
            update UIHealthApp_vaccine
                set onHold = onHold - 1
                set availability = availability - 1
                where vaccineID = (%s)
        """

        vaccineID = vaccineRecord_data['vaccine']
        nurseID = vaccineRecord_data['nurse']
        patientID_id = vaccineRecord_data['patient']
        timeSlot = vaccineRecord_data['timeSlot']
        doses = vaccineRecord_data['doses']
        recordID = vaccineRecord_data['recordID']
    
        with connection.cursor() as cursor:
            cursor.execute(sql_insert_query, (doses, timeSlot, nurseID, patientID_id, vaccineID, recordID))
            print("Before update - vaccineID:", vaccineID)
            cursor.execute(sql_update_hold, (vaccineID,))
            print("After update - vaccineID:", vaccineID)
        return JsonResponse("Added Successfully", safe=False)
    elif request.method=='PUT':
        vaccinationRecord_data=JSONParser().parse(request)
        vaccinationRecord=VaccinationRecord.objects.get(recordID=vaccinationRecord_data['recordID'])
        vaccinationRecord_serializer=VaccinationRecordSerializer(vaccinationRecord,data=vaccinationRecord_data)
        if vaccinationRecord_serializer.is_valid():
            vaccinationRecord_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':

        nurseID = id
        with connection.cursor() as cursor:
            delete_query = "delete from UIHealthApp_vaccinationRecord where recordID = %s"
            cursor.execute(delete_query, (id,))
            if cursor.rowcount > 0:
                return JsonResponse({"message": "Deleted Successfully"}, safe = False)
            else:
                return JsonResponse({"message": "Failed To Delete"}, safe = False)

@csrf_exempt
def vaccinationSchedulingApi(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            vaccine = VaccinationScheduling.objects.raw("select * from UIHealthApp_vaccinationScheduling")
        else:
            vaccine = VaccinationScheduling.objects.raw("select * from UIHealthApp_vaccinationScheduling where vaccID = %s", [id])
        vaccinationScheduling_serializer = VaccinationSchedulingSerializer(vaccine,many=True)
        return JsonResponse(vaccinationScheduling_serializer.data,safe=False)
    elif request.method == 'POST':
        vaccineSchedule_data = JSONParser().parse(request)
        print(vaccineSchedule_data)
        cursor = connection.cursor()
        sql_insert_query = """
            insert into UIHealthApp_vaccinationScheduling
            (vaccID, timeSlot, nurseID_id, patientID_id)
            values
            (%s, %s, %s, %s)
        """
        vaccID = vaccineSchedule_data['recordID']
        nurseID = vaccineSchedule_data['nurse']
        patientID_id = vaccineSchedule_data['patient']
        timeSlot = vaccineSchedule_data['timeSlot']
    
        with connection.cursor() as cursor:
            cursor.execute(sql_insert_query, (vaccID, timeSlot, nurseID, patientID_id))
        return JsonResponse("Added Successfully", safe=False)
    elif request.method=='PUT':
        vaccinationScheduling_data=JSONParser().parse(request)
        vaccinationScheduling=VaccinationScheduling.objects.get(vaccID=vaccinationScheduling_data['vaccID'])
        vaccinationScheduling_serializer=VaccinationSchedulingSerializer(vaccinationScheduling,data=vaccinationScheduling_data)
        if vaccinationScheduling_serializer.is_valid():
            vaccinationScheduling_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        
        vaccineScheduleID = id
        with connection.cursor() as cursor:
            delete_query = "delete from UIHealthApp_vaccinationScheduling where vaccID = %s"
            cursor.execute(delete_query, (id,))
            if cursor.rowcount > 0:
                return JsonResponse({"message": "Deleted Successfully"}, safe = False)
            else:
                return JsonResponse({"message": "Failed To Delete"}, safe = False)

@csrf_exempt
def credentialsApi(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            credentials = Credentials.objects.raw("select * from UIHealthApp_credentials")
        else:
            credentials = Credentials.objects.raw("select * from UIHealthApp_credentials where username = %s", [id])
        credentials_serializer = CredentialsSerializer(credentials,many=True)
        return JsonResponse(credentials_serializer.data,safe=False)
    elif request.method == 'POST':
        credentials_data = JSONParser().parse(request)
        cursor = connection.cursor()
        sql_insert_query = """
            insert into UIHealthApp_credentials
            (username, password, position)
            values
            (%s, %s, %s)
        """

        username = credentials_data['username']
        password = credentials_data['password']
        position = credentials_data['position']
    
        with connection.cursor() as cursor:
            cursor.execute(sql_insert_query, (username, password, position))
        return JsonResponse("Added Successfully", safe=False)
    elif request.method=='PUT':
        credentials_data=JSONParser().parse(request)
        username =credentials_data['username']
        update_query = """
            update UIHealthApp_credentials
            set username = %s,
                password = %s,
                position = %s
            where username = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(update_query, (credentials_data['username'], credentials_data['password'], credentials_data['position'], username))
        if cursor.rowcount > 0:
            return JsonResponse("Update Successfully", safe=False)
        else:
            return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        credentials_data=JSONParser().parse(request)
        username = credentials_data['username']
        print('hello')
        print(username)
        with connection.cursor() as cursor:
            delete_query = "delete from UIHealthApp_credentials where username = %s"
            cursor.execute(delete_query, (username,))
            if cursor.rowcount > 0:
                return JsonResponse({"message": "Deleted Successfully"}, safe = False)
            else:
                return JsonResponse({"message": "Failed To Delete"}, safe = False)
