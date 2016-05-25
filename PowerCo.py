__author__ = 'dixonaws@amazon.com'

from __future__ import print_function


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


# ------------------------- on_session_started()

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


# ------------------------- on_launch()

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


# ------------------------- on_intent()

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # intent_request is a Python dict object
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    print("*** on_intent: I received intent=" + str(intent));
    print("*** on_intent: I received intent_name=" + str(intent_name));

    # Dispatch to your skill's intent handlers
    if intent_name == "VerifyPIN":
        return verifyPIN(intent, session)
    elif intent_name == "MainMenu":
        return mainMenu(intent, session)
    elif intent_name == "GetAccount":
        return getAccount(intent, session)
    elif intent_name == "AccountCommand":
        return getAccountCommand(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


# ------------------------- verifyPIN()

def verifyPIN(intent, session):
    # We hardcode the matching PIN for now
    intCorrectPIN = 9876

    print("*** verifyPIN: I received intent " + str(intent));

    # Grab the PIN out of the intent and cast it to an integer
    PIN = intent['slots']['PIN']['value']
    intReceivedPIN = int(PIN)

    print("*** verifyPIN: I received PIN " + str(PIN))

    card_title = "Welcome"

    # Compare the PIN we received with the correct PIN
    if (intReceivedPIN == intCorrectPIN):
        return mainMenu()

    elif (intReceivedPIN != intCorrectPIN):
        speech_output = "Hmmm. That PIN code doesn't match my records";

    # Setting this to true ends the session and exits the skill.
    should_end_session = True

    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# ------------------------- getAccount()

def getAccount(intent, session):
    print("*** getAccount: I received intent" + str(intent));
    strAccountNumber = "2 0 1 3 4 dash 0 9 4"

    card_title = "Welcome"

    speech_output = "Here are some details for that account... account number " + strAccountNumber + ",,," \
                                                                                                     "Total amount due for the month of May: $94.12" + ",,,," \
                                                                                                                                                       "Due date: June 16, 2016" + ",,,," \
                                                                                                                                                                                   "Consumption: 748 kilowatt hours." + ",,,," \
                                                                                                                                                                                                                        "Say 'stats' if you want me to analyze your consumption.";

    # Setting this to true ends the session and exits the skill.
    should_end_session = False
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# ------------------------- getAccountCommand()

def getAccountCommand(intent, session):
    print("*** getAccountCommand: I received intent" + str(intent));
    strAccountNumber = "2 0 1 3 4 dash 0 9 4"

    card_title = "Welcome"

    speech_output = "Here is the analysis of your bill for the month of May,,," \
                    "Consumption: 748 kilowatt hours." + ",,,," \
                                                         "Which was 119% of April's consumption of 629 kilowatt hours,,," \
                                                         "Last year, you consumed 792 kilowatt hours versus 748 this year,,," \
                                                         "Your consumption is about average, households of similar type in" \
                                                         "your zipcode consume between 512 " \
                                                         "and 1,298 kilowatt hours of energy in the summer months,,," \
                                                         "I sent a PDF report to your inbox j p dixon@gmail.com";

    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# ------------------------- onSessionEnded()

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Hi there! You're on line with PowerCo! To verify it's you, please say " \
                    "the 4 digit code that you created when you enabled the skill for the first time."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "You created a 4 digit pin code the first time you enabled the" \
                    "PowerCo skill. If you remember it, go ahead and say it now."

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# ------------------------- mainMenu()

def mainMenu():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Great! You're all set. I found three accounts in your profile. Which account can I " \
                    "help you with? 1. 3 2 1 0 Piedmont Rd? 2. 1 0 4 6 Peachtree Road? 3. 2 1 2 1 Jamieson Avenue?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I'm here to help. You can ask me about your current bill, just say the number" \
                    "corresponding with the account, 1. 3 2 1 0 Piedmont Rd? 2. 1 0 4 6 Peachtree Road? 3. 2 1 2 1 Jamieson Avenue?"

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# ------------------------- handle_session_end_request()

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for being a PowerCo customer." \
                    "Have a nice day! "

    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))



# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }