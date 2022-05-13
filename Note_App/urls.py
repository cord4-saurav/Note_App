from django.conf.urls import url
from Note_App import views

urlpatterns =[
    url('note',views.noteapi),
    url('note/<int:id>', views.noteapi)
]