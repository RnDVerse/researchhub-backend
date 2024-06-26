from django.db.models import Q
from rest_framework.serializers import SerializerMethodField

from citation.models import CitationProject
from researchhub_access_group.constants import EDITOR, VIEWER
from user.related_models.user_model import User
from user.serializers import MinimalUserSerializer
from utils.serializers import DefaultAuthenticatedSerializer


class ParentSerializer(DefaultAuthenticatedSerializer):
    class Meta:
        model = CitationProject
        fields = "__all__"


class CitationProjectSerializer(DefaultAuthenticatedSerializer):
    children = SerializerMethodField()
    parent_data = SerializerMethodField(read_only=True)
    collaborators = SerializerMethodField(read_only=True)
    current_user_is_admin = SerializerMethodField(read_only=True)

    class Meta:
        model = CitationProject
        fields = "__all__"

    """ ----- Django Method Overrides -----"""

    """ ----- Serializer Methods -----"""

    def get_parent_data(self, project_instance):
        if project_instance.parent:
            return ParentSerializer(project_instance.parent).data

    def get_current_user_is_admin(self, project_instance):
        current_user = self.context.get("request").user
        return project_instance.get_is_user_admin(current_user)

    def get_collaborators(self, project):
        editor_ids = project.permissions.filter(access_type=EDITOR).values_list("user")
        viwer_ids = project.permissions.filter(access_type=VIEWER).values_list("user")
        return {
            "editors": MinimalUserSerializer(
                User.objects.filter(id__in=editor_ids), many=True
            ).data,
            "viewers": MinimalUserSerializer(
                User.objects.filter(id__in=viwer_ids), many=True
            ).data,
        }

    def get_current_user_has_access(self, project_instance):
        current_user = self.context.get("request").user
        return project_instance.get_user_has_access(current_user)

    def get_children(self, project_instance):
        return CitationProjectSerializer(
            context=self.context,
            instance=project_instance.children.filter(
                Q(is_public=True)
                | Q(
                    is_public=False,
                    permissions__user=self.context.get("request").user,
                )
            ).distinct(),
            many=True,
        ).data

    """ ----- Private Methods -----"""
