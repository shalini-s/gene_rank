# tutorial/tables.py
import django_tables2 as tables
from .models import Person

# class PersonTable(tables.Table):
#     class Meta:
#         model = Person
#         template_name = 'django_tables2/bootstrap.html'

class NameTable(tables.Table):
    Feature = tables.Column()
    Gradient = tables.Column(attrs={'td': {'width': '150'}})
    Links = tables.Column(attrs={'td': {'width': '200'}})
    #Links = tables.TemplateColumn('<a href="https://www.ncbi.nlm.nih.gov/gene/?term={{record.id}}">Edit</a>')

