# OpenRGB-REST

A basic [flask-restful](https://flask-restful.readthedocs.io/en/latest/) REST API for [OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB) using my [openrgb-python](https://github.com/jath03/openrgb-python) SDK client.

## Endpoints

GET `/`,`/devices` - Gets the data for all OpenRGB devices
<details>
<summary>Example Response</summary>

```json
[
    {
        "name": "ASUS Aura DRAM",
        "metadata": {
            "description": "ASUS Aura SMBus Device",
            "version": "DIMM_LED-0103",
            "serial": "",
            "location": "/dev/i2c-0, address 0x73"
        },
        "device_type": 1,
        "leds": [
            {
                "name": "DRAM LED 1",
                "value": 0
            },
            {
                "name": "DRAM LED 2",
                "value": 1
            },
            {
                "name": "DRAM LED 3",
                "value": 2
            },
            {
                "name": "DRAM LED 4",
                "value": 3
            },
            {
                "name": "DRAM LED 5",
                "value": 4
            }
        ],
        "zones": [
            {
                "name": "DRAM",
                "zone_type": 1,
                "leds_min": 5,
                "leds_max": 5,
                "num_leds": 5,
                "mat_height": 0,
                "mat_width": 0,
                "matrix_map": [
                    []
                ],
                "leds": [
                    {
                        "name": "DRAM LED 1",
                        "value": 0
                    },
                    {
                        "name": "DRAM LED 2",
                        "value": 1
                    },
                    {
                        "name": "DRAM LED 3",
                        "value": 2
                    },
                    {
                        "name": "DRAM LED 4",
                        "value": 3
                    },
                    {
                        "name": "DRAM LED 5",
                        "value": 4
                    }
                ],
                "colors": [
                    {
                        "red": 100,
                        "green": 100,
                        "blue": 100
                    },
                    {
                        "red": 100,
                        "green": 100,
                        "blue": 100
                    },
                    {
                        "red": 100,
                        "green": 100,
                        "blue": 100
                    },
                    {
                        "red": 100,
                        "green": 100,
                        "blue": 100
                    },
                    {
                        "red": 100,
                        "green": 100,
                        "blue": 100
                    }
                ],
                "start_idx": null
            }
        ],
        "modes": [
            {
                "id": 0,
                "name": "Direct",
                "value": 65535,
                "flags": 32,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 1,
                "name": "Off",
                "value": 0,
                "flags": 0,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 0,
                "colors": []
            },
            {
                "id": 2,
                "name": "Static",
                "value": 1,
                "flags": 32,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 3,
                "name": "Breathing",
                "value": 2,
                "flags": 160,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 4,
                "name": "Flashing",
                "value": 3,
                "flags": 32,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 5,
                "name": "Spectrum Cycle",
                "value": 4,
                "flags": 0,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 0,
                "colors": []
            },
            {
                "id": 6,
                "name": "Rainbow",
                "value": 5,
                "flags": 0,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 0,
                "colors": []
            },
            {
                "id": 7,
                "name": "Chase Fade",
                "value": 7,
                "flags": 160,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 8,
                "name": "Chase",
                "value": 9,
                "flags": 160,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 9,
                "name": "Random Flicker",
                "value": 13,
                "flags": 0,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 0,
                "colors": []
            }
        ],
        "colors": [
            {
                "red": 100,
                "green": 100,
                "blue": 100
            },
            {
                "red": 100,
                "green": 100,
                "blue": 100
            },
            {
                "red": 100,
                "green": 100,
                "blue": 100
            },
            {
                "red": 100,
                "green": 100,
                "blue": 100
            },
            {
                "red": 100,
                "green": 100,
                "blue": 100
            }
        ],
        "active_mode": 0
    },
    {
        "name": "Gigabyte GPU",
        "metadata": {
            "description": "RGB Fusion GPU",
            "version": "",
            "serial": "",
            "location": "/dev/i2c-4, address 0x47"
        },
        "device_type": 2,
        "leds": [
            {
                "name": "GPU LED",
                "value": 0
            }
        ],
        "zones": [
            {
                "name": "GPU Zone",
                "zone_type": 0,
                "leds_min": 1,
                "leds_max": 1,
                "num_leds": 1,
                "mat_height": 0,
                "mat_width": 0,
                "matrix_map": [
                    []
                ],
                "leds": [],
                "colors": [],
                "start_idx": null
            }
        ],
        "modes": [
            {
                "id": 0,
                "name": "Static",
                "value": 1,
                "flags": 32,
                "speed_min": null,
                "speed_max": null,
                "colors_min": null,
                "colors_max": null,
                "speed": null,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 1,
                "name": "Breathing",
                "value": 2,
                "flags": 33,
                "speed_min": 0,
                "speed_max": 9,
                "colors_min": null,
                "colors_max": null,
                "speed": 5,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 2,
                "name": "Flashing",
                "value": 4,
                "flags": 33,
                "speed_min": 0,
                "speed_max": 9,
                "colors_min": null,
                "colors_max": null,
                "speed": 5,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 3,
                "name": "Dual Flashing",
                "value": 8,
                "flags": 33,
                "speed_min": 0,
                "speed_max": 9,
                "colors_min": null,
                "colors_max": null,
                "speed": 5,
                "direction": null,
                "color_mode": 1,
                "colors": []
            },
            {
                "id": 4,
                "name": "Spectrum Cycle",
                "value": 17,
                "flags": 1,
                "speed_min": 0,
                "speed_max": 9,
                "colors_min": null,
                "colors_max": null,
                "speed": 5,
                "direction": null,
                "color_mode": 0,
                "colors": []
            }
        ],
        "colors": [
            {
                "red": 255,
                "green": 255,
                "blue": 255
            }
        ],
        "active_mode": 0
    }
]
```
</details>  

---

PUT `/`, `/devices` - Sets the Color of all of your devices
<details>
<summary>Example Request data</summary>

```json
{
    "red": 0,
    "green": 255,
    "blue": 0
}
```
</details>

---

GET `/devices/<device_id>` - Gets the data for a specified device
<details>
<summary>Example Response</summary>

```json
{
    "name": "Gigabyte GPU",
    "metadata": {
        "description": "RGB Fusion GPU",
        "version": "",
        "serial": "",
        "location": "/dev/i2c-4, address 0x47"
    },
    "device_type": 2,
    "leds": [
        {
            "name": "GPU LED",
            "value": 0
        }
    ],
    "zones": [
        {
            "name": "GPU Zone",
            "zone_type": 0,
            "leds_min": 1,
            "leds_max": 1,
            "num_leds": 1,
            "mat_height": 0,
            "mat_width": 0,
            "matrix_map": [
                []
            ],
            "leds": [],
            "colors": [],
            "start_idx": null
        }
    ],
    "modes": [
        {
            "id": 0,
            "name": "Static",
            "value": 1,
            "flags": 32,
            "speed_min": null,
            "speed_max": null,
            "colors_min": null,
            "colors_max": null,
            "speed": null,
            "direction": null,
            "color_mode": 1,
            "colors": []
        },
        {
            "id": 1,
            "name": "Breathing",
            "value": 2,
            "flags": 33,
            "speed_min": 0,
            "speed_max": 9,
            "colors_min": null,
            "colors_max": null,
            "speed": 5,
            "direction": null,
            "color_mode": 1,
            "colors": []
        },
        {
            "id": 2,
            "name": "Flashing",
            "value": 4,
            "flags": 33,
            "speed_min": 0,
            "speed_max": 9,
            "colors_min": null,
            "colors_max": null,
            "speed": 5,
            "direction": null,
            "color_mode": 1,
            "colors": []
        },
        {
            "id": 3,
            "name": "Dual Flashing",
            "value": 8,
            "flags": 33,
            "speed_min": 0,
            "speed_max": 9,
            "colors_min": null,
            "colors_max": null,
            "speed": 5,
            "direction": null,
            "color_mode": 1,
            "colors": []
        },
        {
            "id": 4,
            "name": "Spectrum Cycle",
            "value": 17,
            "flags": 1,
            "speed_min": 0,
            "speed_max": 9,
            "colors_min": null,
            "colors_max": null,
            "speed": 5,
            "direction": null,
            "color_mode": 0,
            "colors": []
        }
    ],
    "colors": [
        {
            "red": 255,
            "green": 255,
            "blue": 255
        }
    ],
    "active_mode": 0

}
```
</details>

---

PUT `/devices/<device_id>` - Sets the Color or Mode of a specified device
<details>
<summary>Example Request Data</summary>

```json
{
    "red": 255,
    "green": 0,
    "blue": 0
}
```
or

```json
{
    "mode": 2
}
```
Note - Attempting to set both color and mode in one request will only affect the mode.
</details>
