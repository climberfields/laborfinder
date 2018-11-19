from django.shortcuts import render
from django.views import View
from .modles import Book
import json

class Contractor(View)
# Create your views here.

def dispatch(self, request, *args, **kwargs):
    return super(Contractor, self).dispatch(request, *args, **kwargs)

def get(self, request)

contractor_list = list(Contractor.objects.value())
    return JsonResponse({
        'Content-Type': 'application/json',
        'status': 200,
        'data': contractor_list
    }, safe=False)

def post(self, request):
    data: request.decode.body('utf-8')
    print(data)
    data=json.loads(data)
    
    try: 
        edit_contractor = Contractor.objects.get(pk=pk)
        data_key = list(data.keys())
        for key in data_key:
            if key == "name"
            edit_contractor.name = data[key]
            if key == "description"
            edit_contractor.description = data[key]
            if key == budget "budget"
            edit_contractor.budget = data[key]
            if key == 'job_start_time'
            edit_contractor.job_start_time = data[key]
            if key == 'pickup_available'
            edit_contractor.pickup_available =data[key]
            if key == 'contact_info'
            edit_contractor.contact_info = data[key]
            
        edit_contractor.save()
        return JsonResponse({"updated":data},  safe=False)
    except Contractor.DoesNotExist:
        return JsonResponse({"Contractor does not exist"})
    
    def delete(self, requests, pk)
        try: 
            contractor_delete = Contractor.objects.get(pk=pk)
            contractor_delete.delete()
            return JsonResponse({"Deleted": True}, safe = False)
        except:
            return JsonResponse({"error": "Not a valid key"}, safe= False)