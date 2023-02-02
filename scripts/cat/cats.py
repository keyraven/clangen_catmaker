from __future__ import annotations
from random import choice, randint, sample
from typing import Dict, List, Any
import math
import os.path
import itertools
try:
    import ujson
except ImportError:
    import json as ujson

from .pelts import *
from .names import *
from .sprites import *
from .thoughts import *
from .appearance_utility import *
from scripts.conditions import Illness, Injury, PermanentCondition, get_amount_cat_for_one_medic, \
    medical_cats_condition_fulfilled
import bisect

from scripts.utility import *
from scripts.game_structure.game_essentials import *
from scripts.cat_relations.relationship import *
import scripts.game_structure.image_cache as image_cache
from scripts.event_class import Single_Event


class Cat():
    used_screen = screen
    traits = [
        'adventurous', 'altruistic', 'ambitious', 'bloodthirsty', 'bold',
        'calm', 'careful', 'charismatic', 'childish', 'cold', 'compassionate',
        'confident', 'daring', 'empathetic', 'faithful', 'fierce', 'insecure',
        'lonesome', 'loving', 'loyal', 'nervous', 'patient', 'playful',
        'responsible', 'righteous', 'shameless', 'sneaky', 'strange', 'strict',
        'thoughtful', 'troublesome', 'vengeful', 'wise'
    ]
    kit_traits = [
        'attention-seeker', 'bossy', 'bouncy', 'bullying', 'charming',
        'daring', 'daydreamer', 'impulsive', 'inquisitive', 'insecure',
        'nervous', 'noisy', 'polite', 'quiet', 'sweet', 'troublesome'
    ]
    personality_groups = {
        'Outgoing': ['adventurous', 'bold', 'charismatic', 'childish', 'confident', 'daring',
                        'playful', 'righteous', 'attention-seeker', 'bouncy', 'charming', 'noisy'],
        'Benevolent': ['altruistic', 'compassionate', 'empathetic', 'faithful', 'loving',
                        'patient', 'responsible', 'thoughtful', 'wise', 'inquisitive',
                        'polite', 'sweet'],
        'Abrasive': ['ambitious', 'bloodthirsty', 'cold', 'fierce', 'shameless', 'strict',
                        'troublesome', 'vengeful', 'bossy', 'bullying', 'impulsive'],
        'Reserved': ['calm', 'careful', 'insecure', 'lonesome', 'loyal', 'nervous', 'sneaky',
                        'strange', 'daydreamer', 'quiet'],
        }
    ages = [
        'kitten', 'adolescent', 'young adult', 'adult', 'senior adult',
        'elder', 'dead'
    ]
    age_moons = {
        'kitten': [0, 5],
        'adolescent': [6, 11],
        'young adult': [12, 47],
        'adult': [48, 95],
        'senior adult': [96, 119],
        'elder': [120, 300]
    }

    # This in is in reverse order: top of the list at the bottom
    rank_sort_order = [
        "kitten",
        "elder",
        "apprentice",
        "warrior",
        "mediator apprentice",
        "mediator",
        "medicine cat apprentice",
        "medicine cat",
        "deputy",
        "leader"
    ]

    gender_tags = {'female': 'F', 'male': 'M'}

    skills = [
        'good hunter', 'great hunter', 'fantastic hunter', 'smart',
        'very smart', 'extremely smart', 'good fighter', 'great fighter',
        'excellent fighter', 'good speaker', 'great speaker',
        'excellent speaker', 'strong connection to StarClan', 'good teacher',
        'great teacher', 'fantastic teacher'
    ]
    med_skills = [
        'good healer', 'great healer', 'fantastic healer', 'omen sight',
        'dream walker', 'strong connection to StarClan', 'lore keeper',
        'good teacher', 'great teacher', 'fantastic teacher', 'keen eye',
        'smart', 'very smart', 'extremely smart', 'good mediator',
        'great mediator', 'excellent mediator', 'clairvoyant', 'prophet'
    ]
    elder_skills = [
        'good storyteller', 'great storyteller', 'fantastic storyteller',
        'smart tactician', 'valuable tactician','valuable insight',
        'good mediator', 'great mediator', 'excellent mediator',
        'good teacher', 'great teacher', 'fantastic teacher',
        'strong connection to StarClan', 'smart', 'very smart', 'extremely smart',
        'good kitsitter', 'great kitsitter', 'excellent kitsitter', 'camp keeper', 'den builder',
    ]

    skill_groups = {
        'special': ['omen sight', 'dream walker', 'clairvoyant', 'prophet', 'lore keeper', 'keen eye'],
        'star': ['strong connection to StarClan'],
        'heal': ['good healer', 'great healer', 'fantastic healer'],
        'teach': ['good teacher', 'great teacher', 'fantastic teacher'],
        'mediate': ['good mediator', 'great mediator', 'excellent mediator'],
        'smart': ['smart', 'very smart', 'extremely smart'],
        'hunt': ['good hunter', 'great hunter', 'fantastic hunter'],
        'fight': ['good fighter', 'great fighter', 'excellent fighter'],
        'speak': ['good speaker', 'great speaker', 'excellent speaker'],
        'story': ['good storyteller', 'great storyteller', 'fantastic storyteller'],
        'tactician': ['smart tactician', 'valuable tactician', 'valuable insight'],
        'home': ['good kitsitter', 'great kitsitter', 'excellent kitsitter', 'camp keeper', 'den builder']
    }

    backstories = [
        'clanborn', 'halfclan1', 'halfclan2', 'outsider_roots1', 'outsider_roots2',
        'loner1', 'loner2', 'kittypet1', 'kittypet2', 'rogue1', 'rogue2', 'abandoned1',
        'abandoned2', 'abandoned3', 'medicine_cat', 'otherclan', 'otherclan2', 'ostracized_warrior', 'disgraced', 
        'retired_leader', 'refugee', 'tragedy_survivor', 'clan_founder', 'orphaned'
    ]
    all_cats: Dict[str, Cat] = {}  # ID: object
    outside_cats: Dict[str, Cat] = {}  # cats outside the clan
    id_iter = itertools.count()

    all_cats_list: List[Cat] = []

    grief_strings = {}

    def __init__(self,
                 prefix=None,
                 gender=None,
                 status="kitten",
                 backstory="clanborn",
                 parent1=None,
                 parent2=None,
                 pelt=None,
                 eye_colour=None,
                 suffix=None,
                 ID=None,
                 moons=None,
                 example=False,
                 faded=False, # Set this to True if you are loading a faded cat. This will prevent the cat from being added to the list
                 loading_cat=False #Set to true if you are loading a cat at start-up.
                 ):

        # Private attributes
        self._moons = None
        
        # Public attributes
        self.gender = gender
        self.status = status
        self.age = None
        self.skill = None
        self.trait = None
        self.parent1 = parent1
        self.parent2 = parent2
        self.pelt = pelt
        self.tint = None
        self.eye_colour = eye_colour
        self.eye_colour2 = None
        self.scars = []
        self.dead = False
        self.dead_for = 0  # moons
        self.genderalign = None
        self.tortiebase = None
        self.pattern = None
        self.tortiepattern = None
        self.tortiecolour = None
        self.white_patches = None
        self.accessory = None
        self.illnesses = {}
        self.injuries = {}
        self.permanent_condition = {}
        self.df = False
        self.paralyzed = False
        self.age_sprites = {
            "kitten": None,
            "adolescent": None,
            "young adult": None,
            "adult": None,
            "senior adult": None,
            "elder": None
        }

        self.opacity = 100

        # setting ID
        if ID is None:
            potential_id = str(next(Cat.id_iter))

            if game.clan:
                faded_cats = game.clan.faded_ids
            else:
                faded_cats = []

            while potential_id in self.all_cats or potential_id in faded_cats:
                potential_id = str(next(Cat.id_iter))
            self.ID = potential_id
        else:
            self.ID = ID

        # age and status
        if status is None and moons is None:
            self.age = choice(self.ages)
        elif moons is not None:
            self.moons = moons
            if moons > 300:
                # Out of range, always elder
                self.age = 'elder'
            else:
                # In range
                for key_age in self.age_moons.keys():
                    if moons in range(self.age_moons[key_age][0], self.age_moons[key_age][1]+1):
                        self.age = key_age
        else:
            if status in ['kitten', 'elder']:
                self.age = status
            elif status == 'apprentice':
                self.age = 'adolescent'
            elif status == 'medicine cat apprentice':
                self.age = 'adolescent'
            else:
                self.age = choice(['young adult', 'adult', 'adult', 'senior adult'])
            self.moons = random.randint(self.age_moons[self.age][0], self.age_moons[self.age][1])

        # personality trait and skill
        if self.trait is None:
            if self.status != 'kitten':
                self.trait = choice(self.traits)
            else:
                self.trait = choice(self.kit_traits)

        if self.trait in self.kit_traits and self.status != 'kitten':
            self.trait = choice(self.traits)

        if self.skill is None or self.skill == '???':
            if self.moons <= 11:
                self.skill = '???'
            elif self.status == 'warrior':
                self.skill = choice(self.skills)
            elif self.moons >= 120 and self.status != 'leader' and self.status != 'medicine cat':
                self.skill = choice(self.elder_skills)
            elif self.status == 'medicine cat':
                self.skill = choice(self.med_skills)
            else:
                self.skill = choice(self.skills)

        # backstory
        if self.backstory == None:
            if self.skill == 'formerly a loner':
                backstory = choice(['loner1', 'loner2', 'rogue1', 'rogue2'])
                self.backstory = backstory
            elif self.skill == 'formerly a kittypet':
                backstory = choice(['kittypet1', 'kittypet2'])
                self.backstory = backstory
            else:
                self.backstory = 'clanborn'
        else:
            self.backstory = self.backstory

        # sex
        if self.gender is None:
            self.gender = choice(["female", "male"])
        self.g_tag = self.gender_tags[self.gender]


        # APPEARANCE
        init_pelt(self)
        init_tint(self)
        init_sprite(self)
        init_scars(self)
        init_accessories(self)
        init_white_patches(self)
        init_eyes(self)
        init_pattern(self)


        # NAME
        if self.pelt is not None:
            self.name = Name(status,
                             prefix,
                             suffix,
                             self.pelt.colour,
                             self.eye_colour,
                             self.pelt.name,
                             self.tortiepattern)
        else:
            self.name = Name(status, prefix, suffix, eyes=self.eye_colour)

        # Sprite sizes
        self.sprite = None
        self.big_sprite = None
        self.large_sprite = None

        # SAVE CAT INTO ALL_CATS DICTIONARY IN CATS-CLASS
        self.all_cats[self.ID] = self

    def __repr__(self):
        return self.ID

    def describe_cat(self):
        """ Generates a string describing the cat's appearance and gender. Mainly used for generating
        the allegiances."""
        if self.genderalign == 'male' or self.genderalign == "transmasc" or self.genderalign == "trans male":
            sex = 'tom'
        elif self.genderalign == 'female' or self.genderalign == "transfem" or self.genderalign == "trans female":
            sex = 'she-cat'
        else:
            sex = 'cat'
        description = str(self.pelt.length).lower() + '-furred'
        description += ' ' + describe_color(self.pelt, self.tortiecolour, self.tortiepattern, self.white_patches) + ' ' + sex
        return description

    def describe_eyes(self):
        colour = str(self.eye_colour).lower()
        colour2 = str(self.eye_colour2).lower()

        if colour == 'palegreen':
            colour = 'pale green'
        elif colour == 'darkblue':
            colour = 'dark blue'
        elif colour == 'paleblue':
            colour = 'pale blue'
        elif colour == 'paleyellow':
            colour = 'pale yellow'
        elif colour == 'heatherblue':
            colour = 'heather blue'
        elif colour == 'blue2':
            colour = 'blue'
        elif colour == 'sunlitice':
            colour = 'sunlit ice'
        elif colour == 'greenyellow':
            colour = 'green-yellow'
        if self.eye_colour2 != None:
            if colour2 == 'palegreen':
                colour2 = 'pale green'
            if colour2 == 'darkblue':
                colour2 = 'dark blue'
            if colour2 == 'paleblue':
                colour2 = 'pale blue'
            if colour2 == 'paleyellow':
                colour2 = 'pale yellow'
            if colour2 == 'heatherblue':
                colour2 = 'heather blue'
            if colour2 == 'blue2':
                colour2 = 'blue'
            if colour2 == 'sunlitice':
                colour2 = 'sunlit ice'
            if colour2 == 'greenyellow':
                colour2 = 'green-yellow'
            colour = colour + ' and ' + colour2
        return colour

# ---------------------------------------------------------------------------- #
#                                  conditions                                  #
# ---------------------------------------------------------------------------- #
  
    def get_ill(self, name, event_triggered=False, lethal=True, severity='default'):
        """
        use to make a cat ill.
        name = name of the illness you want the cat to get
        event_triggered = make True to have this illness skip the illness_moonskip for 1 moon
        lethal = set True to leave the illness mortality rate at its default level.
                 set False to force the illness to have 0 mortality
        severity = leave 'default' to keep default severity, otherwise set to the desired severity
                   ('minor', 'major', 'severe')
        """
        if name not in ILLNESSES:
            print(f"WARNING: {name} is not in the illnesses collection.")
            return
        if name == 'kittencough' and self.status != 'kitten':
            return

        illness = ILLNESSES[name]
        mortality = illness["mortality"][self.age]
        med_mortality = illness["medicine_mortality"][self.age]
        if severity == 'default':
            illness_severity = illness["severity"]
        else:
            illness_severity = severity

        duration = illness['duration']
        med_duration = illness['medicine_duration']

        amount_per_med = get_amount_cat_for_one_medic(game.clan)

        if medical_cats_condition_fulfilled(Cat.all_cats.values(), amount_per_med):
            duration = med_duration
        duration += random.randrange(-1, 1)
        if duration == 0:
            duration = 1

        if game.clan.game_mode == "cruel season":
            if mortality != 0:
                mortality = int(mortality * 0.5)
                med_mortality = int(med_mortality * 0.5)

                # to prevent an illness gets no mortality, check and set it to 1 if needed
                if mortality == 0 or med_mortality == 0:
                    mortality = 1
                    med_mortality = 1
        if lethal is False:
            mortality = 0

        new_illness = Illness(
            name=name,
            severity=illness_severity,
            mortality=mortality,
            infectiousness=illness["infectiousness"],
            duration=duration,
            medicine_duration=illness["medicine_duration"],
            medicine_mortality=med_mortality,
            risks=illness["risks"],
            event_triggered=event_triggered
        )

        if new_illness.name not in self.illnesses:
            self.illnesses[new_illness.name] = {
                "severity": new_illness.severity,
                "mortality": new_illness.current_mortality,
                "infectiousness": new_illness.infectiousness,
                "duration": new_illness.duration,
                "moons_with": 1,
                "risks": new_illness.risks,
                "event_triggered": new_illness.new
            }


    def get_injured(self, name, event_triggered=False, lethal=True):
        if name not in INJURIES:
            if name not in INJURIES:
                print(f"WARNING: {name} is not in the injuries collection.")
            return

        if name == 'mangled tail' and 'NOTAIL' in self.scars:
            return
        if name == 'torn ear' and 'NOEAR' in self.scars:
            return

        injury = INJURIES[name]
        mortality = injury["mortality"][self.age]
        duration = injury['duration']
        med_duration = injury['medicine_duration']

        amount_per_med = get_amount_cat_for_one_medic(game.clan)

        if medical_cats_condition_fulfilled(Cat.all_cats.values(), amount_per_med):
            duration = med_duration
        duration += random.randrange(-1, 1)
        if duration == 0:
            duration = 1

        if mortality != 0:
            if game.clan.game_mode == "cruel season":
                mortality = int(mortality * 0.5)

                if mortality == 0:
                    mortality = 1
        if lethal is False:
            mortality = 0

        new_injury = Injury(
            name=name,
            severity=injury["severity"],
            duration=injury["duration"],
            medicine_duration=duration,
            mortality=mortality,
            risks=injury["risks"],
            illness_infectiousness=injury["illness_infectiousness"],
            also_got=injury["also_got"],
            cause_permanent=injury["cause_permanent"],
            event_triggered=event_triggered
        )

        if new_injury.name not in self.injuries:
            self.injuries[new_injury.name] = {
                "severity": new_injury.severity,
                "mortality": new_injury.current_mortality,
                "duration": new_injury.duration,
                "moons_with": 1,
                "illness_infectiousness": new_injury.illness_infectiousness,
                "risks": new_injury.risks,
                "complication": None,
                "cause_permanent": new_injury.cause_permanent,
                "event_triggered": new_injury.new
            }

        if len(new_injury.also_got) > 0 and not int(random.random() * 5):
            avoided = False
            if 'blood loss' in new_injury.also_got and len(get_med_cats(Cat)) != 0:
                clan_herbs = set()
                needed_herbs = {"horsetail", "raspberry", "marigold", "cobwebs"}
                clan_herbs.update(game.clan.herbs.keys())
                herb_set = needed_herbs.intersection(clan_herbs)
                usable_herbs = []
                usable_herbs.extend(herb_set)

                if usable_herbs:
                    # deplete the herb
                    herb_used = random.choice(usable_herbs)
                    game.clan.herbs[herb_used] -= 1
                    if game.clan.herbs[herb_used] <= 0:
                        game.clan.herbs.pop(herb_used)
                    avoided = True
                    text = f"{str(herb_used).capitalize()} was used to stop blood loss for {self.name}."
                    game.herb_events_list.append(text)

            if not avoided:
                self.also_got = True
                additional_injury = choice(new_injury.also_got)
                if additional_injury in INJURIES:
                    self.additional_injury(additional_injury)
                else:
                    self.get_ill(additional_injury, event_triggered=True)
        else:
            self.also_got = False

    def congenital_condition(self, cat):
        possible_conditions = []

        for condition in PERMANENT:
            possible = PERMANENT[condition]
            if possible["congenital"] in ['always', 'sometimes']:
                possible_conditions.append(condition)

        new_condition = choice(possible_conditions)

        if new_condition == "born without a leg":
            cat.scars.append('NOPAW')
        elif new_condition == "born without a tail":
            cat.scars.append('NOTAIL')

        self.get_permanent_condition(new_condition, born_with=True)

    def get_permanent_condition(self, name, born_with=False, event_triggered=False):
        if name not in PERMANENT:
            print(f"WARNING: {name} is not in the permanent conditions collection.")
            return

        # remove accessories if need be
        if 'NOTAIL' in self.scars and self.accessory in ['RED FEATHERS', 'BLUE FEATHERS', 'JAY FEATHERS']:
            self.accessory = None
        if 'HALFTAIL' in self.scars and self.accessory in ['RED FEATHERS', 'BLUE FEATHERS', 'JAY FEATHERS']:
            self.accessory = None

        condition = PERMANENT[name]
        new_condition = False
        mortality = condition["mortality"][self.age]
        if mortality != 0:
            if game.clan.game_mode == "cruel season":
                mortality = int(mortality * 0.65)

        if condition['congenital'] == 'always':
            born_with = True
        moons_until = condition["moons_until"]
        if born_with is True and moons_until != 0:
            moons_until = randint(moons_until - 1, moons_until + 1)  # creating a range in which a condition can present
            if moons_until < 0:
                moons_until = 0
        elif born_with is False:
            moons_until = 0

        new_perm_condition = PermanentCondition(
            name=name,
            severity=condition["severity"],
            congenital=condition["congenital"],
            moons_until=moons_until,
            mortality=mortality,
            risks=condition["risks"],
            illness_infectiousness=condition["illness_infectiousness"],
            event_triggered=event_triggered
        )

        if new_perm_condition.name not in self.permanent_condition:
            self.permanent_condition[new_perm_condition.name] = {
                "severity": new_perm_condition.severity,
                "born_with": born_with,
                "moons_until": new_perm_condition.moons_until,
                "moons_with": 1,
                "mortality": new_perm_condition.current_mortality,
                "illness_infectiousness": new_perm_condition.illness_infectiousness,
                "risks": new_perm_condition.risks,
                "complication": None,
                "event_triggered": new_perm_condition.new
            }
            new_condition = True

        return new_condition


    def additional_injury(self, injury):
        self.get_injured(injury, event_triggered=True)

    def is_ill(self):
        is_ill = True
        if len(self.illnesses) <= 0:
            is_ill = False
        return is_ill is not False

    def is_injured(self):
        is_injured = True
        if len(self.injuries) <= 0:
            is_injured = False
        return is_injured is not False

    def is_disabled(self):
        is_disabled = True
        if len(self.permanent_condition) <= 0:
            is_disabled = False
        return is_disabled is not False

    def save_condition(self):
        # save conditions for each cat
        clanname = None
        if game.switches['clan_name'] != '':
            clanname = game.switches['clan_name']
        elif len(game.switches['clan_name']) > 0:
            clanname = game.switches['clan_list'][0]
        elif game.clan is not None:
            clanname = game.clan.name

        condition_directory = 'saves/' + clanname + '/conditions'
        condition_file_path = condition_directory + '/' + self.ID + '_conditions.json'

        if not os.path.exists(condition_directory):
            os.makedirs(condition_directory)

        if (not self.is_ill() and not self.is_injured() and not self.is_disabled()) or self.dead or self.outside:
            if os.path.exists(condition_file_path):
                os.remove(condition_file_path)
            return

        conditions = {}

        if self.is_ill():
            conditions["illnesses"] = self.illnesses

        if self.is_injured():
            conditions["injuries"] = self.injuries

        if self.is_disabled():
            conditions["permanent conditions"] = self.permanent_condition

        try:
            with open(condition_file_path, 'w') as rel_file:
                json_string = ujson.dumps(conditions, indent=4)
                rel_file.write(json_string)
        except:
            print(f"WARNING: Saving conditions of cat #{self} didn't work.")

    def load_conditions(self):
        if game.switches['clan_name'] != '':
            clanname = game.switches['clan_name']
        else:
            clanname = game.switches['clan_list'][0]

        condition_directory = 'saves/' + clanname + '/conditions/'
        condition_cat_directory = condition_directory + self.ID + '_conditions.json'
        if not os.path.exists(condition_cat_directory):
            return

        try:
            with open(condition_cat_directory, 'r') as read_file:
                rel_data = ujson.loads(read_file.read())
                if "illnesses" in rel_data:
                    self.illnesses = rel_data.get("illnesses")
                if "injuries" in rel_data:
                    self.injuries = rel_data.get("injuries")
                if "permanent conditions" in rel_data:
                    self.permanent_condition = rel_data.get("permanent conditions")

        except Exception as e:
            print(f"WARNING: There was an error reading the condition file of cat #{self}.\n", e)


    @property
    def moons(self):
        return self._moons

    @moons.setter
    def moons(self, value: int):
        self._moons = value

        updated_age = False
        for key_age in self.age_moons.keys():
            if self._moons in range(self.age_moons[key_age][0], self.age_moons[key_age][1]+1):
                updated_age = True
                self.age = key_age
        if not updated_age and self.age is not None:
            self.age = "elder"


# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #

# CAT CLASS ITEMS
cat_class = Cat(example=True)
game.cat_class = cat_class

# ---------------------------------------------------------------------------- #
#                                load json files                               #
# ---------------------------------------------------------------------------- #

resource_directory = "resources/dicts/conditions/"

ILLNESSES = None
with open(f"{resource_directory}illnesses.json", 'r') as read_file:
    ILLNESSES = ujson.loads(read_file.read())

INJURIES = None
with open(f"{resource_directory}injuries.json", 'r') as read_file:
    INJURIES = ujson.loads(read_file.read())

PERMANENT = None
with open(f"{resource_directory}permanent_conditions.json", 'r') as read_file:
    PERMANENT = ujson.loads(read_file.read())

resource_directory = "resources/dicts/events/death/death_reactions/"

GRIEF_GENERAL_POSITIVE = None
with open(f"{resource_directory}general_positive.json", 'r') as read_file:
    GRIEF_GENERAL_POSITIVE = ujson.loads(read_file.read())

GRIEF_GENERAL_NEGATIVE = None
with open(f"{resource_directory}general_negative.json", 'r') as read_file:
    GRIEF_GENERAL_NEGATIVE = ujson.loads(read_file.read())

GRIEF_FAMILY_POSITIVE = None
with open(f"{resource_directory}family_positive.json", 'r') as read_file:
    GRIEF_FAMILY_POSITIVE = ujson.loads(read_file.read())

GRIEF_FAMILY_NEGATIVE = None
with open(f"{resource_directory}family_negative.json", 'r') as read_file:
    GRIEF_FAMILY_NEGATIVE = ujson.loads(read_file.read())
