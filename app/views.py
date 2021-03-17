from django.shortcuts import render, redirect
from django.views import View

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import *
from .forms import *


class BaseView(View):
    """главная страница"""

    def get(self, request):
        template = 'app/home.html/'
        return render(request, template, context={'user': request.user})


class NoteDetailView(View):
    """заметка"""

    def get(self, request, pk):
        template = 'app/note_products.html/'
        products_list = Product.objects.select_related().filter(note__pk=pk)
        note = Note.objects.get(pk=pk)

        if note.owner == request.user:
            context = {'objects_list': products_list, 'note': note}
            return render(request, template, context)
        else:
            return redirect('home')


class DeleteNote(View):
    """удаление заметки"""

    def post(self, request, pk):
        noteToDelete = Note.objects.get(id=pk)
        noteToDelete.delete()
        return JsonResponse({'result': 'ok'}, status=200)


class EditNote(View):
    """изменение заметки"""

    def get(self, request, note_pk):
        note = Note.objects.get(pk=note_pk)
        template = 'app/edit_note.html'
        form = NoteForm(instance=note)
        context = {'note': note, 'form': form}

        return render(request, template, context)

    def post(self, request, note_pk):
        noteToEdit = Note.objects.get(pk=note_pk)
        bound_form = NoteForm(request.POST, instance=noteToEdit)

        if bound_form.is_valid():
            bound_form.save()

        return redirect('home')


class AddProduct(View):
    """добавление продукта в заметку"""

    def get(self, request, note_pk):
        note = Note.objects.get(pk=note_pk)
        form = ProductForm()
        context = {'note': note, 'form': form}
        return render(request, 'app/add_product.html', context)

    def post(self, request, note_pk):
        note = Note.objects.get(pk=note_pk)
        bound_form = ProductForm(request.POST)

        if bound_form.is_valid():
            new_product = bound_form.save(commit=False)
            new_product.note = note
            new_product.save()

        return redirect('note_products', note_pk)


class ComplatedProduct(View):
    """продукт куплен"""

    def post(self, request, product_pk):
        product = Product.objects.get(pk=product_pk)
        product.completed = True
        product.save()
        return JsonResponse({'result': 'ok'}, status=200)


class NotComplatedProduct(View):
    """продукт не куплен"""

    def post(self, request, product_pk):
        product = Product.objects.get(pk=product_pk)
        product.completed = False
        product.save()
        return JsonResponse({'result': 'ok'}, status=200)


class DeleteProduct(View):
    """удаление продукта из заметки"""

    def post(self, request, product_pk):
        product = Product.objects.select_related().get(pk=product_pk)
        product.delete()
        return JsonResponse({'result': 'ok'}, status=200)
