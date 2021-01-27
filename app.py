from interface import DCCUI, generate_app

if __name__ == '__main__':
    app = generate_app()
    ui = DCCUI()
    ui.resize(600, 400)
    ui.show()
    exit(app.exec_())
