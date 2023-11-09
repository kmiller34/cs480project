from django.urls import re_path
from UIHealthApp import views

urlpatterns=[
    re_path(r'^patient$',views.patientApi),
    re_path(r'^patient/([0-9]+)$', views.patientApi),

    re_path(r'^nurse$',views.nurseApi),
    re_path(r'^nurse/([0-9]+)$', views.nurseApi),

    re_path(r'^vaccine$',views.vaccineApi),
    re_path(r'^vaccine/([0-9]+)$', views.vaccineApi),

    re_path(r'^vaccinationRecord$',views.vaccinationRecordApi),
    re_path(r'^vaccinationRecord/([0-9]+)$', views.vaccinationRecordApi),

    re_path(r'^vaccinationScheduling$',views.vaccinationSchedulingApi),
    re_path(r'^vaccinationScheduling/([0-9]+)$', views.vaccinationSchedulingApi),

    re_path(r'^credentials$',views.credentialsApi),
    re_path(r'^credentials/([0-9]+)$', views.credentialsApi)
]