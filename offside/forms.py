# -*- coding: utf-8 -*-
from django import forms
from .models import Comment,CommentNews







class CommentModelForm(forms.ModelForm):
    RATING_CHOICES = [
        ('0', '0- Too Bad'),
        ('1', '1- Ehh'),
        ('2', '2- Normal'),
        ('3', '3 - Good'),
        ('4', '4 - Very Good'),
        ('5', '5 - Incredible'),
    ]
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter the title', 'class': 'input-text full-width'}))

    body = forms.CharField(label='Title',widget=forms.Textarea(attrs={'placeholder': 'Your Comment','class':'input-text full-width'}))
    rating = forms.CharField(label='Gradings ', widget=forms.Select(attrs={"class":"selector"},choices=RATING_CHOICES))

    class Meta:
        model= Comment
        fields = [
            # "user",
            "title",
            "body",
            "rating"

        ]


class CommentNewsForm(forms.ModelForm):
    RATING_CHOICES = [
        ('0', '0- Too Bad'),
        ('1', '1- Ehh'),
        ('2', '2- Normal'),
        ('3', '3 - Good'),
        ('4', '4 - Very Good'),
        ('5', '5 - Incredible'),
    ]
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter the title', 'class': 'input-text full-width'}))

    body = forms.CharField(label='Title',widget=forms.Textarea(attrs={'placeholder': 'Your Comment','class':'input-text full-width'}))
    rating = forms.CharField(label='Gradings ', widget=forms.Select(attrs={"class":"selector"},choices=RATING_CHOICES))

    class Meta:
        model= CommentNews
        fields = [
            # "user",
            "title",
            "body",
            "rating"

        ]