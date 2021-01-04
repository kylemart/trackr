import logging

from pushover import Client

from trackr.notifier.common import NotifierBase, NotifierFactory


logger = logging.getLogger(__name__)


@NotifierFactory.register('pushover')
class PushoverNotifier(NotifierBase):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_key = kwargs.get('api_key')
        self.user_key = kwargs.get('user_key')

    def execute(self, subject: str, content: str):
        logging.info(f'Notifying Pushover user: {self.user_key}')
        client = Client(self.user_key, api_token=self.api_key)
        client.send_message(content, title=subject)
