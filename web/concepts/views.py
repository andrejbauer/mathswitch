from concepts.models import Concept, Item
from django.shortcuts import get_object_or_404, redirect, render


def concept(request, name):
    concept = get_object_or_404(Concept, name=name)
    context = {
        "concept": {
            "name": concept.name,
            "description": concept.description,
            "items": [
                item.to_dict() for item in Item.objects.filter(concept=concept.id)
            ],
        }
    }
    return render(request, "detail.html", context)


def home(request):
    autocomplete_concepts = [c.name for c in Concept.objects.all()]
    context = {"concepts": autocomplete_concepts}
    return render(request, "index.html", context)


def search(request):
    search_value = request.GET.get("q")
    return redirect("/concept/" + search_value)
