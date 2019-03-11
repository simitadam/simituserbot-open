# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import os
import sys
from uniborg import Uniborg

logging.basicConfig(level=logging.INFO)

# the secret configuration specific things
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from sample_config import Config
else:
    if os.path.exists("config.py"):
        from config import Config
    else:
        logging.warning("No config.py Found!")
        logging.info("[BETA] Trying to create config.py")
        with open("app.json") as auto_json_file:
            json_data = json.load(json_file)
            app_variables = json_data["env"]
            logging.info(app_variables)
            logging.info("Need to finish this, but not now!")
        logging.info("Please run the command, again, after creating config.py similar to README.md")
        sys.exit(1)


if len(sys.argv) == 2:
    session_name = str(sys.argv[1])
    borg = Uniborg(
        session_name,
        plugin_path="stdplugins",
        connection_retries=None,
        api_config=Config,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH
    )
    borg.run_until_disconnected()
else:
    logging.error("USAGE EXAMPLE:\n"
                  "python3 -m stdborg <SESSION_NAME>"
                  "\n 👆👆 Please follow the above format to run your userbot."
                  "\n Bot quitting.")
