from otree.api import *
import random
c = Currency

doc = """
SIM_SI
"""


class Constants(BaseConstants):
    name_in_url = 'SIM_SI'
    players_per_group = None
    num_rounds = 1
    use_timeout = False
    guess_time = 600
    labelled_time = 300
    artist_payoff = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.StringField()
    artist1 = models.StringField(
        choices=['Paul Klee', 'Wassily Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist2 = models.StringField(
        choices=['Paul Klee', 'Wassily Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist_points = models.IntegerField(initial=0)


# PAGES
class Instructions(Page):
    pass


class MyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'payout_calc'

    # Function to determine which individual has won the SIM
    # Winner is determined by amount of solved paintings (or at random if amount of solved paintings is equal)

def payout_calc(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        participant = p.participant
        p.identity = participant.identity
    for p in players:
        if p.artist1 == "Paul Klee":
            p.artist_points += 1
        if p.artist2 == "Wassily Kandinsky":
            p.artist_points += 1
    correct_yellow = 0
    correct_blue = 0
    for p in players:
        if p.identity == "Yellow":
            correct_yellow += p.artist_points
        if p.identity == "Blue":
            correct_blue += p.artist_points
    for p in players:
        participant = p.participant
        if correct_yellow > correct_blue and p.identity == "Yellow":
            p.payoff = Constants.artist_payoff
            participant.SIM_payoff = p.payoff
        if correct_yellow < correct_blue and p.identity == "Blue":
            p.payoff = Constants.artist_payoff
            participant.SIM_payoff = p.payoff
    if correct_yellow == correct_blue:
        winner = random.choice(["Yellow", "Blue"])
        for p in players:
            participant = p.participant
            if p.identity == winner:
                p.payoff = Constants.artist_payoff
                participant.SIM_payoff = p.payoff
            else:
                p.payoff = 0
                participant.SIM_payoff = p.payoff



class Paintings_labelled(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.labelled_time


class Paintings_guess(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.guess_time
    form_model = 'player'
    form_fields = ['artist1', 'artist2']


page_sequence = [Instructions, Paintings_labelled, Paintings_guess, MyWaitPage]
