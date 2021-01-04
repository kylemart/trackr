import logging

from abc import ABCMeta, abstractmethod


logger = logging.getLogger(__name__)


class NotifierBase(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        pass

    @classmethod
    def from_dict(cls, args: dict):
        return cls(**args)

    @abstractmethod
    def execute(self, subject: str, content: str):
        pass


class NotifierFactory:

    _registry = {}

    @classmethod
    def register(cls, name: str):

        def inner_wrapper(wrapped_class):
            if name in cls._registry:
                logger.warning('Replacing notifier %s in the registry', name)
            cls._registry[name] = wrapped_class
            return wrapped_class

        return inner_wrapper

    @classmethod
    def get_class(cls, name: str):
        if name not in cls._registry:
            logger.warning('Notifier %s is not in the registry', name)
            return None

        notifier_class = cls._registry[name]
        return notifier_class
