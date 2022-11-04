from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def operation(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        operation_type = body['operation_type']
        x = body['x']
        y = body['y']
        if operation_type == 'addition':
            result = x + y
        elif operation_type == 'subtraction':
            result = x - y
        elif operation_type == 'multiplication':
            result = x * y
        elif operation_type == 'division':
            result = x / y
        else:
            return HttpResponse(status=400)
        response_data = {'slackUsername': 'bolex', 'result': result, 'operation_type': operation_type}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(status=405)