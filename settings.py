SESSION_CONFIGS = [
    dict(
        name='disposition_3groups',
        display_name='Disposition Effect Experiment - 3 Groups',
        app_sequence=['disposition'],
        num_demo_participants=6,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="Disposition effect online experiment with three randomized groups"
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'
DEMO_PAGE_INTRO_HTML = "Disposition Effect Experiment"
SECRET_KEY = 'replace-this-with-any-random-secret-key'
INSTALLED_APPS = ['otree']
