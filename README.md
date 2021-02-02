# BRC Automad Installer

Project to install and customise Automad to create BRC info website using automad

## Installation and Running

1. Download the code from github

```bash
git clone https://github.com/LCBRU/brc_automad_installer.git
```

2. Install PHP requirements

 - PHP GD

3. Install Python Requirements

  1. Create the python virtual environmenmt by running the command: `python3 -m venv venv`
  2. Activate the virtual environment: `. venv/bin/activate`
  3. Install the requirements `pip install -r requirements.txt`

4. Amend the parameters

  1. Copy the file `example.env` to `.env`.
  2. Amend the file to fill in the correct values for the `WWW_DIR` and `HTTP_DIR`.

## Deployment

To deploy the app, run the command:

```bash
install.py
```

## Site Management

To edit the site, use the Dashboard at /dashboard.

## User Management

The first time that you access the dashboard, you will be asked to create a user.

New users can then be added through the dashbaord.

