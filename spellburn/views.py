from random import randint, choice

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView

from .models import Character
from .forms import CharacterCreationForm, RollSpellForm, ChooseOriginForm


from .roll import roll_stats, roll_spell_func

from .backgrounds import backgrounds
from .random_names import random_names
from .archetypes import (
    archetypes,
    origins,
    abilities_dict,
    triggers_dict,
    starting_gear_dict,
)

from .equipment import ARMOR, WEAPONS, GEAR_TOOLS
from .scars import scars
from .mishaps import mishaps
from .spells import spells, spell_names, spell_dict


@login_required
def create_character(request):
    if request.method == "POST":
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            # création du personnage proprement dit
            character = Character()
            character.archetype = CharacterCreationForm.archetype_choices[
                int(form.cleaned_data["archetype"]) - 1
            ][1]

            if character.archetype == "Random":
                character.archetype = choice(archetypes)

            character.name = form.cleaned_data["name"] or choice(
                random_names.get(character.archetype)
            )

            character.user = request.user

            character.hp = randint(1, 6)
            background, bg_gear = choice(backgrounds.get(character.hp))
            character.background = background

            character.gear = [
                bg_gear,
                "Three days’ Rations",
                "A Torch",
            ] + starting_gear_dict.get(character.archetype)
            prioritize_body = form.cleaned_data["prioritize_body"]
            body, mind, luck = roll_stats(prioritize_body=prioritize_body)
            character.body = body
            character.mind = mind
            character.luck = luck
            character.gold = 10
            # save the char
            character.save()

            # redirect to my characters or character detail
            # add a success message before
            messages.success(
                request,
                f"{character.name}, the {character.archetype} created. Now choose an origin.",
            )
            return HttpResponseRedirect(
                reverse("characters:choose_origin", args=[character.pk])
            )
    else:
        # build context with empty form
        context = {"form": CharacterCreationForm()}

    return render(request, "characters/create_character.html", context)


@login_required
def choose_origin_view(request, pk):
    character = Character.objects.get(pk=pk)
    # check if character.user and request.user match
    if character.user == request.user:
        # if we're in the POST method case
        if request.method == "POST":
            # create the filled form, with archetype to manage the prompt and the choices
            form = ChooseOriginForm(character.archetype, request.POST)

            if form.is_valid():
                origin_prompt = origins.get(character.archetype).get("prompt")
                # offset by 1 because the choices enumerate starting from 1 instead of 0
                choice_made = int(form.cleaned_data["origin"]) - 1
                origin_text = origins.get(character.archetype).get("choices")[
                    choice_made
                ][1]
                character.origin = f"<b>{origin_prompt}</b><br>{origin_text}"

                # add the chosen ability
                choice_made = int(form.cleaned_data.get("ability"))
                character.abilities = [int(choice_made)]

                character.save()
                messages.success(
                    request, f"Welcome, {character.name} the {character.archetype}."
                )
                return HttpResponseRedirect(reverse("characters:my_characters"))
            else:
                messages.warning(request, "invalid form?")
                return HttpResponseRedirect(reverse("characters:my_characters"))
        else:
            # build context with empty form with archetype to manage the prompt and the choices
            context = {"form": ChooseOriginForm(archetype=character.archetype)}
            return render(request, "characters/choose_origin.html", context)
    else:
        messages.warning(request, "This character is not yours")
        return HttpResponseRedirect(reverse("characters:my_characters"))


class my_characters(LoginRequiredMixin, ListView):
    model = Character
    # paginate_by = 10  # if pagination is desired
    template_name = "characters/my_characters.html"
    context_object_name = "characters"

    # redirect_field_name = "personnages/mes_personnages"

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)


class character_detail(LoginRequiredMixin, DetailView):
    model = Character
    template_name = "characters/character_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archetype = context.get("character").archetype
        context.get("character").abilities = eval(context.get("character").abilities)
        context["triggers"] = triggers_dict.get(archetype)
        context["abilities"] = [ab[1] for ab in abilities_dict.get(archetype)]
        context["rows"] = list(range(5))
        inventory = eval(context.get("character").gear)
        empty_slots = ["" for _ in range(10 - len(inventory))]
        context["inventory"] = inventory + empty_slots
        return context


@login_required
def delete_character(request, pk):
    character = Character.objects.get(pk=pk)
    # check if character.user and request.user match
    if character.user == request.user:
        name = character.name
        character.delete()
        messages.success(request, f"Rest in peace, {name}.")
    else:
        messages.warning(request, "This characters is not yours.")

    return HttpResponseRedirect(reverse("characters:my_characters"))


class Scars(TemplateView):
    template_name = "characters/scars.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["scars"] = scars
        return context


class Mishaps(TemplateView):
    template_name = "characters/mishaps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mishaps"] = mishaps
        return context


class Spells(TemplateView):
    template_name = "characters/spells.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spells"] = spells
        return context


class Equipment(TemplateView):
    template_name = "characters/equipment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["armor"] = ARMOR
        context["weapons"] = WEAPONS
        context["tools"] = GEAR_TOOLS
        return context


def roll_spell_view(request):
    if request.method == "POST":
        form = RollSpellForm(request.POST)

        if form.is_valid():
            power = form.cleaned_data.get("power")
            spell_chosen = int(form.cleaned_data.get("spell"))

            spell_name = spell_names[spell_chosen]
            spell_effect = spell_dict[spell_name]

            DICE_LIST, SUM, DICE, FATIGUE, MISHAP = roll_spell_func(power)
            context = {
                "form": form,
                "SUM": SUM,
                "DICE_LIST": DICE_LIST,
                "DICE": DICE,
                "FATIGUE": FATIGUE,
                "MISHAP": MISHAP,
                "spell_name": spell_name,
                "spell_effect": spell_effect,
            }
            return render(request, "characters/roll_spell.html", context)
        # if a GET (or any other method) we'll create a blank form
    else:
        context = {"form": RollSpellForm()}
    return render(request, "characters/roll_spell.html", context)
