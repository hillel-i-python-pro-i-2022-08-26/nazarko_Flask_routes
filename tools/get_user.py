from faker import Faker

fake = Faker()


def User():
    name = fake.first_name()
    email = fake.domain_name()
    return f"{name} {email}"
