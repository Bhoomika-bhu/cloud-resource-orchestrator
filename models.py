from pydantic import BaseModel
from typing import List, Dict

class VM(BaseModel):
    id: str
    cpu: int
    memory: int
    status: str  # running / stopped

class Observation(BaseModel):
    vms: List[VM]
    pending_tasks: int
    cost: float

class Action(BaseModel):
    action_type: str  # create / delete / scale
    vm_id: str = ""
    cpu: int = 0
    memory: int = 0

class Reward(BaseModel):
    value: float