# this is going to assume that the user has a copy of Simple World;
# the only content directly from SW is the six lines of Move templates

import random

# giant list of keywords
keywords = [
"plague", "searching", "keeping", "stealing", "rose", "honor", "retrieve", "locate", "chase", "explore", "deliver", "hunt", "befriend", "persuade", "barter", "protect", "collect", "sleuth", "respite", "restore", "destroy", "prepare", "interrupt", "return", "protect", "passion", "redemption", "annhilate", "justice", "attack", "resist", "future", "agent", "secret", "revenge", "distance", "anger", "supply", "power", "desire", "choice", "phobia", "ice", "lust", "dirt", "machinery", "pride", "love", "betrayal", "honor", "duty", "mistake", "debt", "fire", "air", "death", "pain", "self", "history", "need", "flaw", "fear", "guilt", "purity", "vice", "artifice", "spy", "action", "romance", "war", "exploration", "fire", "air", "water", "earth", "stealth", "madness", "mobius", "time", "distance", "travel", "oration", "mind", "seduction", "deduction", "spirit", "fierce", "evolution",
]

# remove duplicates so we can be free with adding keywords
keywords = list(set(keywords))

# giant list of class-type roles; needs more options for sure
roles = [
    "Athletics",
    "Persuading",
    "Communication and Protocol",
    "Detection",
    "Driving, Riding and Piloting",
    "Gadgeteering"
    "The medical arts"
    "Wilderness Mastery"
    "Scholarship"
    "Intrusion"
    "Combat"
    "Magic and Weird"
    ]
   

# every role needs at least one specialty but more is better
specialties = {
    "running for your life" : ["Athletics", "Scholarship" ],
    "jumping despite risk" : ["Athletics", "Gadgeteering"],
    "climbing a dangerous route" : ["Athletics", "Wilderness Mastery"],
    "overpowering with strength" : ["Athletics", "Combat"],
    "lying to their face" : [ "Persuading", "Detection"],
    "seducing someone vulnerable": [ "Persuading", "Communication and Protocol"],
    "inspiring a crowd" : [ "Persuading", "Combat"],
    "enthralling a room"  : [ "Persuading", "Magic and Weird"],
    "calming a charged situation": ["Persuading", "The medical arts"],
    "leading a gang" : ["Persuading", "Athletics"],
    "relying on language alone" : ["Communication and Protocol", "Persuading"],
    "deciphering a secret"  : ["Communication and Protocol", "Intrusion"],
    "avoiding a breach of ettiquette" : ["Communication and Protocol", "Scholarship"],
    "recalling a cultural quirk" : ["Communication and Protocol", "Driving, Riding and Piloting"],
    "noticing a clue" : ["Detection", "Gadgeteering"],
    "recognizing a threat" : ["Detection", "Magic and Weird"],
    "understanding a detail" : ["Detection", "Scholarship"]  ,                     
    "chasing": ["Driving, Riding and Piloting", "Detection"],
    "eluding": ["Driving, Riding and Piloting", "Wilderness Mastery"],
    "handling tricky enviroments" : ["Driving, Riding and Piloting", "Athletics"],
    "needing to react quickly" : ["Driving, Riding and Piloting", "Combat"],
    "exploiting technology": ["Gadgeteering", "Magic and Weird"],
    "disabling a threat": ["Gadgeteering", "Intrusion"],
    "repairing equipment": ["Gadgeteering", "Driving, Riding and Piloting"],
    "deciphering jargon under pressure": ["Gadgeteering", "Scholarship"],
    "healing the injured": ["The medical arts", "Magic and Weird"],
    "saving a life": ["The medical arts", "Combat"],
    "diagnosing a threat": ["The medical arts", "Detection"],
    "surviving despite the odds": ["Wilderness Mastery"],
    "tracking or hunting": ["Wilderness Mastery", "Detection"],
    "taming dangerous beasts": ["Wilderness Mastery", "Driving, Riding and Piloting"],
    "using nature's gifts": ["Wilderness Mastery", "Magic and Weird"],
    "recalling useful knowledge": ["Scholarship", "Magic and Weird"],
    "piercing lies": ["Scholarship", "Detection"],
    "stealing": ["Intrusion", "Persuading"],
    "hiding from danger": ["Intrusion", "Wilderness Mastery"],
    "breaking through locks": ["Intrusion", "Gadgeteering"],
    "slipping by unnoticed": ["Intrusion", "Athletics"],
    "beating someone up" : ["Combat","Athletics"],
    "seizing objective by force" : ["Combat","Intrusion"],
    "delivering distant violence": ["Combat","Magic and Weird"],
    "bending reality": ["Magic and Weird", "Gadgeteering"],
    "channeling power": ["Magic and Weird", "The medical arts"],
    "changing a target": ["Magic and Weird", "Persuading"]
#"" : [],
}

def specilties_checker(d):
    # type in " specilties_checker(specialties) " at the command to check the specialites dictionary of lists above doesn't have broken links in
    # Iterate through and find out how many times each key occurs
    vals = {}                       # A dictonary to store how often each value occurs.
    for i in d.values():
      for j in set(i):              # Convert to a set to remove duplicates
        vals[j] = 1 + vals.get(j,0) # If we've seen this value iterate the count
                                    # Otherwise we get the default of 0 and iterate it
    print(vals)

    # Iterate through each possible freqency and find how many values have that count.
    counts = {}                     # A dictonary to store the final frequencies.
    # We will iterate from 0 (which is a valid count) to the maximum count
    for i in range(0,max(vals.values())+1):
        # Find all values that have the current frequency, count them
        #and add them to the frequency dictionary
        counts[i] = len([x for x in vals.values() if x == i])

    for key in sorted(counts.keys()):
      if counts[key] > 0:
         print (key,":",counts[key] )



premise = random.choice(keywords)

# number of playbooks
pcount = random.randint(3,6)

pbA = random.sample(roles, pcount)
pbB = random.sample(keywords, pcount)

playbooks = []
pbspecialties = []
for i in range(0, len(pbA)):
    subspecialties = []
    playbooks.append(pbB[i] + " " + pbA[i])
    for key,value in specialties.items():
        if pbA[i] in value:
            subspecialties.append(key)
    pbspecialties.append(subspecialties)

# and probably a core dichotomy, like honor vs discipline or something
cards = [
["Ace", "Hearts", "Fool", "Freedom", "Isolation"],
["2", "Hearts", "Messenger", "communication", "miscommunication",],
["3", "Hearts", "Spring", "Newness", "Corruption"],
["4", "Hearts", "Cross", "Belief", "Disbelief"],
["5", "Hearts", "Moon", "Enthusiasm", "Fickleness"],
["6", "Hearts", "Satyr", "Tolerance", "Indulgence"],
["7", "Hearts", "Crossroad", "choice", "restriction"],
["8", "Hearts", "Muse", "inspiration", "madness"],
["9", "Hearts", "Eros", "desire", "obsession"],
["10", "Hearts", "Feather", "hope", "despair"],
["Jack", "Hearts", "Lover", "love", "jilt"],
["Queen", "Hearts", "Priestess", "mysteries revealed", "reckless curiosity"],
["King", "Hearts", "Mentor", "sacrifice", "jealousy"],

["Ace", "Diamonds", "Tower", "Alliance", "Solitude"],
["2", "Diamonds", "Fox", "Cunning", "Cynicism"],
["3", "Diamonds", "Autumn", "abundance", "lack"],
["4", "Diamonds", "Status Quo", "Order", "Rebellion"],
["5", "Diamonds", "Succubus", "Power at a Cost", "Temptation"],
["6", "Diamonds", "Treasure", "windfall", "thieves"],
["7", "Diamonds", "Armor", "protection", "overprotection"],
["8", "Diamonds", "Key", "Open", "Close"],
["9", "Diamonds", "Magpie", "collect", "waste"],
["10", "Diamonds", "Peacock", "amusement", "vanity"],
["Jack", "Diamonds", "Merchant", "calculated risk", "debt"],
["Queen", "Diamonds", "Luck", "good fortune", "mischance"],
["King", "Diamonds", "Dragon", "self-interest", "hoarding"],

["Ace", "Spades", "Phoenix", "Rebirth", "Destruction"],
["2", "Spades", "Wolf", "Outsider", "Outcast"],
["3", "Spades", "Summer", "Passion", "Exhaustion"],
["4", "Spades", "Vampire", "Natural", "Supernatural"],
["5", "Spades", "Shadows", "justified caution", "fear of shadows"],
["6", "Spades", "Whip", "Pleasure", "Pain"],
["7", "Spades", "Ship", "journey", "shipwreck"],
["8", "Spades", "Crossed Swords", "combat", "subjugation"],
["9", "Spades", "Toy", "novelty", "recklessness"],
["10", "Spades", "Fertility", "Purposeful Growth", "Wantonness"],
["Jack", "Spades", "Soldier", "skill", "overspecialization"],
["Queen", "Spades", "Amazon", "power", "arrogance"],
["King", "Spades", "Death", "change", "stasis"],

["Ace", "Clubs", "Unicorn", "Innocence", "Ruse"],
["2", "Clubs", "Stars", "Insight", "Overreach"],
["3", "Clubs", "Winter", "Hard Choice", "Selfishness"],
["4", "Clubs", "Birds", "Intuition", "Logic"],
["5", "Clubs", "Sun", "revelation", "blindness"],
["6", "Clubs", "Trial", "truth", "falsehood"],
["7", "Clubs", "Child", "maturity", "childishness"],
["8", "Clubs", "Veil", "disguise", "self-deception"],
["9", "Clubs", "Anchor", "security", "weight"],
["10", "Clubs", "Palace", "luxury", "bureaucracy"],
["Jack", "Clubs", "Judge", "justice", "injustice"],
["Queen", "Clubs", "Empress", "generosity", "generosity with strings"],
["King", "Clubs", "Emperor", "authority", "tyranny"]
]

# Principles, Agenda, GM Moves

agenda = ["Challenge yourself; ask difficult questions.", "Play to find out what happens."]

agendalist = [
"Make the heroes' lives bold and full of larger than life dilemmas.",
"Fill the heroes' lives with darkness to throw the light into relief.",
"Fill the heroes' lives with dilemmas and wonder.",
"Fill the heroes' lives with tension and unexpected twists.",
"Fill the heroes' lives with risk and adventure.",
"Fill the heroes' lives with chivalry and romance.",
]

agenda.append(random.choice(agendalist))

principles = ["Be a fan of the heroes, but make them prove they deserve the role.",
"Nobody has plot immunity; nothing is safe. Build the world and mythos as you go.",
"Be honest, even when it hurts; follow the fiction where it leads.",]

principlelist = [
"Look for the extremes of good and evil but explore the gray areas in between.",
"Juxtapose the normal and the horrific, the mundane and the uneasily other.",
"The heroes are a wild card and people will look to them to solve their problems.",
"Sex is always a factor; everyone wants to consume the heroes.",
"The heroes are special; celebrate it but also make them prove it.",
"Seek out the exotic and strange but interject the familiar.",
"The truth is all-powerful; oaths and bargains have their own magic.",
]

principles = principles + random.sample(principlelist, random.randint(1,len(principlelist)))

# choose some stat names at random

# Reflexive/Graceful

reflex = ["Reflex", "Grace", "Cool", "Dexterity", "Quickness", "Grasp"]

# Persuasive/Assertive

social = ["Persuasion", "Assertiveness", "Hotness", "Charm", "Charisma", "Social", "Glib"]

# Aggressive/Forceful

force = ["Aggression", "Force", "Hardness", "Daring", "Combat", "Strength", "Attack"]

# Calculating/Methodical

mind = ["Calculation", "Precision", "Cunning", "Sharp", "Intelligence", "Mind", "Brains"]

# Inquisitive/Exploratory

explore = ["Inquisitiveness", "Curiousity", "Whim", "Weird", "Sensitive", "Wisdom", "Magic", "Spirit"]

# but just set them to recognizable defaults for now for sanity testing
reflex = ["Dexterity"]
social = ["Charisma"]
force = ["Strength"]
mind = ["Intelligence"]
explore = ["Magic"]
# end comment out block

stats = [
random.choice(reflex),
random.choice(social),
random.choice(force),
random.choice(mind),
random.choice(explore),
]

card = random.choice(cards)

print()
print("*** " + card[2] + " World ***")
print()

print("The theme of the setting is \"" + premise + "\".")

print()

print("The main struggle is between \"" + card[3].lower() + "\" and \"" + card[4].lower() + "\".")

print()

print("The Stats are: " + ", ".join(stats) + ".\n")

print("Your Agenda is:\n" + "\n".join(agenda))
print()
print("Your Principles Are:\n" + "\n".join(principles))

# generate a playbook for each of the premise playbooks, suggesting a stat but allowing the end user to customize it

movetypes = [
"When you do something relating to [specialty], add +1.",
"You have the ability to [do some sort of active special power]. It counts as a basic move using [statA].",
"You have [some passive special power that has a constant effect].",
"You have a [thing]. When applicable, it adds +1 to [statA] and [statB].",
"When you do [specialty], mark XP.",
"Add +1 to [statA].",
]

# these are the playbooks
count = 0
for item in playbooks:

    print("\n")

    moves = [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)]

    movecats = random.sample(["Explore", "Fight", "Social", "Weird"], 2) + random.sample(["Explore", "Fight", "Social", "Weird"], 2)

    for i in range(len(moves)):
        if "[statB]" in moves[i]:
            temp = random.sample(stats,2)
            moves[i] = moves[i].replace("[statA]", temp[0])
            moves[i] = moves[i].replace("[statB]", temp[1])
        if "[statA]" in moves[i]:
            moves[i] = moves[i].replace("[statA]", random.choice(stats))
        if "[specialty]" in moves[i]:
            moves[i] = moves[i].replace("[specialty]", "\x1B[3m" + random.choice(pbspecialties[count]) + "\x1B[23m")

    keyword = random.choice(keywords)

    print(item.upper())
    print()

    #print("Title")

    titlelist = ["Core Class Move", movecats[0] + " Move", movecats[1] + " Move", movecats[2] + " Move", keyword.title() + " Move (\x1B[3munique keyword for this playbook\x1B[23m)", random.choice([card[3],card[4]]).title() + " Move (\x1B[3mrelates to the core dilemma of the setting\x1B[23m)", premise.title() + " Move (\x1B[3mrelates to the theme of the setting\x1B[23m)" ]

    for x in range(len(titlelist)):
        print(titlelist[x])
        print(moves[x])
        print()

    count = count + 1
