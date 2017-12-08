# Importing from ex_user_module_mm  and ex_admin_module_mm

from ex_user_module_mm import User
from ex_admin_module_mm import Admin

john = Admin("john", "starc", "n00b", 23, "new york",
             "john_noob@hotmail.com",
             ["can block users", "can delete posts"])

john.privileges.show_privileges()
