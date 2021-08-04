# Harmful

def get_log_level(config_dict):
if 'ENABLE_LOGGING' in config_dict:
if config_dict['ENABLE_LOGGING'] != True:
return None
elif not 'DEFAULT_LOG_LEVEL' in config_dict:
return Noneelse:
return config_dict['DEFAULT_LOG_LEVEL']
else:
return None


# Idiomatic

def get_log_level(config_dict):
try:
if config_dict['ENABLE_LOGGING']:
return config_dict['DEFAULT_LOG_LEVEL']
except KeyError:
# if either value wasn't present, a
# KeyError will be raised, so
# return None
return None

