from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
import json, time
from .ocean_predictor import main

DATA_REQUIRE = "اطلاعات را به شکل کامل وارد کنید."

@permission_classes((permissions.AllowAny,))
class Predict(APIView):
    def post(self, request):
        rec_data = json.loads(request.read().decode('utf-8'))
        personal_text = rec_data['personal_text']
        answer = main.predict(personal_text)
        answer_text = []
        time.sleep(5)
        for item in answer:
            if item == 0:
                answer_text.append("NO")
            else:
                answer_text.append("YES")
        if not personal_text:
            return Response(data={"response_code": 401, "error_msg": DATA_REQUIRE})

        return Response(data={'response_code': 200, 'ocean': answer_text})
