from firebase_auth_ui import draw_ui
import home
import joblib

firebase_config = joblib.load("firebase_config.priom")
draw_ui.run_authentication(firebase_config, home.call)


