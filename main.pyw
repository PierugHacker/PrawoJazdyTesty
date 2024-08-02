from engine import create_app
import webview
import multiprocessing

app = create_app()

def engineThread():
    global app
    app.run()

if __name__ == '__main__':
    th = multiprocessing.Process(target=engineThread)
    th.start()
    webview.create_window('Egzamin teoretyczny na prawo jazdy', 'http://localhost:5000', width=1280, height=720)
    webview.start()
    th.terminate()