from django.shortcuts import render
from katalog.models import CatalogItem

mhs_name = 'Maulana Bayu Risma Santoso Sari'
studentID = 2106750401

def show_catalog(req):
    data_catalog_item = CatalogItem.objects.all()
    context  = {
        'name' : mhs_name,
        'studentID': studentID,
        'list_item': data_catalog_item}
    return render(req, 'katalog.html', context)
