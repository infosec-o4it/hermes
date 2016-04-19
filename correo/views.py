# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from six import b
import triplesec
import base64


def cifrar(texto, clave):
    texto = triplesec.encrypt(b(texto).encode('utf8'), b(clave).encode('utf8'))
    return base64.b64encode(texto)


def decifrar(texto, clave):
    texto = b(base64.b64decode(texto))
    clave = b(clave.encode('utf8'))
    mensaje = triplesec.decrypt(texto, clave)
    return mensaje


class cifrado(forms.Form):
    texto = forms.CharField(label="Paste the encrypted text to decrypt \n",
                            widget=forms.Textarea)
    clave = forms.CharField(label="Phone Key")


class descifrado(forms.Form):
    texto = forms.CharField(label="Paste the text to encrypt \n",
                            widget=forms.Textarea)
    clave = forms.CharField(label="Phone Key")


def index(request):
    if request.method == 'POST':
        form = cifrado(request.POST)
        if form.is_valid():
            textos = form.cleaned_data['texto']
            contra = form.cleaned_data['clave']
            try:
                dato = decifrar(textos, contra)
            except Exception as e:
                return render(request, 'correo/index.html',  {'form': form})
            return render(request,
                          'correo/index.html',
                          {
                              'form': form,
                              'datos': dir(request),
                              'dato': dato,
                          }
                          )
    else:
        form = cifrado()
    return render(request, 'correo/index.html',  {'form': form})


def hide(request):
    if request.method == 'POST':
        form = descifrado(request.POST)
        if form.is_valid():
            try:
                textos = form.cleaned_data['texto']
                contra = form.cleaned_data['clave']
                dato = cifrar(textos, contra)
            except Exception as e:
                return render(request, 'correo/index2.html',  {'form': form})

            return render(request,
                          'correo/index2.html',
                          {
                              'form': form,
                              'datos': dir(request),
                              'dato': dato,
                          }
                          )
    else:
        form = descifrado()
    return render(request, 'correo/index2.html',  {'form': form})
