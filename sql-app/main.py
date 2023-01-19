import gui
import sql

if __name__ == "__main__":
    print(sql.get_top(2))

    loginScreen = gui.LoginScreen()
    loginScreen.mainloop()