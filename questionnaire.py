import random
from dominate import tags

from psynet.demography.general import (
    BasicDemography,
    BasicMusic,
    Dance,
    HearingLoss,
    Income,
    Language,
    LanguagesInOrderOfProficiency,
    MotherTongues,
)
from psynet.demography.gmsi import GMSI
from psynet.modular_page import ModularPage, RadioButtonControl, TextControl
from psynet.page import InfoPage
from psynet.timeline import join


def introduction():
    html = tags.div()
    with html:
        tags.p(
            "Congratulations, you completed the main experiment!"
        )
        tags.p(
            "Before we finish, we would like to ask you a few questions about you and the study. ",
            "They should only take a couple of minutes to complete.",
        )
    return InfoPage(html, time_estimate=10)


def questionnaire():
    return join(
        introduction(),
        BasicDemography(),
        Language(),
        MotherTongues(),
        BasicMusic(),
        musical_tradition_forced_choice(),
        musical_tradition_open(),
        GMSI(subscales=["Musical Training"]),
        feedback(),
        debrief()
    )


def musical_tradition_open():
    return ModularPage(
        "main_musical_tradition",
        prompt="Which musical tradition best describes your main musical training and practice?",
        control=TextControl(one_line=True),
        save_answer="main_musical_tradition",
        time_estimate=5,
    )


def musical_tradition_forced_choice():
    return ModularPage(
        "musical_tradition_practice",
        prompt="Which musical tradition best describes your musical practice?",
        control=RadioButtonControl(
            ["western_classical", "traditional_turkish", "other"],
            [
                "Western classical music",
                "Traditional Turkish music",
                "Other",
            ],
            name="musical_tradition_practice",
            arrange_vertically=False,
        ),
        save_answer="musical_tradition_practice",
        time_estimate=5,
    )


def feedback():
    return ModularPage(
        "feedback",
        "Do you have any feedback to give us about the experiment?",
        TextControl(one_line=False),
        bot_response="I am just a bot, I don't have any feedback for you.",
        save_answer="feedback",
        time_estimate=5,
    )


# def debrief():
#     html = tags.div()

#     with html:
#         tags.p(
#             """
#             Thank you for participating in this experiment. The purpose of the experiment was to collect data on how we 
#             perceive and sing melodies (sequences of musical tones), such as the ones you have been listening to. In particular, 
#             we are interested in studying the role of emotions in the perception of melodies.
#             """
#         )
#         tags.p(
#             """
#             The data collected during this experiment will help to better understand how people derive emotions from 
#             melodies, studying for the first time all possible melodic combinations and listeners' individual 
#             differences at a large scale (testing many melodies and participants from different backgrounds).
#             """
#         )

#     return InfoPage(html, time_estimate=5)

def debrief():
    html = tags.div()

    with html:
        tags.h3("Debrief")
        
        tags.p(
            """
            Thank you for taking part in this listening and singing experiment.
            """
        )

        tags.p(
            """
            The aim of this study is to understand how musical expertise shapes the way people perceive, imagine, 
            and reproduce melodies. In this experiment, you were asked to listen to melodies and sing them back, 
            allowing us to study how accurately people can recall and reproduce musical information.
            """
        )

        tags.p(
            """
            You were invited to take part in this study based on your level of musical expertise. By comparing 
            participants with different musical backgrounds, we aim to better understand individual differences 
            in musical perception and production.
            """
        )

        tags.p(
            """
            All data collected in this study will be treated in the strictest confidence. Please note that once 
            the study results and materials are made publicly available (e.g., through academic publication or 
            open science practices), it may no longer be possible to withdraw or delete your data, including any 
            voice recordings.
            """
        )

        tags.p(
            """
            If you would like more information about this study, or if you have any questions, please feel free 
            to contact the researcher supervisor, Dr. Manuel Anglada-Tort (m.anglada-tort@gold.ac.uk).
            """
        )

        tags.p(
            """
            Thank you again for your valuable contribution to this research.
            """
        )

    return InfoPage(html, time_estimate=5)