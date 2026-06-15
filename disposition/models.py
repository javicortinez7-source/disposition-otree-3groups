from otree.api import *
import random


doc = """
Online experiment about the disposition effect in investment decisions.
Participants are randomly assigned to one of three conditions:
gain, loss, or mixed/control.
"""


class C(BaseConstants):
    NAME_IN_URL = 'disposition'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    conditions = ['gain', 'loss', 'mixed']
    for p in subsession.get_players():
        p.condition = random.choice(conditions)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    condition = models.StringField()

    consent = models.BooleanField(
        label="I confirm that I am at least 18 years old and voluntarily agree to participate in this study.",
        choices=[[True, "Yes, I agree"]],
        widget=widgets.RadioSelect
    )

    age = models.IntegerField(label="What is your age?", min=18, max=100)

    gender = models.StringField(
        label="What is your gender?",
        choices=[
            ['female', 'Female'],
            ['male', 'Male'],
            ['non_binary', 'Non-binary'],
            ['prefer_not', 'Prefer not to say'],
            ['other', 'Other'],
        ],
        widget=widgets.RadioSelect
    )

    investment_experience = models.StringField(
        label="How would you describe your investment experience?",
        choices=[
            ['none', 'No investment experience'],
            ['basic', 'Basic knowledge, but little or no real investing experience'],
            ['some', 'Some investing experience'],
            ['experienced', 'Experienced investor'],
        ],
        widget=widgets.RadioSelect
    )

    finance_courses = models.StringField(
        label="Have you taken finance or investment-related courses?",
        choices=[['yes', 'Yes'], ['no', 'No']],
        widget=widgets.RadioSelect
    )

    known_assets_stocks = models.BooleanField(label="Stocks", blank=True)
    known_assets_bonds = models.BooleanField(label="Bonds", blank=True)
    known_assets_crypto = models.BooleanField(label="Cryptocurrencies", blank=True)
    known_assets_funds = models.BooleanField(label="Mutual funds / ETFs", blank=True)
    known_assets_real_estate = models.BooleanField(label="Real estate investments", blank=True)

    decision_1 = models.StringField(choices=[['sell', 'Sell'], ['hold', 'Hold']], widget=widgets.RadioSelect)
    decision_2 = models.StringField(choices=[['sell', 'Sell'], ['hold', 'Hold']], widget=widgets.RadioSelect)
    decision_3 = models.StringField(choices=[['sell', 'Sell'], ['hold', 'Hold']], widget=widgets.RadioSelect)
    decision_4 = models.StringField(choices=[['sell', 'Sell'], ['hold', 'Hold']], widget=widgets.RadioSelect)
    decision_5 = models.StringField(choices=[['sell', 'Sell'], ['hold', 'Hold']], widget=widgets.RadioSelect)
    decision_6 = models.StringField(choices=[['sell', 'Sell'], ['hold', 'Hold']], widget=widgets.RadioSelect)

    regret_sell_recovery = models.IntegerField(
        label="If you sell an investment and it later increases in value, how much regret would you feel?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    regret_hold_decline = models.IntegerField(
        label="If you hold an investment and it later decreases in value, how much regret would you feel?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    regret_realize_loss = models.IntegerField(
        label="How uncomfortable would you feel selling an investment at a loss?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    regret_missed_gain = models.IntegerField(
        label="How uncomfortable would you feel selling too early and missing future gains?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    loss_aversion_1 = models.StringField(
        label="Which option would you choose?",
        choices=[
            ['safe', 'Option A: Receive EUR 10 for sure'],
            ['risky', 'Option B: 50% chance to win EUR 25 and 50% chance to lose EUR 10'],
        ],
        widget=widgets.RadioSelect
    )

    loss_aversion_2 = models.StringField(
        label="Which option would you choose?",
        choices=[
            ['safe', 'Option A: Receive EUR 15 for sure'],
            ['risky', 'Option B: 50% chance to win EUR 45 and 50% chance to lose EUR 20'],
        ],
        widget=widgets.RadioSelect
    )

    loss_aversion_3 = models.StringField(
        label="Which option would you choose?",
        choices=[
            ['safe', 'Option A: Receive EUR 20 for sure'],
            ['risky', 'Option B: 50% chance to win EUR 70 and 50% chance to lose EUR 30'],
        ],
        widget=widgets.RadioSelect
    )

    loss_aversion_4 = models.StringField(
        label="Which option would you choose?",
        choices=[
            ['safe', 'Option A: Receive EUR 25 for sure'],
            ['risky', 'Option B: 50% chance to win EUR 90 and 50% chance to lose EUR 40'],
        ],
        widget=widgets.RadioSelect
    )

    confidence = models.IntegerField(
        label="How confident are you in your investment decisions?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    perceived_skill = models.IntegerField(
        label="Compared with other people, how skilled do you think you are at making investment decisions?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    risk_tolerance = models.IntegerField(
        label="How willing are you to take financial risks?",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelectHorizontal
    )

    comments = models.LongStringField(
        label="Optional: briefly explain how you made your investment decisions.",
        blank=True
    )
