
from dataclasses import dataclass
from datetime import datetime
from django.utils.translation import gettext as _
@dataclass
class Section:
    id: int
    name: str
    type: str
    description: str
    start_time: datetime.time
    end_time: datetime.time
    has_break: bool
    break_count: int
    break_duration: datetime.time
    days: list[str] = None
    
    
    def __post_init__(self):
        if not self.name:
            raise ValueError(_("Section name cannot be empty"))
        if not self.type:
            raise ValueError(_("Section type cannot be empty"))
        if not self.start_time:
            raise ValueError(_("Start date cannot be empty"))
        if not self.end_time:
            raise ValueError(_("End date cannot be empty"))
        if self.break_count < 0:
            raise ValueError(_("Break count cannot be negative"))
        if self.break_duration < 0:
            raise ValueError(_("Break duration cannot be negative"))
        
        if self.start_time >= self.end_time:
            raise ValueError(_("Start date must be before end date"))
        
        if self.break_duration > (self.end_time.hour * 60 + self.end_time.minute -
                                  (self.start_time.hour * 60 + self.start_time.minute)):
            raise ValueError(_("Break duration cannot exceed the section duration"))
