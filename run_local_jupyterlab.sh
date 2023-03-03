#!/usr/bin/env bash
port=8999
jupyter lab --no-browser --port=${port} --ip 0 --NotebookApp.max_buffer_size=16000000000
# on local: port=8999; ssh -L 8999:localhost:${port} chois7@juno.mskcc.org
