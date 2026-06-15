from otree.api import *


GAIN_SCENARIOS = [
    dict(number=1, purchase=100, current=120, info="Analysts say future performance is uncertain.", field="decision_1"),
    dict(number=2, purchase=100, current=135, info="The stock recently performed better than expected.", field="decision_2"),
    dict(number=3, purchase=100, current=160, info="Some analysts believe the price may decline in the future.", field="decision_3"),
    dict(number=4, purchase=100, current=125, info="Market news is mixed and future performance is unclear.", field="decision_4"),
    dict(number=5, purchase=100, current=150, info="The company has reported strong recent results.", field="decision_5"),
    dict(number=6, purchase=100, current=130, info="Analysts disagree about whether the price will keep increasing.", field="decision_6"),
]

LOSS_SCENARIOS = [
    dict(number=1, purchase=100, current=80, info="Analysts say future performance is uncertain.", field="decision_1"),
    dict(number=2, purchase=100, current=65, info="The stock recently performed worse than expected.", field="decision_2"),
    dict(number=3, purchase=100, current=40, info="Some analysts believe the price may recover in the future.", field="decision_3"),
    dict(number=4, purchase=100, current=75, info="Market news is mixed and future performance is unclear.", field="decision_4"),
    dict(number=5, purchase=100, current=50, info="The company has reported weak recent results.", field="decision_5"),
    dict(number=6, purchase=100, current=70, info="Analysts disagree about whether the price will recover.", field="decision_6"),
]

MIXED_SCENARIOS = [
    dict(number=1, purchase=100, current=120, info="Analysts say future performance is uncertain.", field="decision_1"),
    dict(number=2, purchase=100, current=80, info="Analysts say future performance is uncertain.", field="decision_2"),
    dict(number=3, purchase=100, current=135, info="The stock recently performed better than expected.", field="decision_3"),
    dict(number=4, purchase=100, current=65, info="The stock recently performed worse than expected.", field="decision_4"),
    dict(number=5, purchase=100, current=130, info="Some analysts believe the price may decline in the future.", field="decision_5"),
    dict(number=6, purchase=100, current=70, info="Some analysts believe the price may recover in the future.", field="decision_6"),
]


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'investment_experience',
        'finance_courses',
        'known_assets_stocks',
        'known_assets_bonds',
        'known_assets_crypto',
        'known_assets_funds',
        'known_assets_real_estate',
    ]

    def before_next_page(self):
        if not self.player.field_maybe_none('condition'):
            import random
            self.player.condition = random.choice(['gain', 'loss', 'mixed'])


class InvestmentScenarios(Page):
    form_model = 'player'
    form_fields = [
        'decision_1',
        'decision_2',
        'decision_3',
        'decision_4',
        'decision_5',
        'decision_6',
    ]

    def vars_for_template(self):
        condition = self.player.field_maybe_none('condition')
        if condition == 'gain':
            scenarios = GAIN_SCENARIOS
            condition_label = "Gain condition"
        elif condition == 'loss':
            scenarios = LOSS_SCENARIOS
            condition_label = "Loss condition"
        else:
            scenarios = MIXED_SCENARIOS
            condition_label = "Mixed/control condition"

        return dict(scenarios=scenarios, condition_label=condition_label)


class Regret(Page):
    form_model = 'player'
    form_fields = [
        'regret_sell_recovery',
        'regret_hold_decline',
        'regret_realize_loss',
        'regret_missed_gain',
    ]


class LossAversion(Page):
    form_model = 'player'
    form_fields = [
        'loss_aversion_1',
        'loss_aversion_2',
        'loss_aversion_3',
        'loss_aversion_4',
    ]


class Confidence(Page):
    form_model = 'player'
    form_fields = ['confidence', 'perceived_skill', 'risk_tolerance']


class Explanation(Page):
    form_model = 'player'
    form_fields = ['comments']


class Debrief(Page):
    pass


page_sequence = [
    Consent,
    Demographics,
    InvestmentScenarios,
    Regret,
    LossAversion,
    Confidence,
    Explanation,
    Debrief,
]
