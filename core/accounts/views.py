from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
import requests
from .tasks import sendEmail


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h2>Done sending email</h2>")


@cache_page(240)
def test(request):
    response = requests.get(
        "https://2eb52b7a-5508-4ca8-9084-50fc89db120b.mock.pstmn.io/test/delay/5"
    )
    return JsonResponse(response.json())
