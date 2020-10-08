def get_emails():
    email = input("Email address: ")
    email_list = [email]
    while email != 'q':
        email = input("Email address: ")
        if email != 'q':
            email_list.append(email)
    return email_list

def get_names_and_domains(email_list):
    name_and_domains_list = []
    for email in email_list:
        split_email = email.split('@')
        tuple_email = tuple(split_email)
        name_and_domains_list.append(tuple_email)
    return name_and_domains_list 


email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)