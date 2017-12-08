# Importing from ex_imported_admin_modules

from ex_imported_admin_modules import Admin

john = Admin("john", "starc", "n00b", 23, "new york",
             "john_noob@hotmail.com",
             ["can block users", "can delete posts"])

john.privileges.show_privileges()
 