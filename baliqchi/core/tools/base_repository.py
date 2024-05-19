from abc import ABC


class BaseRepository(ABC):
    """
    Abstract base class for repository implementations.

    Provides common CRUD methods for interacting with models.

    Attributes:
    - model: Model class associated with the repository.
    """
    def __init__(self, model: object):
        """
        Initializes the repository with the specified model.

        Parameters:
        - model: Model class associated with the repository.
        """
        self.model = model

    def get(self, **kwargs):
        """
        Retrieves a single object from the database based on the provided filter parameters.

        Parameters:
        - kwargs: Filter parameters to query the object.

        Returns:
        - Object: Retrieved object from the database.
        """
        return self.model.objects.get(**kwargs)

    def filter(self, **kwargs):
        """
        Retrieves a list of objects from the database based on the provided filter parameters.

        Parameters:
        - kwargs: Filter parameters to query the objects.

        Returns:
        - QuerySet: QuerySet containing the retrieved objects.
        """
        return self.model.objects.filter(**kwargs)

    def create(self, **kwargs):
        """
        Creates a new object in the database with the provided data.

        Parameters:
        - kwargs: Data for creating the object.

        Returns:
        - Object: Created object.
        """
        return self.model.objects.create(**kwargs)

    def update(self, instance: object, **kwargs):
        """
        Updates the specified object with the provided data.

        Parameters:
        - instance: Object to be updated.
        - kwargs: Data for updating the object.

        Returns:
        - Object: Updated object.
        """
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
