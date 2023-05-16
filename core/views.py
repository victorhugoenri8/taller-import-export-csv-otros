import csv

from django.http import HttpResponse

from import_export import resources

from core.models import Letras


def export_csv(request):
    
    # Import-Export library
    author_resource = resources.modelresource_factory(model=Letras)()
    dataset = author_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'atachment; filename="author_library.csv"'
    return response



def import_csv(request):
   

    # Import-Export library

     with open("letrascsv.csv", "r") as csv_file:
        import tablib

        author_resource = resources.modelresource_factory(model=Letras)()
        dataset = tablib.Dataset().load(csv_file)
        result = author_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            author_resource.import_data(dataset, dry_run=False)
        return HttpResponse(
            "strst"
        )