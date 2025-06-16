from django.shortcuts import render
from project.models import menubaritems, childcell


def menubar(request):

    items = menubaritems.objects.all()
    childitems = childcell.objects.all()

    data = {
        "items": items,
        "childitems": childitems,
    }
    return render(request, "index.html", data)


# Create your views here.
