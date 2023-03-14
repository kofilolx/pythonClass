class User:
    def __init__(self, first_name, last_name, mobile, o_address):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.o_address = o_address
        self.username = ''
        self.password = ''
        self.login_attempts = 0

    def describe_user(self):
        print(f"first name: {self.first_name}"
              f"\nlast name: {self.last_name}"
              f"\nmobile number:{self.mobile}"
              f"\nOffice Address:{self.o_address}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, welcome to wickStudios.")

    def login_attempt(self):
        self.password = ''
        self.username = ''
        count = self.login_attempts
        while count < 3:
            self.username = input("Enter Cred: ")
            self.password = input("Enter Password: ")
            if self.username == "admin" and self.password == "admin":
                print(f"Access granted")
                break
            else:
                print('Access denied, Try again.')
                count += 1

    def increment_login_attempts(self, new_user):
        self.login_attempts += new_user
        print(f"Total attempts {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Attempt reset: {self.login_attempts}")


profile = User("Jonathan", "Kotey", '021548788', 'GA-842-415')
print(f"{profile.o_address} is {profile.last_name}'s office address")
profile.describe_user()
profile.greet_user()

profile = User("Gabriel", "Kotei", '02000008788', 'GA-342-415')
profile.describe_user()
profile.greet_user()
profile.login_attempt()
profile.increment_login_attempts(3)
profile.increment_login_attempts(3)
profile.increment_login_attempts(30)
profile.reset_login_attempts()
profile.increment_login_attempts(3)
profile.reset_login_attempts()
