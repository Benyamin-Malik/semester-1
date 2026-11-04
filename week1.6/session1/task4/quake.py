# Week 1.6, Session 1: Task 4

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Quake:
 """
    Details of a single earthquake.
    """

when: datetime
longitude: float
atitude: float
depth: float
magnitude: float
