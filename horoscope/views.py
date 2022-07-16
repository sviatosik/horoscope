from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass


def index(request):
    zodiaks = list(zodiak_dickt)
    # li_element += f"<li> <a href='{ridirect_path}'> {sign.title()}</a></li>"
    context = {
        'zodiaks': zodiaks,
        'zodiak_dickt': zodiak_dickt
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign(request, sign_zodiak: str):
    zodiaks = list(zodiak_dickt)
    description = zodiak_dickt.get(sign_zodiak)
    data = {
        'description_zodisk': description,
        'description_title': sign_zodiak,
        'zodiaks': zodiaks,
    }
    return render(request, 'horoscope/info_zodiak.html', context=data )



def get_info_about_sign_by_number(request, sign_zodiak: int):
    zodiaks = list(zodiak_dickt)
    if sign_zodiak > len(zodiaks):
        return HttpResponse(f'WRONG NUMBER {sign_zodiak}')
    name_zodiak = zodiaks[sign_zodiak - 1]
    riderect_url = reverse('horoscope-name', args=[name_zodiak])
    return HttpResponseRedirect(riderect_url)


zodiak_dickt = {
    'leo': 'leo baby',
    'aqua': 'good fish',
    'teron': 'not good',
    'gemini': 'very very very bed',
    'tonga': 'next please',
    'libra': 'what are you doing please'
}

types_dickt = {
    'earth': ['leo', 'teron'],
    'water': ['aqua', 'gemini'],
    'air': ['libra', 'tonga']
}


def type(request):
    list_types = list(types_dickt)
    li_elem = ''
    for typ in list_types:
        li_elem += f"<li><a href='{typ}'>{typ.title()}</a></li>"
    responce = f"""<ul>{li_elem}</ul>"""
    return HttpResponse(responce)


def type2(request, element):
    exito = ''
    for elem in types_dickt:
        if element == elem:
            out = types_dickt.get(elem)
            for i in out:
                ridirect_path = reverse('horoscope-name', args=[i])
                exito += f"<li><a href='{ridirect_path}'>{i}</a></li>"
    response = f"""<ul>{exito}</ul>"""
    return HttpResponse(response)
