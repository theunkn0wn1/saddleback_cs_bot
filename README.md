# What is this?
This is a `discord.py` implemented discord bot that provides small 
role-management services for the student-operated Saddleback CS Discord.

Nothing special.


## Installation
```shell
git clone https://github.com/theunkn0wn1/saddleback_cs_bot
pip install ./saddleback_cs_bot
```

## Configuration
The program won't start without a valid configuration file.

The config is split into three logical chunks:

### Root

- `command-prefix` - prefix the bot will treat when scanning for commands
- `guild` Legacy, unused.
- `secrets` Secrets configuration, see [below](#secrets)
- `rolls` list of rolls this bot manages, and their aliases. see [below](#rolls)
### Secrets

- `token` - discord t0k3n.

# Rolls

Each entry in `Rolls` consists of two parts:

- `name` - this corresponds to the name of the role as it is in Discord
- `aliases` this corresponds to the list of strings that are translated to the `name` at runtime. 
  Note: no sanity checks are done to prevent conflicts.
  
## Adding new rolls 
Once you have a valid configuration, you can add more roles by using the helper utility.
 Example invocation
```shell

$ python -m discord_university.add_roll production.toml --name CIMP8A -a python --alias cimp8a

```

**note::** you will need to restart the bot since I haven't implemented a in-flight rehashing mechanism yet.