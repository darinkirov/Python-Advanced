class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

while True:
    email = input("Enter an email or 'End' to stop: ")
    if email == "End":
        break

    try:
        name, domain = email.split("@")
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")
        if domain not in [".com", ".bg", ".net", ".org"]:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
        print("Email is valid")
    except NameTooShortError as e:
        print(e)
    except MustContainAtSymbolError as e:
        print(e)
    except InvalidDomainError as e:
        print(e)
