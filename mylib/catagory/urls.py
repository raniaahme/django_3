
urlpatterns=[
path('Add', views.Add, name='Catagory_Add'),
    path('Update/<int:catid>', views.Update, name='Catagory_Update'),

]