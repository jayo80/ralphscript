import random
from random import choice as rc
import openai
import os
from fullralphlists import *
from namegen import *
from demontitle import *
from fantasyname import *
import nltk
import mysql.connector

openapi_api_key = os.environ['OPENAI_API_KEY']
db_pass = os.environ['PROMPT_DB_KEY']

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=db_pass,
    database="ralphprompts2"
)

mycursor = db.cursor()

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

    def readfile(file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dir_path, file_name)
        with open(filepath) as f:
            content = f.read()
            return content


    @classmethod
    def bandname(cls, textsource):
        number = random.randint(1, 250)
        source = cls.readfile(textsource)
        tokens = nltk.word_tokenize(source)
        pos_tags = nltk.pos_tag(tokens)
        adjectives = [word for word, pos in pos_tags if pos.startswith("JJ")]
        nouns = [word for word, pos in pos_tags if pos.startswith("NN")]
        if number % 2 == 0:
            x = f"The {random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()}"
        else:
            x = f"{random.choice(adjectives).capitalize()} {random.choice(nouns).capitalize()}"
        return x

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
        mycursor.execute("INSERT INTO prompts (name,prompt_text, prompt_result) VALUES (%s, %s, %s)", (self.prompt_title, self.text, result_without_first_line))
        db.commit()
        return f"{self.text}\n--------------------\n{result_without_first_line}"


prompt_list = [
                                Ralphprompt("ralphalive",f"Write a story about being trapped in a stuck elevator for an hour with your {rc(family_relationships)} and several strangers, and ultimately being forced to eat human flesh after drawing straws to see who would be killed for food.  Describe beating them to death with a bag of {rc(ralph_items)}.     {Ralphprompt.select_random((randwords, 3))}"),

                                Ralphprompt("ralphwar",f"Draft a professional government document declaring war against your own butthole.  As terms of the document {Ralphprompt.select_random((ralph_items, 3), (mental_illnesses, 3))}"),

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

                                Ralphprompt("ralphfieri",f"Write a negative review of Guy Fieri's new restaurant, {rc(randwords).capitalize()}town. Describe the feeling of {rc(emotions)} upon discovering that all of the patrons shit themselves uncontrollably after the first bite of the {rc(italian_dishes)} featuring {rc(barnyard_animals).lower()} {rc(organs)} and that the {rc(italian_dishes)} was served cold and covered in {rc(ralph_items)}.  Fieri himself showed up, slapped a server in the face with a bag fill of {rc(old_barn_items)} and then took a steaming dump in the middle of the restaurant while screaming '{rc(folk_sayings)}!'.  The response will note that every surface of the restaurant was covered in {rc(ralph_items)} and the waitstaff all seemed to suffer from {rc(mental_illnesses)}, and the televisions inside the restaurant were for some reason playing footage of the autopsy of {rc(dead_celebs)}. {Ralphprompt.select_random((randwords,3))}"),

                                Ralphprompt("ralphwar",f"Draft a professional government document declaring war against your own butthole.  As terms of the document {Ralphprompt.select_random((ralph_items, 3), (mental_illnesses, 3))}"),

                                Ralphprompt("ralphsaint",f"write a biography of St. {last_name()} of {rc(townprefix)}{rc(townsuffix)}, who, despite constantly defecating and bleeding from both eyes, was known to plant a jar of {rc(ralph_items)} in every town, which would miraculously sprout into a {rc(places)} overnight, and who singlehandly defeated the {rc(mythical_creatures)} of {rc(townprefix)}{rc(townsuffix)} with a {rc(medieval_weapons)} made of {rc(ralph_items)} "),

                                Ralphprompt("ralphmma",f"Write a sports article describing an MMA fight between {full_name()} and {full_name()}.  Describe how the fight ended with the loser suffering a shattering kick to the face resulting in their {rc(organs)} being ejected from their anus. The challenger fought with the strength of a rabid {rc(barnyard_animals).lower()}.  In the match's climax, the challenger's penis was forceably grabbed and twisted into the shape of a {rc(barnyard_animals)} in a mockery of the Gods themselves. Halfway through the match, Guy Fieri showed up and screamed 'Welcome to {rc(randwords).capitalize()}town!' and was immediately killed by having a pile of rancid {rc(ralph_items)} shoved down his throat. Describe how this caused the referee to vomit on the winner.  {Ralphprompt.select_random((ralph_items,3))}"),

                                Ralphprompt("ralphblog3",f"write a profanity-filled blog post about his experiments with {rc(cleaning_fluids)} enemas. He will also comment that it causes intense hallucinations about {rc(ralph_items)} Ralph will then note that he has soiled himself uncontrollably before signing off"),

                                Ralphprompt("ralphblog2",f"write an angry, letter filled with profanity to his {rc(family_relationships)} asking them to bail him out of jail.  He has been arrested for running naked through a {rc(places)}, high on crack and drinking from a large bottle of {rc(cleaning_fluids)}, claiming that he has been transformed into a sentient bag of {rc(ralph_items)} by the spirit of {rc(us_presidents_1800s)}.  During the entire ordeal, Ralph will note that he was defecating uncontrollably and striking people with a {rc(gardening_tools)}"),

                                Ralphprompt("ralphblog6",f"write a passionate letter to his {rc(family_relationships)} from a cave in Central Park.  Explain that he has chosen to live there because he had a vision of {rc(warnerbros)} riding through New York on a {rc(mythical_creatures)} and slaughtering the populace with a fiery {rc(gardening_tools)}.  Insist that this vision was foretold in the lyrics of {rapname()}.  Before signing off, mention that he has soiled himself and is painting pictures of {rc(us_presidents_1800s)} on the cave wall with his own feces"),

                                Ralphprompt("ralph4prez",f"write a lengthy blog post about his intention to run for President.  His slogan will be 'a bag of {rc(ralph_items)} in every home'.  His running mate will be {rc(warnerbros)} and he vows to violently purge the country of {rc(mythical_creatures)}. He intends to declare war on {rc(states)} and vows to blow up {rc(planets)}. He intends to pardon anyone convicted of {rc(felonies)} and {rc(felonies)} He will nominate the ghost of {us_presidents_1800s} as the secretary of state, and a rapper named {rapname()} will be nominated as Supreme Court Justice."),

                                Ralphprompt("ralphletter", f"Write a letter to {rc(family_relationships)} about the decision to change my name to {full_name()} and move into a port-o-potty. Also mention in detail that you are proud of your new {rc(common_insects)} collection and apologize for shitting in your {rc(family_relationships)}'s casket at their funeral while high on methamphetamine and {rc(cleaning_fluids)}.  The letter will conclude with a rambling, incoherent rant about his hatred of the music of {rc(softrock)}."),

                                Ralphprompt("ralphchild",f"Write a story about growing up in a port-o-potty as a {rc(ralph_items)} farmer in {rc(townprefix)}{rc(townsuffix)}, {rc(states)}.  Describe the beatings which were regularly administered by your {rc(family_relationships)} with a {rc(gardening_tools)} , and being left in the woods for days at a time with a with only a pet bag of {rc(ralph_items)} named {full_name()} for company.  {Ralphprompt.select_random((industrial_solvents,2),(old_barn_items,2),(ralph_items,3))}"),

                                Ralphprompt("ralphstory1",f"Ralph was recently discovered defecating in a urinal.  Ralph's father regularly beats prostitutes with his prosthetic leg and was just released from jail for illict acts with a bag of oysters.  Ralph's diarrhea is causing him to void his bowels constantly throughout the conversation. During the conversation, Ralph's father sets himself on fire. {Ralphprompt.select_random((randwords,3),(ralph_items,2))}"),

                                Ralphprompt("ralphraparticle",f"Write an article for a music magazine.  The title of the article will be {rapheadline()} {Ralphprompt.select_random((ralph_items,2), (randwords,3))}"),

                                Ralphprompt("ralphvisit",f"Describe a scenario in which Ralph is visiting a {rc(places)} with his {rc(family_relationships)}.  Ralph begins angrily berating them before knocking them down with a {rc(gardening_tools)} before releasing a stream of diarrhea into their face, all while claiming to be a {rc(fantasy_characters)} from {rc(planets)}.  He continues to defecate while screaming obscenities into the faces of passerby.  {Ralphprompt.select_random((ralph_items,2),(cleaning_fluids,2),(randwords,3))}.  "),

                                Ralphprompt("ralphfuture",f"describe a scenario in which Ralph is standing in a {rc(places)}, stark naked, constantly defecating, and gnawing on a live {rc(barnyard_animals)} as he pronounces a prediction of the future.  He claims that he gained the ability to predict the future after smoking a mixture of {rc(cleaning_fluids)} and ground {rc(common_insects)} feces while listening to {rc(softrock)} records backwards. The response will include a dire prophecy of future events and will involve the following subjects: {rc(felonies)}, {rc(tv_shows_1970s)}, {rc(ralph_items)}, fiery anuses, unrelenting diarrhea, {rc(softrock)}, A fiendish {rc(fantasy_characters)} known as the Father of {rc(old_barn_items)}, {rc(planets)}, and {rc(common_ailments)}" ),

                                Ralphprompt("ralphcamp",f"as Ralph, write a letter home from summer camp.  His roommate, {rapname()}, is obsessed with {rc(ralph_items)}, which makes Ralph feel {rc(emotions)}.  Describe in detail how he is being force-fed {rc(cleaning_items)} which exacerbates his chronic diarrhea.  Describe how the camp counselors forced them to build a giant statue of {rc(us_presidents_1800s)} out of {rc(ralph_items)}.  Describe in length how the campers are beaten and occasionally fed to a {rc(mythical_creatures)} which lives in the woods.  He is furious with his family for handcuffing him and forcing him to go to the camp.  "),

                                Ralphprompt("ralphtattoo",f"write a story in which Ralph is standing in the middle of a {rc(places)} and waving around a large plastic bottle full of {rc(ralph_items)}. He is also rambling constantly about how his anus is haunted by the ghost of {rc(us_presidents_1800s)}.  It is also important to note that the entire time, he is defecating constantly and blood is pouring from his eyes.  He is stark naked, revealing an enormous tattoo on his chest of {rc(warnerbros)} engaged in sexual intercourse with a {rc(mythical_creatures)}.  On his head he has fashioned a hat out of the carcass of a {rc(extinct)}.  The onlookers are {rc(emotions)}.  "),

                                Ralphprompt("ralphifesto",f"Write a letter to your {rc(family_relationships)} announcing that you are heretofore to be known as '{demon_name()}'.  Compose a manifesto which outlines your intent to colonize {rc(planets)} in a spaceship you are currently building out of {rc(cleaning_items)} and {rc(barnyard_animals)} flesh, and that you made this decision after smoking a mixture of crack and {rc(cleaning_fluids)}.  {Ralphprompt.select_random((deaths,2),(ralph_items,3),(randwords,4))}"),

                                Ralphprompt("ralphwwi",f"Write a term paper on the causes of World War I, {Ralphprompt.select_random((ralph_items, 2), (randwords, 3))}"),

                                Ralphprompt("ralphpoa",f"Draw up a legal document granting power of attorney to your own butthole.  {Ralphprompt.select_random((deaths,2),(ralph_items,3),(randwords,4))}")

                                ]


def print_single(pname):
    plist = []
    for prompt in prompt_list:
        plist.append(prompt.prompt_title)
        if pname == prompt.prompt_title:
            return prompt.airesult()
    return random.choice(prompt_list).airesult()

if __name__ == "__main__":
    print(print_single("rando"))


