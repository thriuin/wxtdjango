from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .models import ATI, Department
from .searchform import SearchForm

# Create your views here.


def show_atis(request):
    """
    Show the ATI search result template
    :param request: HTTP Request object
    :return: ATI search page
    """
    ati = ATI.objects.all()
    context = {
        'atis': ati
    }
    return render(request, "list.html", context)


def show_page(request):
    return render(request, 'content-en.html')


def show_search(request):
    if request.method == 'POST':
        # process the submitted form
        form = SearchForm(request.POST)
        if form.is_valid():
            search_terms = form.cleaned_data['searchtext']
            return redirect('home-en')
    else:
        form = SearchForm
    context = {
        'form': form
    }
    return render(request, 'search-en.html', context)


class DepartmentList(View):
    def get(self, request):
        depts = Department.objects.all()

        context = {
            'depts': depts,
        }

        return render(request, "departments.html", context)
