from rest_framework import serializers


class ModelHelpTextSerializer(serializers.Serializer):
    help_texts = serializers.SerializerMethodField(read_only=True)

    def get_help_texts(self, obj=None):
        model = self.context.get("model")
        help_texts = {}
        if model:
            for field in model._meta.get_fields():
                if hasattr(field, "help_text") and field.help_text:
                    help_texts[field.name] = field.help_text

        return help_texts
