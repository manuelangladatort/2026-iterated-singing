from markupsafe import Markup
from psynet.page import InfoPage


def welcome():
    return InfoPage(
        Markup(
            """
            <h3>Welcome</h3>
            <hr>
            Thank you for taking part in our study on singing.<br><br>
            We are interested in how musical background and cultural experience relate to how people perceive and sing melodies.<br><br>
            You will complete a series of short tasks where you listen to melodies and sing them back, followed by a few questions about your musical experience.
            <hr>
            """
        ),
        time_estimate=3
    )


def requirements_mic():
    return InfoPage(
        Markup(
            """
            <h3>Requirements</h3>
            <hr>
            <ul>
                <li>You must use a working microphone, either from your headphones or computer.</li>
                <li>You must be in a quiet room (with no background noises).</li>
            </ul>
            If you cannot meet these requirements, please stop the study now and return to it later when you can.
            <hr>
            """
        ),
        time_estimate=3
    )
