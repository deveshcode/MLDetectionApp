# -*- coding: utf-8 -*-
"""config file for mldetect app"""
import configparser
import os

# pylint: disable=invalid-name
config_file = os.getenv(
    "MLOD_SETTINGS", "/home/pcadmin/personal/MLDetectionApp/FlaskApp_Backend/configs/local.ini"
)


# define config parser
config = configparser.ConfigParser(allow_no_value=True)
config.read(config_file)
