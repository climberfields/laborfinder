from django.http import JsonResponse
from django.views import View
from .models import Contractor
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class Contractors(View):
# Create your views here.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Contractors, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        contractor_list = list(Contractor.objects.value())
        return JsonResponse({
        'Content-Type': 'application/json',
        'status': 200,
        'data': contractor_list
        }, safe=False)
    
    def post(self, request):
        data = request.body.decode('utf-8')
        print(data)
        data = json.loads(data)
        try:
            new_contractor = Contractor(name=data["name"], description=data["description"], budget=data["budget"], job_start_time=data["job_start_time"] )
        
            new_contractor.save()
            print('this is a new contractor', new_contractor.id)
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not valid data"}, safe=False)
    
    
class Contractor_detail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Contractor, self).dispatch(request, *args, **kwargs)


    def get(self, request, pk):
        contractor_list = list(Contractor.objects.filter(pk=pk).values())
        return JsonResponse({"data": contractor_list}, safe=False)
    
    def post(self, request):
        data: request.decode.body('utf-8')
        print(data)
        data=json.loads(data)
    
        try: 
            edit_contractor = Contractor.objects.get(pk=pk)
            data_key = list(data.keys())
            for key in data_key:
                if key == "name":
                    edit_contractor.name = data[key]
                if key == "description":
                    edit_contractor.description = data[key]
                if key == "budget":
                    edit_contractor.budget = data[key]
                if key == 'job_start_time':
                    edit_contractor.job_start_time = data[key]
                if key == 'pickup_available':
                    edit_contractor.pickup_available =data[key]
                if key == 'contact_info':
                    edit_contractor.contact_info = data[key]

            edit_contractor.save()
            return JsonResponse({"updated":data},  safe=False)
        except Contractor.DoesNotExist:
            return JsonResponse({"Contractor does not exist"})
    
    def delete(self, requests, pk):
        try: 
            contractor_delete = Contractor.objects.get(pk=pk)
            contractor_delete.delete()
            return JsonResponse({"Deleted": True}, safe = False)
        except:
            return JsonResponse({"error": "Not a valid key"}, safe= False)