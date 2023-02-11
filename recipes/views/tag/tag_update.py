from django.urls import reverse
from django.views.generic import UpdateView

from recipes.models.tag import Tag


class TagUpdateView(UpdateView):
    template_name = 'tag_update_view.html'
    model = Tag
    fields = ['text']

    def get_success_url(self):
        return reverse('tag_list')
