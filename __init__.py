from mycroft import MycroftSkill, intent_file_handler


class DomoticzSwitch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('switch.domoticz.intent')
    def handle_switch_domoticz(self, message):
        self.speak_dialog('switch.domoticz')


def create_skill():
    return DomoticzSwitch()

