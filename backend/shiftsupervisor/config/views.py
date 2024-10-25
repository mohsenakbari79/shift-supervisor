from rest_framework import viewsets, status
from rest_framework.response import Response

from config.serializers import ModelHelpTextSerializer


class HelpTextViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ModelHelpTextSerializer

    def get_queryset(self):
        return [self.model]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["model"] = self.model  # ارسال مدل به context
        return context

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
