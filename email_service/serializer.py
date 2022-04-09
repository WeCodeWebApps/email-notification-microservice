from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    subject = serializers.CharField(allow_null=True)
    template_name = serializers.CharField()
    args = serializers.JSONField()
    email = serializers.EmailField()

    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

    def send_email(self):
        pass
