import logging
from flask import Flask
import psutil
from typing import Iterable
from opentelemetry import trace, metrics
from opentelemetry.metrics import CallbackOptions,Observation
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from random import randint
#collector endpoint
endpoint = "http://10.111.0.123:55680"

resource = Resource.create(attributes={SERVICE_NAME: "python-backend"})

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# Trace
tracer_provider = TracerProvider(resource=resource)
#export to collector
tracer_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
# export to console
# tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)

# Metrics
#export to collector
reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(endpoint=endpoint)
)
# export to console
# reader = PeriodicExportingMetricReader(ConsoleMetricExporter()) 
Metrics_provider = MeterProvider(resource=resource, metric_readers=[reader])
meter = metrics.get_meter(__name__)

def get_cpu_usage(options: CallbackOptions) -> Iterable[Observation]:
    cpu_usage_percent = psutil.cpu_percent(interval=None)
    print("cpu_usage_percent")
    print(cpu_usage_percent )
    observation = Observation(value=cpu_usage_percent)
    print(observation)
    return [observation]

# create a metrics that collect cpu usage
cpu_usage_metric = meter.create_observable_gauge(
    name="cpu_usage",
    description="CPU Usage",
    unit="percent",
    callbacks=[get_cpu_usage]
)

# # Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)
metrics.set_meter_provider(Metrics_provider)

@app.route("/rolldice")
def roll_dice():
    with tracer.start_as_current_span("dice") as dicespan:
        dicespan.add_event("start roll")
        return hello_world(str(do_roll()))

def do_roll():
    with tracer.start_as_current_span("do_roll") as rollspan: #naming spqn = do_roll
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        rollspan.add_event("rolled !")
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": res})
        return res
        
def hello_world(number):
    number=int(number)
    with tracer.start_as_current_span("show_number") as span:
        if 0<number<4:
            span.add_event("To low")
            return "<h1> To low </h1>"
        elif 3<number<7:
            span.add_event("To High!")
            return "<h1> To High </h1>"

# Webapp
@app.route("/HI")
def HI():
    return "HI"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)

tracer = trace.get_tracer_provider().get_tracer("python-backend.trace")
meter = metrics.get_meter_provider().get_meter("python-backend.metric")