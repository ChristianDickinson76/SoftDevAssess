user_data = {
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "phone": "07123456789",
    "national_id": "AB123456C"
}

def mask_email(email):
    local, domain = email.split("@")
    return local[0] + "***@" + domain

def mask_phone(phone):
    return "***-***-" + phone[-4:]

def mask_national_id(nid):
    return "***" + nid[-3:]   # show only last 3 characters

protected_data = {
    "name": user_data["name"],  # name can stay visible
    "email": mask_email(user_data["email"]),
    "phone": mask_phone(user_data["phone"]),
    "national_id": mask_national_id(user_data["national_id"])
}

print("Protected User Data:")
for key, value in protected_data.items():
    print(f"{key}: {value}")