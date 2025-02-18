# This is a sample Python script.
import argparse
import json
import logging
import os
import sys


def extract_cert(cosmos_config: str, cert_path: str, key_path: str) -> None:
    with open(cosmos_config, "r") as cosmos_file:
        cosmos_json = json.loads(cosmos_file.read())

    cert = cosmos_json["HTTPConfig"]["TLSCert"]
    key = cosmos_json["HTTPConfig"]["TLSKey"]

    with open(key_path, "w") as file:
        file.write(key)

    with open(cert_path, "w") as file:
        file.write(cert)

    os.sync()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    argp = argparse.ArgumentParser()

    argp.add_argument("-c", "--config", required=False, help='Path to cosmos config', type=str,
                      default="/var/lib/cosmos/cosmos.config.json")
    argp.add_argument("-ok", "--out-key", required=False, help='Path to save private key', type=str,
                      default="/usr/adguardhome/cert/key.txt")
    argp.add_argument("-oc", "--out-cert", required=False, help='Path to save cert', type=str,
                      default="/usr/adguardhome/cert/cert.txt")

    param = argp.parse_args()
    extract_cert(cosmos_config=param.config, cert_path=param.out_cert, key_path=param.out_key)
