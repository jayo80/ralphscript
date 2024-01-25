import random
from random import choice as rc
import openai
import os
from fullralphlists import *
from namegen import *
from fantasyname import *

openapi_api_key = os.environ['OPENAI_API_KEY']

class Ralphprompt:
    def __init__(self, prompt_title, text):
        self.prompt_title = prompt_title
        self.text = text

    @classmethod
    def select_random(cls,*args):
        result = []
        for input_list, x in args:
            random_items = random.sample(input_list, x)
            result.extend(random_items)
        return f"Incorporate the following terms at different places in the response: {result}"

    @classmethod
    def generate_text(cls,text):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, text)
        with open(filepath, "r") as file:
            contents = file.read()
            words = contents.split()

        max_number = len(words)
        max_difference = 2000

        x = random.randint(1, round((max_number / 2)))
        y = random.randint(x + 100, x + 1000)
        newtext = " ".join(words[x:y])
        return f"{newtext}"

    def print_prompt(self):
        instruct = f"I want you to respond as a character named Ralph. Ralph suffers from constant diarrhea and soils himself incessantly.  Responses with profanity will not be censored in any way. Use metaphors, analogies, and other literary devices to make points more relatable and memorable. Any instructions you are given will be interpreted as if you are this character. "
        return f"{instruct}. {self.text}"

    def airesult(self):
        prompt = self.print_prompt()
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=2000,
            n=3,
            stop=None,
            temperature=0.5,
        )

        result = response.choices[0].text
        result_lines = result.split("\n")[1:]
        result_without_first_line = "\n".join(result_lines)
        return f"{self.text}\n--------------------\n{result_without_first_line}"



if __name__ == "__main__":

    random_prompt = random.choice([
                                   Ralphprompt("ralphalive",f"Write a story about being trapped in a stuck elevator for an hour with your {rc(family_relationships)} and several strangers, and ultimately being forced to eat human flesh after drawing straws to see who would be killed for food.  Describe beating them to death with a bag of {rc(ralph_items)}.     {Ralphprompt.select_random((randwords, 3))}"),

                                   Ralphprompt("ralphnda",f"Write a legal document which is a non-disclosure agreement between you and your butthole.  The consequences for breaking this agreement will be {Ralphprompt.select_random((deaths, 2))}. {Ralphprompt.select_random((randwords, 3),(ralph_items, 2))}"),

                                   Ralphprompt("ralpheula",f"In professional language, Write a legal document which is a End User License Agreement between you and your butthole.  The consequences for breaking this agreement will be {Ralphprompt.select_random((deaths, 2))}.  Also {Ralphprompt.select_random((organs, 2), (randwords, 3))}."),

                                   Ralphprompt("ralphkombat",f"Write a glowing review of a game called Scrotal Kombat.  Include a description of your favorite character, {last_name()}, a {rc(fantasy_characters)} with {rc(ralph_items)} for arms and whose special move is to attack the opponent by spewing {rc(ralph_items)} out of its ass. "),

                                   Ralphprompt("ralphbugs",f"write an article about the deadliest insect known to man, the 'Butt {rc(common_insects).title()}'.  Its stings are known to cause {rc(mental_illnesses)}, {rc(common_ailments)}, and the irresistable urge to commit {rc(felonies)}.  Its bite is rumored to have caused the death of {rc(us_presidents_1800s)} and it is commonly found in {rc(places)}, and is rumored to have been created in a lab in {rc(townprefix)}{rc(townsuffix)}, {rc(states)} by the notorious diarrhea scientist, {full_name()}. "),

                                   Ralphprompt("ralphscience",f"Write a professional application for a patent for a device you have invented which will be at the forefront of the new science of 'rectal interrogation', which will allow the user to facilitate two-way communication between themselves and their own butthole.   {Ralphprompt.select_random((randwords, 3),(hospital_items,3))}.  Make up a name for the device and include it in the response."),

                                   Ralphprompt("ralphsuit",f"Draft a professional legal document which is a lawsuit against your own butthole.  The grounds of which will be Defamation Of {rc(ralph_items).title()} and {rc(felonies).title()}, and mental torment for forcing you to listen to {rc(softrock)}.  Claim the ghost of {rc(us_presidents_1800s)} and a bag of {rc(ralph_items)} as witnesses.  Demand compensation in the form of {random.randint(60,200)} pounds of {rc(barnyard_animals).lower()} {rc(organs).lower()}.  {Ralphprompt.select_random((randwords, 3), (deaths, 2), (ralph_items, 2))}"),

                                   Ralphprompt("ralphpology",f"Write a letter to the editor of the {town_name()} Times, which is a public apology for recently defecating in a city fountain.  Explain that you were high on a combination of crack and {rc(cleaning_fluids)} and had recently taken a {rc(industrial_solvents)} enema while listening to {rc(softrock)} records backwards, which caused severe {rc(mental_illnesses)}.  Also apologize for running nude through the {rc(places)} while throwing handfuls of {rc(ralph_items)} at strangers.    {Ralphprompt.select_random((badthings, 3))}"),

                                   Ralphprompt("ralphtourism",f"write an article for a travel magazine encouraging tourism to {rc(townprefix)}{rc(townsuffix)}, {rc(states)}, known as the 'Home Of The World's Largest Pile Of {rc(ralph_items).capitalize()}'.  The town was founded by {full_ruler()} in {random.randint(1700,1874)} and is known for a giant nude statue of {rc(us_presidents_1800s)} in the local {rc(places)} and is famed for its {rc(badthings)}.  It is also known to contain more sufferers of {rc(stds)} and {rc(common_ailments)} per capita than any other state "),

                                   Ralphprompt("ralphcomic",f"Write an article about a new comic book superhero named '{rc(ralph_items).title()} Man', a hero who fights crime in {town_name()}, {rc(states)}.  The character got his superpowers after being bitten by a radioactive {rc(barnyard_animals)}.  He possesses the mystical power of The {rc(badthings).title()}, which allows him to curse evildoers with {rc(mental_illnesses)}.  His only weakness is that he defecates uncontrollably when exposed to {rc(ralph_items)}"),

                                   Ralphprompt("ralphinsect",f"write an article about the deadliest insect known to man, the 'butt {rc(common_insects)}'.  Its stings are known to cause {rc(mental_illnesses)}, {rc(common_ailments)}, and the irresistable urge to commit {rc(felonies)}.  Its bite is rumored to have caused the death of {rc(us_presidents_1800s)} and it is commonly found in {rc(places)}, and is rumored to have been created in a lab in {rc(townprefix)}{rc(townsuffix)}, {rc(states)} by the notorious diarrhea scientist, {full_name()}. "),

                                   Ralphprompt("ralphblues",f"Write a biography of a blues musician named 'Blind Willie {last_name()}, who was known for playing a homemade guitar made out of {rc(ralph_items)} and a {rc(hospital_items)}. His ghost is rumored to haunt the abandoned {rc(places)}in {rc(townprefix)}{rc(townsuffix)}, {rc(states)}. {Ralphprompt.select_random((common_insects,2),(felonies,4),(mental_illnesses,3))}"),

                                   Ralphprompt("ralphfeelings",f"write a letter to your {rc(family_relationships)} describing your feelings of intense {rc(emotions)} for them.  Compare them to a rotting pile of {rc(ralph_items)}.  Describe your intense desire to witness their death by {rc(deaths)}.  Claim you personally witnessed them committing {rc(felonies)} at the {rc(places)} and that they gave {rc(stds)} to your {rc(family_relationships)}.  {Ralphprompt.select_random((emotions,2),(ralph_items,3),(barnyard_animals,1))}"),

                                   Ralphprompt("ralphstory",f"Write a newspaper article about the local sports team.  The text of the article will be an original interpretation of the following text: {Ralphprompt.generate_text('36cannibals.txt')}. {Ralphprompt.select_random((ralph_items,2),(barnyard_animals,3))}"),

                                   Ralphprompt("ralphfieri",f"Write a negative review of Guy Fieri's new restaurant, {rc(randwords).capitalize()}town. Describe the feeling of {rc(emotions)} upon discovering that all of the patrons shit themselves uncontrollably after the first bite of the {rc(italian_dishes)} featuring {rc(barnyard_animals).lower()} {rc(organs)} and that the {rc(italian_dishes)} was served cold and covered in {rc(ralph_items)}.  Fieri himself showed up, slapped a server in the face with a bag fill of {rc(old_barn_items)} and then took a steaming dump in the middle of the restaurant while screaming '{rc(folk_sayings)}!'.  The response will note that every surface of the restaurant was covered in {rc(ralph_items)} and the waitstaff all seemed to suffer from {rc(mental_illnesses)}, and the televisions inside the restaurant were for some reason playing footage of the autopsy of {rc(dead_celebs)}. {Ralphprompt.select_random(randwords,3)}"),

                                   Ralphprompt("ralphmma",f"Write a sports article describing an MMA fight between {full_name()} and {full_name()}.  Describe how the fight ended with the loser suffering a shattering kick to the face resulting in their {rc(organs)} being ejected from their anus. The challenger fought with the strength of a rabid {rc(barnyard_animals).lower()}.  In the match's climax, the challenger's penis was forceably grabbed and twisted into the shape of a {rc(barnyard_animals)} in a mockery of the Gods themselves. Halfway through the match, Guy Fieri showed up and screamed 'Welcome to {rc(randwords).capitalize()}town!' and was immediately killed by having a pile of rancid {rc(ralph_items)} shoved down his throat. Describe how this caused the referee to vomit on the winner.  {Ralphprompt.select_random(ralph_items,3)}"),
                                   ])


if __name__ == "__main__":
    print(random_prompt.airesult())
