from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from typing import Any, Dict
from .coinmarketcap import CoinMarketCap


class HomePageView(TemplateView):
    template_name = "coins/list.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(HomePageView, self).get_context_data(**kwargs)
        cmc = CoinMarketCap()
        context["coins"] = cmc.get_latest_coins()
        return context