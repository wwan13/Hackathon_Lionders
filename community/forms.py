from django import forms
from .models import Community
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CommunityForm(forms.ModelForm):
    # title = forms.CharField(label='제목', max_length=100)
    # content = forms.CharField(label='', widget = CKEditorWidget())

    class Meta:
        model = Community
        fields = ['title', 'content',]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목을 입력하세요.',
                }
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = ""

        # self.fields['title'].widget.attrs.update({
        #     'class': '',
        # })

        self.fields['content'].widget.attrs.update({
            # 'class': '클래스명',
        })

# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('content', )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['content'].label = ""

#         self.fields['content'].widget.attrs.update({
#             # 'class': '클래스명',
#         })