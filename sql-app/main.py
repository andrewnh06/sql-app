import gui
import sql

if __name__ == "__main__":
    print(sql.login("newUser76", "Gamer7387"))

    loginScreen = gui.LoginScreen()
    loginScreen.mainloop()