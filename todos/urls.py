from django .conf .urls import url
from . import views



urlpatterns= [
url(r'^$', views.home),
url(r'^todocreate/',views.todocreate, name="create"),
url(r'^workcreate/',views.worktodocreate, name="work"),
url(r'^details/(?P<id>\w{0,50})/$',views.details,),
]
