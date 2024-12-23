import toml

# config.toml dosyasını pythonun anlayacagı hale getiriyoruz
# loadConfig() fonksiyonu ile config.toml okunmus oluyor
def loadConfig(config_file):

    try:
        with open(config_file, "r") as f:
            config_data = toml.load(f)
        return config_data
    except Exception as e:
        print(f"Config load error: {e}")
        return None
