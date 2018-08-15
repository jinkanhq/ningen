from django.db.models import Count
from django.db.models.functions import TruncYear
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from ningen.interview.models import Interview, Item, Tag


def about(request):
    """「关于」页面"""
    return render(request, 'about.html')


class InterviewDetail(DetailView):
    """采访详情页"""
    model = Interview


class InterviewList(ListView):
    """采访列表，默认作为「首页」"""
    model = Interview
    paginate_by = 5
    queryset = Interview.objects.all().order_by('-create_on')
    template_name = 'interview/interview_index.html'


def archives(request):
    """「采访」页面"""
    years = Interview.objects.annotate(year=TruncYear('create_on')) \
        .values('year').annotate(count=Count('id'))
    total_count = Interview.objects.count()
    tags = Tag.objects.all()
    item_count = Item.objects.count()
    return render(
        request, 'interview/interview_archives.html',
        {'years': years, 'total_count': total_count, 'tags': tags,
         'item_count': item_count})


class InterviewYearList(InterviewList):
    """年份采访列表"""
    template_name = 'interview/interview_year_list.html'

    def get_queryset(self):
        year = self.kwargs.get('year')
        return Interview.objects.filter(
            create_on__year=year).order_by('-create_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        return context


class InterviewTagList(InterviewList):
    """分类采访列表"""
    template_name = 'interview/interview_tag_list.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get('slug')
        return Interview.objects.filter(
            tags__slug=tag_slug).order_by('-create_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_slug'] = self.kwargs.get('slug')
        return context
