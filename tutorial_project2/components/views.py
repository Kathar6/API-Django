from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import ListView, DetailView, View
from .models import Component, ComponentCategory


# Category view
class ComponentCategoryListView(ListView):
    template_name = 'components/category.html'
    context_object_name = 'categories'

    # Set a query in the models
    def get_queryset(self, *args, **kwargs):
        return ComponentCategory.objects.all()


# Components with a category view, 
class ComponentListView(ListView):
    template_name = 'components/components.html'

    # Set a query in the models
    def get_queryset(self):
        return Component.objects.filter(category_id=int(self.kwargs['category']))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['components'] = self.get_queryset()
        context['category'] = self.kwargs['category']
        return context


# View of details to a specific component
class ComponentDetailView(DetailView):
    model = Component
    template_name = 'components/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["category"] = self.kwargs['category']
        return context
    

# View for buy a component, obtain the id of the component and substracts the number of stock
class BuyComponentView(View):
    def post(self, request, **kwargs):
        info_message = 'An error has ocurred'
        if 'pk' in self.kwargs:
            info_message = 'The purchase has been made successfully.'
            current_component = self.kwargs['pk']
            new_stock = Component.objects.get(id=current_component).stock - 1
            # Component.objects.filter(id=current_component).update(stock=new_stock)
        return HttpResponseRedirect(reverse('components:component_category'))
