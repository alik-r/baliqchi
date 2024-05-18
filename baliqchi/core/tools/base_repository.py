from abc import ABC


class BaseRepository(ABC):
    def __init__(self, model: object):
        self.model = model

    def get(self, **kwargs):
        return self.model.objects.get(**kwargs)

    def filter(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update(self, instance: object, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
