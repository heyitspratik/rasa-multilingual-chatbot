from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUttered, BotUttered
from rasa.core.channels.channel import InputChannel
import langid

class MyIO(InputChannel):
    def name() -> Text:
        """Name of your custom channel."""
        return "myio"


class ActionExtractMobileNumber(Action):
    def name(self) -> Text:
        return "action_extract_mobile_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extracting user events
        import pdb;pdb.set_trace()
        mobile_number = tracker.latest_message['metadata']['mobile_number']
        events = tracker.current_state()['events']

        custom_data = {"key": mobile_number}

        # Send a custom event to store the custom data
        bot_utterance = BotUttered(
            metadata={"metadata": custom_data}
        )
        return [bot_utterance]


    
class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # define language-specific responses
        responses = {
            'en': {
                'greet': 'utter_greet',
                'english': 'utter_english',
                'profile_menu': 'utter_profile_menu',
                'update_profile_picture': 'utter_update_profile_picture',
                'update_mobile': 'utter_update_mobile',
                'update_personal_details': 'utter_update_personal_details',
                'certificates': 'utter_certificates',
                'password_menu': 'utter_password_menu',
                'policy_menu': 'utter_policy_menu',
                'happy': 'utter_happy',
                'affirm': 'utter_affirm',
                'goodbye': 'utter_goodbye',
                'iamabot': 'utter_iamabot',
                'Thanks': 'utter_Thanks',
                'out_of_scope': 'utter_out_of_scope',
            },
            'hi': {
                'hindi': 'utter_hindi',
                'profile_menu_hindi': 'utter_profile_menu_hindi',
                'update_profile_picture_hindi': 'utter_update_profile_picture_hindi',
                'update_mobile_hindi': 'utter_update_mobile_hindi',
                'update_personal_details_hindi': 'utter_update_personal_details_hindi',
                'certificates_hindi': 'utter_certificates_hindi',
                'password_menu_hindi': 'utter_password_menu_hindi',
                'policy_menu_hindi': 'utter_policy_menu_hindi',
                'happy_hindi': 'utter_happy_hindi',
                'affirm_hindi': 'utter_affirm_hindi',
                'goodbye_hindi': 'utter_goodbye_hindi',
                'iamabot_hindi': 'utter_iamabot_hindi',
                'Thanks_hindi': 'utter_Thanks_hindi',
                'out_of_scope_hindi': 'utter_out_of_scope_hindi',
            },
            'mr': {
                'marathi': 'utter_marathi',
                'profile_menu_marathi': 'utter_profile_menu_marathi',
                'update_profile_picture_marathi': 'utter_update_profile_picture_marathi',
                'update_mobile_marathi': 'utter_update_mobile_marathi',
                'update_personal_details_marathi': 'utter_update_personal_details_marathi',
                'certificates_marathi': 'utter_certificates_marathi',
                'password_menu_marathi': 'utter_password_menu_marathi',
                'policy_menu_marathi': 'utter_policy_menu_marathi',
                'happy_marathi': 'utter_happy_marathi',
                'affirm_marathi': 'utter_affirm_marathi',
                'goodbye_marathi': 'utter_goodbye_marathi',
                'iamabot_marathi': 'utter_iamabot_marathi',
                'Thanks_marathi': 'utter_Thanks_marathi',
                'out_of_scope_marathi': 'utter_out_of_scope_marathi',
            },
            'ta': {
                'tamil': 'utter_tamil',
                'profile_menu_tamil': 'utter_profile_menu_tamil',
                'update_profile_picture_tamil': 'utter_update_profile_picture_tamil',
                'update_mobile_tamil': 'utter_update_mobile_tamil',
                'update_personal_details_tamil': 'utter_update_personal_details_tamil',
                'certificates_tamil': 'utter_certificates_tamil',
                'password_menu_tamil': 'utter_password_menu_tamil',
                'policy_menu_tamil': 'utter_policy_menu_tamil',
                'happy_tamil': 'utter_happy_tamil',
                'affirm_tamil': 'utter_affirm_tamil',
                'goodbye_tamil': 'utter_goodbye_tamil',
                'iamabot_tamil': 'utter_iamabot_tamil',
                'Thanks_tamil': 'utter_Thanks_tamil',
                'out_of_scope_tamil': 'utter_out_of_scope_tamil',
            },
            'or': {
                'odia': 'utter_odia',
                'profile_menu_odia': 'utter_profile_menu_odia',
                'update_profile_picture_odia': 'utter_update_profile_picture_odia',
                'update_mobile_odia': 'utter_update_mobile_odia',
                'update_personal_details_odia': 'utter_update_personal_details_odia',
                'certificates_odia': 'utter_certificates_odia',
                'password_menu_odia': 'utter_password_menu_odia',
                'policy_menu_odia': 'utter_policy_menu_odia',
                'happy_odia': 'utter_happy_odia',
                'affirm_odia': 'utter_affirm_odia',
                'goodbye_odia': 'utter_goodbye_odia',
                'iamabot_odia': 'utter_iamabot_odia',
                'Thanks_odia': 'utter_Thanks_odia',
                'out_of_scope_odia': 'utter_out_of_scope_odia',
            },
            
            # add more language codes and language-specific responses dictionaries here
        }
        
        # detect the language of the user input
        user_input = tracker.latest_message['text']
        lang, _ = langid.classify(user_input)
        
        # select the appropriate response based on the language and intent of the user input
        intent = tracker.latest_message['intent'].get('name')
        response_key = responses.get(lang, {}).get(intent, 'utter_default')
        dispatcher.utter_message(response_key)
        
        return []

