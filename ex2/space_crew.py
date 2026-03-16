from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_requirements(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        has_leadership = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        if self.duration_days > 365:
            experienced_count = sum(1
                                    for member in self.crew
                                    if member.years_experience >= 5
                                    )
            if experienced_count / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions require at least 50% "
                    "of crew to have 5+ years of experience"
                    )

        if not all(member.is_active for member in self.crew):
            raise ValueError(
                "All crew members assigned to a mission must be active"
                )

        return self


def wrong_data(my_crew: list[CrewMember]) -> None:
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Moon Base Setup",
            destination="Moon",
            launch_date=datetime(2025, 8, 15),
            duration_days=30,
            budget_millions=500.0,
            crew=[my_crew[1], my_crew[2]]
        )
        print(f"Mission: {invalid_mission.mission_name}")
        print(f"ID: {invalid_mission.mission_id}")
        print(f"Destination: {invalid_mission.destination}")
        print(f"Duration: {invalid_mission.duration_days} days")
        print(f"Budget: ${invalid_mission.budget_millions}M")
        print(f"Crew size: {len(invalid_mission.crew)}")
        print("Crew members:")
        for member in invalid_mission.crew:
            print(f"- {member.name}"
                  f" ({member.rank.value})"
                  f"- {member.specialization}")

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error.get("msg"))


def valid_data(my_crew: list[CrewMember]) -> None:
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_EUROPA",
            mission_name="Saturn Rings Research Mission",
            destination="Saturn Rings",
            launch_date=datetime(2024, 9, 18, 00, 00, 00),
            duration_days=602,
            crew=my_crew,
            budget_millions=1092.6
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name}"
                  f" ({member.rank.value})"
                  f"- {member.specialization}")
        print()
    except ValidationError as e:
        print(f"Unexpected error: {e}")


def get_crew() -> list[CrewMember]:
    captain = CrewMember(
        member_id="CM041", name="William Davis", rank=Rank.CAPTAIN,
        age=35, specialization="Medical Officer", years_experience=14
    )
    officier = CrewMember(
        member_id="CM046", name="Lisa Rodriguez", rank=Rank.OFFICER,
        age=30, specialization="Life Support", years_experience=12
    )
    cadet = CrewMember(
        member_id="CM047", name="Sarah Smith", rank=Rank.CADET,
        age=28, specialization="Pilot", years_experience=8
    )
    return [captain, officier, cadet]


def main() -> None:
    print("Space Mission Crew Validation\n")
    my_crew = get_crew()
    valid_data(my_crew)
    wrong_data(my_crew)


if __name__ == "__main__":
    main()
