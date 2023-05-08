# pi-garage-controller
Raspberry Pi Garage Controller

## Run Options
- **docker** - `docker-compose.yml` can be found in repo; image will only work for armv6 device
- **linux service** - mv `garage.service.txt` file to `garage.service` and place in `/etc/system/systemd`; you will need `gunicorn` and `flask` installed (recommended for pi zeros)
  * `sudo apt install gunicorn`
  * `pip3 install gunicorn` - install with sudo if running service as sudo user (service file default)
- **from cli** - run `./start_app.sh`
