from typing import TypedDict


class Link(TypedDict):
    title: str
    url: str | None
    icon: str | None


class Experience(TypedDict):
    title: str
    sub_title: str | None
    role: str | None
    description: str
    stack: str | None
    domain: str | None


class Education(TypedDict):
    field: str
    location: str
    degree: str
    date: str


class Skill(TypedDict):
    name: str
    icon: str | None


class Context(TypedDict):
    lang: str
    dir: str
    fullname: str
    role: str
    links: list[Link]
    about: str
    experiences: list[Experience]
    educations: list[Education]
    skills: list[Skill]
