from rest_framework.generics import GenericAPIView as APIView

from .serializer import MailSerializer


class SendEmailView(APIView):
    serializer_class = MailSerializer

    def post(self, *args, **kwargs):
        pass
