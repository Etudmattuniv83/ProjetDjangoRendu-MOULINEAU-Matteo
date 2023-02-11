from django.views.generic import ListView

from recipes.models.tag import Tag


class TagListView(ListView):
    template_name = 'tag_list_view.html'
    model = Tag
