from rest_framework import serializers

from journal.models import Journal, Page
from users.models import User


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ["id", "name", "date", "shared"]

    def create(self, validated_data):
        """ Create a new journal. """
        name = validated_data.get('name')
        date = validated_data.get('date')
        user = User.objects.get(email=validated_data.get('user'))

        journal = Journal(
            name=name,
            date=date,
            user=user
        )
        journal.save()

        return journal


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ["id", "name", "text", "journal"]

    def create(self, validated_data):
        """ Create a new page. """
        name = validated_data.get('name')
        text = validated_data.get('text')
        journal = Journal.objects.get(id=validated_data.get('journal'))
        user = User.objects.get(email=validated_data.get('user'))
        if journal.user != user:
            raise PermissionError('You are not the author of the journal.')

        page = Page(
            name=name,
            text=text,
            journal=journal
        )
        page.save()

        return page
