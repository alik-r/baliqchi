from core.models import Incident
from core.tools import BaseRepository


class AlertRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Incident)


alert_repository = AlertRepository()
