# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django_tables2 import RequestConfig
from django.http import HttpResponse
from .models import Person
from .tables import NameTable

key = []
rank = []
link = []

import csv

with open('/Users/miaschoening/Desktop/gene_rank/one/gradients.rnk','r') as csvfile: 
	delimiter='\t'
	delimiter = delimiter.encode('utf-8')
	reader = csv.reader(csvfile, delimiter=delimiter)
	for row in reader:
		key.append(row[0])
		rank.append(row[1])
		link.append("https://www.ncbi.nlm.nih.gov/gene/?term=" + row[0])
	#for i in key:
	#	link.append(i)

def people(request):
	#data = [
    #{'Feature': 'Bradley', 'Gradient':'1'},
#	]
#	d = {}


	data = [
		{'Feature': 'Bradley'},
		{'Gradient': '1'},
		{'Links': 'Stevie'},
	]

	dictlist = [dict() for x in range(399)]
	for i in range(0,399):
		dictlist[i]['Feature'] = key[i]
		dictlist[i]['Gradient'] = rank[i]
		dictlist[i]['Links'] = link[i]
	#print(d)
	#print(rank)
	table = NameTable(dictlist)
	RequestConfig(request, paginate = {'per_page': 399}).configure(table)
	return render(request, 'one/people.html', {'table': table})


# def people(request):
#     table = PersonTable(Person.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'people.html', {'table': table})

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def simple_list(request):
#     queryset = Simple.objects.all()
#     table = SimpleTable(queryset)
#     return render(request, 'simple_list.html', {'table': table})
    #return render(request, 'one/people.html', {'people': Person.objects.all()})
