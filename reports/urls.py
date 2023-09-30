from django.urls import path

from reports.views import get_latest_report

urlpatterns = [
    path('get_latest_report/', get_latest_report, name='Сводка по суммарным показателям производства роботов за неделю'),
]