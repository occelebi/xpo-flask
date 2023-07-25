from flask import Flask

#from storage.bucket import bucket_blueprint
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__, static_url_path="", static_folder="../static")
app.config.from_object(__name__)
app.config["APPLICATION_ROOT"] = "/api"
#app.register_blueprint(bucket_blueprint, url_prefix="/api")
metrics = PrometheusMetrics(app)
