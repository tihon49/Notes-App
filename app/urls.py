from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note_products'),
    path('delete/<int:pk>/', DeleteNote.as_view(), name='delete_note'),
    path('editNote/<int:note_pk>/', EditNote.as_view(), name='edit_note'),
    path('add_product/<int:note_pk>/', AddProduct.as_view(), name='add_product'),
    path('completed_product/<int:product_pk>/', ComplatedProduct.as_view(), name='completed_product'),
    path('not_completed_product/<int:product_pk>/', NotComplatedProduct.as_view(), name='completed_product'),
    path('delete_product/<int:product_pk>/', DeleteProduct.as_view(), name='delete_product'),
]