from characters.character import Character


class CharacterFactory(object):
    def __init__(self, character_templates):
        self.character_templates = character_templates

    def build(self, uid):
        """
        Builds a characters instance from a template using the uid.
        :param uid: uid of the template to instanciate.
        :return: Built instance from template.
        """

        character_template = next((template for template in self.character_templates if template.uid == uid), None)
        if character_template:
            return self._create_instance_of_template(character_template)
        else:
            raise Exception("Could not find template for UID " + uid)

    @staticmethod
    def _create_instance_of_template(character_template):
        return Character(**character_template.__dict__)

        