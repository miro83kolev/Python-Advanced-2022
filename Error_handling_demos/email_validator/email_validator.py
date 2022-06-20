from custom_exceptions import MustContainAtSymbolError, NameToShortNameError, InvalidDomainError

valid_domains = {'.com', '.org', '.net', '.bg'}
while True:
    line = input()

    if line == "End":
        break

    email = line

    email_parts = email.split('@')

    if len(email_parts) != 2:
        raise MustContainAtSymbolError('Email must contain @')

    name, domain_name = email_parts

    if len(name) <= 4:
        raise NameToShortNameError('Name must be more than 4 characters')


    domain = f".{domain_name.split('.')[-1]}"

    if domain not in valid_domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    print('Email is valid')