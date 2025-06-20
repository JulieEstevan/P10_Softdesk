from rest_framework import serializers

from .models import Comment, Contributor, Issue, Project
from authentication.models import User


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("name", "description", "project_type")


class ProjectDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    contributors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"
        read_only_fields = ("project", "added_on")

    def validate_user(self, value):
        if not User.objects.filter(pk=value.id).exists():
            raise serializers.ValidationError("The user does not exist")
        return value


class IssueSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ("project", "author")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("issue", "author")
