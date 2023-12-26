from django.http import JsonResponse

# Create your views here.
def sample_view(request):
    return JsonResponse({"message": "Hello, World!"})