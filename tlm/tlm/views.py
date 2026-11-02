from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse('<h1>Home</h1>')
    data = {"header": "Homepage", "message": "Welcome to My Site!"}
    return render(request, 'homepage.html', context=data)

def about(request):
   # return HttpResponse(f"""<h1>About</h1>
   #     <div> Company Name: {company_name}</div>
   #     <div> Company Phone: {company_phone}</div>
   # """)
    header = "About us"
    staff = ['John Nichols', 'John Rogers', 'Timothy Smith']
    director = {"name": "David Lee", "img": "/director.jpg"}
    address = ('20 W 34th St.', 'New Your', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', context=data)
    