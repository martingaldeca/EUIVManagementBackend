from django.db import models
from logging import getLogger
from djchoices import DjangoChoices, ChoiceItem
from django.contrib.auth.models import AbstractUser
from EUIVSaveGame.models import EuIVSaveGame
from EUIVCountries.models import EuIVCountry

from EUIVManagement.helpers import EuIVModel

logger = getLogger(__name__)


class EuIVUserTypes(DjangoChoices):
    """
    Allowed user types for users in the game
    """
    host = ChoiceItem(0)
    admin = ChoiceItem(1)
    player = ChoiceItem(2)


class EuIVUser(AbstractUser, EuIVModel):
    """
    Model for add extra parameters to the users in the platform
    """

    # Common fields for users
    user_type = models.IntegerField(
        choices=EuIVUserTypes.choices, default=EuIVUserTypes.player, null=True, blank=True, help_text="Select one of the user types for the platform.", verbose_name="User type"
    )

    # EuIV specific fields
    user_active_games = models.ManyToManyField(
        EuIVSaveGame, related_name='active_games', verbose_name='User active games', help_text='All the games active where the user is playing.', through='EuIVUserActiveGames'
    )

    def __str__(self):
        return f'{self.username}'

    def change_user_type(self, new_user_type: int = 0) -> None:
        """
        Function to update the user type
        :param new_user_type:
        :return:
        """
        logger.info(f"The user {self}, will change the user type from '{EuIVUserTypes.attributes[self.user_type]}' to '{EuIVUserTypes.attributes[new_user_type]}'.")
        self.user_type = new_user_type
        self.save()


class EuIVUserActiveGames(EuIVModel):
    user = models.ForeignKey(EuIVUser, blank=True, null=True, db_index=True, verbose_name='User', help_text='User associated to the save game', on_delete=models.CASCADE)
    save_game = models.ForeignKey(EuIVSaveGame, blank=True, null=True, db_index=True, verbose_name='Save game', help_text='The Save game associated to the user.', on_delete=models.CASCADE)
    country = models.ForeignKey(EuIVCountry, blank=True, null=True, db_index=True, verbose_name='Country', help_text='Country used by the user in the save game.', on_delete=models.CASCADE)
