from django.shortcuts import render,HttpResponse
from translate import Translator

from translator_app.models import TranslatorItem
# Create your views here.

def home(request):
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        new_item = TranslatorItem(content=text, language=language, translated_data=translation)
        new_item.save()

        return HttpResponse(translation)

    return render(request, "index.html")

def data(request):
    # all_data_items = TranslatorItem.objects.all()
    # print(all_data_items)
    try:
        all_data_items = TranslatorItem.objects.get(content='python')
        all_data_items.content='python1'
        all_data_items.save()
        all_data_items = TranslatorItem.objects.all()
        print(all_data_items)
    except Exception:
        all_data_items = TranslatorItem.objects.all()
    return render(request, "index1.html", {'all_items': all_data_items})
# CRUD -- Create Retreive update delete