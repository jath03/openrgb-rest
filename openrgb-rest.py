from flask import Flask
from flask_restful import Resource, Api, reqparse
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
import dataclasses

app = Flask(__name__)
api = Api(app)
cli = OpenRGBClient(name="openrgb-rest")

parser = reqparse.RequestParser()
parser.add_argument('red', type=int)
parser.add_argument('green', type=int)
parser.add_argument('blue', type=int)
parser.add_argument('mode', type=int)


class Device(Resource):
    def get(self, device_id: int = -1):
        if device_id == -1:
            return [dataclasses.asdict(dev.data) for dev in cli.devices]
        else:
            return dataclasses.asdict(cli.devices[device_id].data)

    def put(self, device_id: int = -1):
        args = parser.parse_args()
        if device_id == -1:
            if any(c is None for c in (args['red'], args['blue'], args['green'])):
                return args, 400
            cli.set_color(RGBColor(args['red'], args['green'], args['blue']))
            return args, 201
        else:
            if args['mode'] is not None:
                cli.devices[device_id].set_mode(args['mode'])
                return args, 201
            elif all(c is not None for c in (args['red'], args['blue'], args['green'])):
                cli.devices[device_id].set_color(RGBColor(args['red'], args['green'], args['blue']))
                return args, 201
            else:
                return args, 400


api.add_resource(Device, '/', '/devices', '/devices/<int:device_id>')


if __name__ == "__main__":
    app.run(debug=True)
