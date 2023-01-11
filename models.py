from pydantic import BaseModel, Field, validator


class Address(BaseModel):
    region: str
    city: str
    street_type: str
    street: str
    house_type: str
    house: str
    value: str
    lat: float
    lng: float


class Salary(BaseModel):
    from_: int = Field(alias='from')
    to: int
    currency: str
    gross: bool


class Contacts(BaseModel):
    fullName: str
    phone: str
    email: str

    '''тривиальная проверка почты'''

    @validator('email')
    def at_in_email(cls, v: str) -> str:
        if not '@' in v:
            raise ValueError('Email некорректный')
        return v


class CandidateInfo(BaseModel):
    description: str
    employment: str
    address: Address
    name: str
    salary: Salary
    contacts: Contacts


class Experience(BaseModel):
    id = "noMatter"


class ChangedCoordinates(BaseModel):
    latitude: float
    longitude: float


class Phone(BaseModel):
    city: str
    country: str
    number: str


class ChangedContacts(BaseModel):
    email: str
    name: str
    phone: Phone


class ChangedSalary(BaseModel):
    from_: int = Field(alias='from')
    to: int


class Schedule(BaseModel):
    id: str


class ResultInfo(BaseModel):
    address: str
    allow_messages = True
    billing_type = "packageOrSingle"
    business_area = 1
    contacts: ChangedContacts
    coordinates: ChangedCoordinates
    description: str
    experience: Experience
    html_tags = True
    image_url = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    name: str
    salary: int
    salary_range: ChangedSalary
    schedule: Schedule
