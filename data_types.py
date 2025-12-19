from typing import TypedDict, List


class Link(TypedDict):
    title: str
    url: str | None


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


class HardSkill(TypedDict):
    title: str
    content: str


class Context(TypedDict):
    lang: str
    dir: str
    fullname: str
    role: str
    links: List[Link]
    about: str
    experiences: List[Experience]
    educations: List[Education]
    hard_skills: List[HardSkill]
    soft_skills: List[str]
