from django.shortcuts import render
from django.db import connection  # Імпортуйте об'єкт підключення
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def main(request):
    print('rerer')
    return render(request, 'main.html')
@csrf_exempt
def search(request):
    if request.method == "POST":
        search_query = request.POST.get('search_query', '')
       

        # Ваш SQL-запит для пошуку в базі даних MySQL
        query = f'''
        SELECT edovidnyk.gpu.modelgpu, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.gpu
            INNER JOIN edovidnyk.producer ON edovidnyk.gpu.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.gpu.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.gpu.modelgpu LIKE %s

            UNION
            SELECT edovidnyk.cpu.modelcpu, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.cpu
            INNER JOIN edovidnyk.producer ON edovidnyk.cpu.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.cpu.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.cpu.modelcpu LIKE %s

            UNION
            SELECT edovidnyk.device.modeldevice, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.device
            INNER JOIN edovidnyk.producer ON edovidnyk.device.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.device.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.device.modeldevice LIKE %s

            UNION
            SELECT edovidnyk.networkcard.modelnetworkcard, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.networkcard
            INNER JOIN edovidnyk.producer ON edovidnyk.networkcard.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.networkcard.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.networkcard.modelnetworkcard LIKE %s

             UNION
            SELECT edovidnyk.ram.modelram, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.ram
            INNER JOIN edovidnyk.producer ON edovidnyk.ram.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.ram.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.ram.modelram LIKE %s

            UNION
            SELECT edovidnyk.rom.modelrom, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.rom
            INNER JOIN edovidnyk.producer ON edovidnyk.rom.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.rom.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.rom.modelrom LIKE %s
            
            UNION
            SELECT edovidnyk.rom.modelrom, edovidnyk.producer.name, edovidnyk.idpage.mainphoto
            FROM ((edovidnyk.rom
            INNER JOIN edovidnyk.producer ON edovidnyk.rom.producer = edovidnyk.producer.idproducer)
            INNER JOIN edovidnyk.idpage ON edovidnyk.rom.idpage = edovidnyk.idpage.ididPAGE)
            WHERE edovidnyk.producer.name LIKE %s OR edovidnyk.rom.modelrom LIKE %s

        '''
        with connection.cursor() as cursor:
            cursor.execute(query, [f'%{search_query}%'] * 14)
            search_results = cursor.fetchall()
        #if search_results:#щоб повернути іф перенеси блок редер в нього 


        print(search_results)
            # Повернути результати пошуку в шаблон, де ви їх 
        return render(request, 'search_results.html', {'search_results': search_results})
        
        
    else:
        return HttpResponse('This page is only accessible via POST request')


