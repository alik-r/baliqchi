from core.models import Incident
from core.tools import BaseRepository


class IncidentRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Incident)


incident_repository = IncidentRepository()
