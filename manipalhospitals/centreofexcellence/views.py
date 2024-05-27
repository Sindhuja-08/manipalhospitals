
from django.shortcuts import render, get_object_or_404
from .models import Hospital, City_Choices

# Create your views here.
def city_list(request):
    cities = City_Choices
    selected_city = request.GET.get('city')
    locations = None
    hospital_by_location = {}
    
    if selected_city:
        locations = Hospital.objects.filter(city=selected_city).values_list('location', flat=True).distinct()
        for location in locations:
            hospital_by_location[location] = Hospital.objects.filter(city=selected_city, location=location)
    
    return render(request, 'city_list.html', {
        'cities': cities,
        'hospital_by_location': hospital_by_location,
        'selected_city': selected_city
    })


def location_list(request, city):
    locations = Hospital.objects.filter(city=city)
    location_dict = {}
    for hospital in locations:
        if hospital.location not in location_dict:
            location_dict[hospital.location] = hospital.id
    return render(request, 'location_list.html', {'location_dict': location_dict, 'city': city})



def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, 'hospital_detail.html', {'hospital': hospital})






