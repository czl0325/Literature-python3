from app import create_app

app = create_app('dev_config')

if __name__ == '__main__':
    app.run()
