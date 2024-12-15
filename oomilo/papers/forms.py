from .models import Paper, Tag
from bootstrap_modal_forms.forms import BSModalModelForm

class PaperModelForm(BSModalModelForm):
    class Meta:
        model = Paper
        fields = ['name', 'url', 'category', 'notes']