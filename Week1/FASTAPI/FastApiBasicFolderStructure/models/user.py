from pydantic import BaseModal
from typing import Optional

class User(BaseModal):
    name: str
    email: str
    age: Optional[int] = None     # This modal is the None By default 