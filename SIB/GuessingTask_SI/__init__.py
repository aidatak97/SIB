from otree.api import *
import numpy as np
import random


c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_SI"
    num_rounds = 20
    players_per_group = None
    num_senders = 6
    true_state = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sd = 3


class Subsession(BaseSubsession):
    x = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    identity = models.StringField()  # the identity from the previous apps
    sent_signal = models.IntegerField()  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.FloatField()  # the posterior belief of the receiver
    true_state = models.IntegerField()
    received_signal_1 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_2 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_3 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_4 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_5 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_6 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_1_identity = models.BooleanField(initial=False) #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_2_identity = models.BooleanField(initial=False) #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_3_identity = models.BooleanField(initial=False) #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_4_identity = models.BooleanField(initial=False) #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_5_identity = models.BooleanField(initial=False) #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_6_identity = models.BooleanField(initial=False) #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    comprq1 = models.IntegerField(choices=[[1, 'The estimate of a randomly drawn estimation device is equally likely to be the correct number x or any other number.'],
                                           [2, 'The estimate of a randomly drawn estimation device is less likely to be '
                                               'the correct number x than any other number, and the further one moves away '
                                               'from x, the more likely it is that an estimation device reports such a number.'],
                                           [3, 'The estimate of a randomly drawn estimation device is more likely to be '
                                               'the correct number x than any other number, and the further one moves away '
                                               'from x, the less likely it is that an estimation device reports such a number.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq2 = models.IntegerField(choices=[[1, 'The average of estimates of all the estimation devices can be any number with equal probability.'],
                                           [2, 'The average of estimates of all the estimation devices corresponds exactly (or almost exactly) to number x'],
                                           [3, 'The average of estimates of all the estimation devices will always be larger than number x.'],
                                           [4, 'The average of estimates of all the estimation devices will always be smaller than number x.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq3 = models.IntegerField(choices=[[1, 'I will observe an estimate of 1 randomly drawn estimation device.'],
                                           [2, 'I will observe the estimates of 3 randomly drawn estimation devices.'],
                                            [3, 'I will observe the actual number x and the estimate of 1 randomly drawn estimation device.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq4 = models.IntegerField(choices=[[1, 'A randomly drawn estimation device shows me an estimate of 490.'],
                                           [2, 'A randomly drawn estimation device shows me an estimate of 541.'],
                                            [3, 'A randomly drawn estimation device shows me an estimate of 555.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq5 = models.IntegerField(choices=[[1, '9'],
                                           [2, '18'],
                                            [3, '19'],
                                            [4, '24']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq6 = models.IntegerField(choices=[[1, 'All parts of the experiment in which additional money can be earned will be paid out.'],
                                           [2, 'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. '
                                               'If it happens that part 2 is chosen, then the earnings from each of the 10 estimation tasks will be paid out.'],
                                           [3, 'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. '
                                               'If it happens that part 2 is chosen, then one of the 10 estimation tasks will be randomly chosen, and my additional payment will depend only on my precision on that particular estimation task.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq7 = models.IntegerField(
        choices=[[1, 'Each sender observed an estimate of 1 randomly drawn estimation device.'],
                 [2, 'Each sender observed an estimate of 3 randomly drawn estimation devices.'],
                 [3,
                  'Each sender observed an estimate of an actual number x and the estimate of 1 randomly drawn estimation device.']],
        widget=widgets.RadioSelect,
        label='')
    comprq8 = models.IntegerField(choices=[[1, 'I will observe an estimate of 1 randomly drawn estimation device.'],
                                           [2, 'I will observe an estimate of 6 randomly drawn estimation devices.'],
                                           [3, 'I will observe an estimate of 1 sender.'],
                                           [4, 'I will observe the estimates of 6 different senders.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq9 = models.IntegerField(choices=[[1,
                                            'The estimate of a randomly drawn estimation device is equally likely to be the correct number x or any other number'],
                                           [2,
                                            'The estimate of a randomly drawn estimation device is less likely to be the correct number x than any other number, and the further one moves away from x, the more likely it is that an estimation device reports such a number'],
                                           [3,
                                            'The estimate of a randomly drawn estimation device is more likely to be the correct number x than any other number, and the further one moves away from x, the less likely it is that an estimation device reports such a number']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq10 = models.IntegerField(choices=[
        [1, 'The average of estimates of all the estimation devices can be any number with equal probability.'],
        [2,
         'The average of estimates of all the estimation devices corresponds exactly (or almost exactly) to number x.'],
        [3, 'The average of estimates of all the estimation devices will always be larger than number x.'],
        [4, 'The average of estimates of all the estimation devices will always be smaller than number x.']],
                                   widget=widgets.RadioSelect,
                                   label='')
    comprq11 = models.IntegerField(
        choices=[[1, 'A sender’s randomly drawn estimation device showed an estimate of 490.'],
                 [2, 'A sender’s randomly drawn estimation device showed an estimate of 541.'],
                 [3, 'A sender’s randomly drawn estimation device showed an estimate of 555.']],
        widget=widgets.RadioSelect,
        label='')
    comprq12 = models.IntegerField(choices=[[1, '9'],
                                            [2, '18'],
                                            [3, '19'],
                                            [4, '24']],
                                   widget=widgets.RadioSelect,
                                   label='')
    comprq13 = models.IntegerField(choices=[[1, '1490'],
                                            [2, '1520'],
                                            [3, '1521'],
                                            [4, '1525']],
                                   widget=widgets.RadioSelect,
                                   label='')
    comprq14 = models.IntegerField(
        choices=[[1, 'All parts of the experiment in which additional money can be earned will be paid out.'],
                 [2,
                  'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. '
                  'If it happens that part 3 is chosen, then the earnings from each of the 10 estimation tasks will be paid out.'],
                 [3,
                  'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. If it happens that part 3 is chosen, then one of the 10 estimation tasks will be randomly chosen, and my additional payment will depend only on my precision on that particular estimation task.']],
        widget=widgets.RadioSelect,
        label='')

    q1 = models.IntegerField(label='')
    q2 = models.IntegerField(label='')
    q3 = models.StringField(label='')
    q4 = models.StringField(label='')
    q5 = models.IntegerField(
        choices=[[0, "Weiblich"],
                 [1, "Mänlich"],
                  [2, "Divers"]],
        widget=widgets.RadioSelect, label=''
        )
    q6 = models.StringField(label='')
    q7 = models.IntegerField(label='')
    q8 = models.IntegerField(label='')
    q9 = models.IntegerField(label='')
    q10 = models.IntegerField(
        choices=[[1, "Poor"],
                 [2, "Average"],
                  [3, "Good"],
                 [4, "Excellent"]],
        widget=widgets.RadioSelect, label=''
        )
    q11 =  models.IntegerField(
        choices=[[1, "Poor"],
                 [2, "Average"],
                  [3, "Good"],
                 [4, "Excellent"]],
        widget=widgets.RadioSelect, label=''
        )
    q12 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q13 =  models.IntegerField(
        choices=[[1, "I’ve always known how to budget"],
                 [2, "I’ve had to learn to budget whilst at University"],
                 [3, "I struggle to purchase necessities"],
                 [4, "I can afford everything but I don’t budget"]],
        widget=widgets.RadioSelect, label=''
        )
    q14 = models.IntegerField(
        choices=[[1, "Not budgeting"],
                 [2, "Cost of necessities too expensive"],
                 [3, "Too care-free with money"],
                 [4, "Other priorities such as shopping & nightlife take a priority"],
                 [5, "I don’t struggle"],
                 [6, " I’m good with budgeting"],
                 [7, " I have no idea"]],
        widget=widgets.RadioSelect, label=''
        )
    q15 = models.StringField(label='')
    q16 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q17 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q18 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q19 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q20 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q21 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
        )
    q22 = models.IntegerField(
        choices=[[1, "Student Union"],
                 [2, "Parents"],
                 [3, "Friends"],
                 [4, "Bank"],
                 [5, "Financial adviser"],
                 [6, "Other"]],
        widget=widgets.RadioSelect, label=''
        )
    q23 = models.StringField(label='')
    q24 = models.StringField(label='')
    q25 = models.StringField(label='')




# FUNCTIONS

#roles allocation and mu_signals (true) simulation for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    subsession.x = random.randint(0, 50)
    estimates = np.random.normal(Constants.true_state[subsession.round_number - 1], Constants.sd, Constants.num_senders)
    estimates = np.rint(estimates)
    for p in players:  # Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.Role = participant.Role
        if p.Role == "sender":
            p.estimate = estimates[p.id_in_group - 1]
        if p.round_number <= Constants.num_rounds / 2:
            p.true_state = Constants.true_state[subsession.round_number - 1]
        else:
            p.true_state = Constants.true_state[int(subsession.round_number - Constants.num_rounds / 2) - 1]
        participant = p.participant
        p.identity = participant.identity


# PAGES


# senders see estimate and send signal
class Signals(Page):
    form_model = "player"
    form_fields = ["sent_signal"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((Constants.true_state[int(player.round_number) - 1] - player.sent_signal), 2)
        if diff <= player.subsession.x:
            player.payoff = player.session.config['GT_receiver_payoff']
        else:
            player.payoff = 0

    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number <= Constants.num_rounds/2

    def vars_for_template(player: Player):
        estimate = player.estimate
        return dict(
            estimate=estimate,
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round=player.round_number,
        )


class Instructions_GT_senders(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1

    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3", "comprq4", "comprq5", "comprq6"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3=1,
            comprq4=2,
            comprq5=3,
            comprq6=3,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigiere deine Angabe oder hebe deine Hand zur Klärung mit dem Laborpersonal.'

        return error_messages


class Instructions_GT_receivers(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == (Constants.num_rounds / 2) + 1

    form_model = "player"
    form_fields = ["comprq7", "comprq8", "comprq9", "comprq10", "comprq11", "comprq12", "comprq13", "comprq14"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq7=1,
            comprq8=4,
            comprq9=3,
            comprq10=2,
            comprq11=2,
            comprq12=3,
            comprq13=2,
            comprq14=3,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigiere deine Angabe oder hebe deine Hand zur Klärung mit dem Laborpersonal.'

        return error_messages


# wait for all senders to send a signal
class StartWaitPage(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player):
        return player.round_number == (Constants.num_rounds / 2) + 1



class Filler_Task(Page):
    form_model = "player"
    form_fields = ["q"+str(i) for i in range(1, 26)]


    @staticmethod
    def is_displayed(player):
        return (player.Role == "receiver" and player.round_number == 1) or (player.Role == "sender" and player.round_number == Constants.num_rounds/2 + 1)





# the receiver observes all the signals sent by senders and states a guess/posterior
# Receivers see signals sent by senders in a random order and with known group identity
class Guess(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((Constants.true_state[int(player.round_number - Constants.num_rounds / 2) - 1] - player.posterior), 2)
        if diff <= player.subsession.x:
            player.payoff = player.session.config['GT_receiver_payoff']
        else:
            player.payoff = 0


    @staticmethod
    def vars_for_template(player: Player):
        current_round = player.round_number
        prev_player = player.in_round(current_round - Constants.num_rounds/2)
        prev_players = prev_player.group.get_players()
        signals = [p.sent_signal for p in prev_players if p.Role =='sender']
        identities = [p.participant.identity for p in prev_players if p.Role == 'sender']

        if player.Role == "receiver":   # Gathering all signals and the resp. sender's identities for analyses -
                                        # this part works but can be improved with a loop or something
            player.received_signal_1 = signals[0]
            if identities[0] == player.participant.identity:
                player.received_signal_1_identity = True
            player.received_signal_2 = signals[1]
            if identities[1] == player.participant.identity:
                player.received_signal_2_identity = True
            player.received_signal_3 = signals[2]
            if identities[2] == player.participant.identity:
                player.received_signal_3_identity = True
            player.received_signal_4 = signals[3]
            if identities[3] == player.participant.identity:
                player.received_signal_4_identity = True
            player.received_signal_5 = signals[4]
            if identities[4] == player.participant.identity:
                player.received_signal_5_identity = True
            player.received_signal_6 = signals[5]
            if identities[5] == player.participant.identity:
                player.received_signal_6_identity = True
            return dict(
                signal_1=signals[0],
                signal_2=signals[1],
                signal_3=signals[2],
                signal_4=signals[3],
                signal_5=signals[4],
                signal_6=signals[5],
            )

    form_model = "player"
    form_fields = ["posterior"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number > Constants.num_rounds/2

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round=player.round_number - Constants.num_rounds / 2,
        )

class SecondWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'save_signals_payoff'

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


def save_signals_payoff(subsession: Subsession):
    players = subsession.get_players()
    signals_all_rounds = []
    estimates_all_rounds = []

    for i in list(range(0, int(Constants.num_rounds / 2))):
        for p in players:
            if p.Role == 'sender':
                prev_player = p.in_round(i + 1)
                signals_all_rounds.append(prev_player.field_maybe_none('sent_signal'))
                estimates_all_rounds.append(prev_player.estimate)
    # Payoff calculation
    for p in players:
        participant = p.participant
        participant.estimates_all_rounds = estimates_all_rounds
        participant.signals_all_rounds = signals_all_rounds
        if p.Role == "sender":
            i = random.randint(1, int(Constants.num_rounds / 2))
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff
        if p.Role == "receiver":
            i = random.randint(int(Constants.num_rounds / 2) + 1, Constants.num_rounds)
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff




page_sequence = [Instructions_GT_senders, StartWaitPage, Signals, Filler_Task, Instructions_GT_receivers,
                 Guess, SecondWaitPage]
