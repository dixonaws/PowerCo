<h1>Alexa skill - PowerCo v1.0</h1>
This skill allows PowerCo Energy customers to check their recent bill and energy usage.
Launch the skill by saying "Launch PowerCo" or "Open PowerCo" The program will then ask you to authenticate with
a 4-digit PIN. In this version, the PIN has been hardcoded as "9876". The skill will then list the addresses that are
associate with your account. Choose one of the addresses simply by saying the number that corresponds to the address, like "Two."
As with the PIN, the addresses and account information are hardcoded into the skill in this version. Alexa will
then read the account detail, including the current amount due, due date, and energy consumption. You can then say "Read
me some stats" to have Alexa read some analysis of the current bill. The skill then exits after it has read the analysis
information.

<h2>Source Files</h2>
<b>IntentSchema.json</b><br>
This schema defines the intents and word formats for which our skill will listen. This code needs to be entered into the skill configuration on the Alexa page of your Amazon Developer Account.
<br>

<b>PowerCo.py</b><br>
This is the Python source code for the Lambda function that powers the skill.
<br>

<b>PowerCoAPITest.py</b><br>
This is Python code that is used to test how a JSON object is returned from an API and processed for use by the Alexa skill.
<br>

<b>SampleUtterances.txt</b><br>
This code needs to be entered into the skill configuration on the Alexa page of your Amazon Developer Account.
