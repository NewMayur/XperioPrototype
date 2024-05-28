from pydantic import BaseModel, Field

class Device(BaseModel):
    id: int
    name: str
    status: str = Field(default="off", description="The current status of the device")

# Learning Comment:
# Pydantic's BaseModel is used to define data structures with type annotations.
# This ensures that each device has an id, a name, and a status with a default value of "off".
