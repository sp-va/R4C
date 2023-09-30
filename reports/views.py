from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
import os

from reports.utils import create_excel
from R4C.settings import MEDIA_ROOT, BASE_DIR

def get_latest_report(request):
    if request.method == 'GET':
        create_excel()
        file_location = os.path.join(MEDIA_ROOT, 'reports/report.xls')
        

        with open(file_location, 'rb') as file:
            file_data = file.read()
                
            response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=report.xls'

            return response
