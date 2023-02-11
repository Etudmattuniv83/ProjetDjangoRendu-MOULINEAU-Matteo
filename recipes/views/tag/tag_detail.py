from django.views.generic import DetailView

from recipes.models.tag import Tag


class TagDetailView(DetailView):
    template_name = 'tag_detail_view.html'
    model = Tag
