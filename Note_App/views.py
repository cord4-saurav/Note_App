from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Note
from .serializers import NoteSerializers
# Create your views here.

@csrf_exempt
def noteapi(request, id=0):
    if request.method =="GET":
        note = Note.objects.all()
        note_serializers = NoteSerializers(note, many=True)
        return JsonResponse(note_serializers.data,safe=False)
    elif request.method =="POST":
        note_data = JSONParser().parse(request)
        note_serializers = NoteSerializers(data=note_data)
        if note_serializers.is_valid():
            note_serializers.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == "PUT":
        note_data = JSONParser().parse(request)
        note = Note.objects.get(name_id =note_data['name_id'])
        note_serializers = NoteSerializers(note, data=note_data)
        if note_serializers.is_valid():
            note_serializers.save()
            return JsonResponse("Updated , safe=False")
        return JsonResponse("failed to update",  safe=False)
    elif request.method == "DELETE":
        note = Note.onjects.get(name_id = id)
        note.delete()
        return JsonResponse("Delete data",safe=False)