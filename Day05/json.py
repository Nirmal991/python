def traverse_nested_config(config_dict, path_str, default=None):
    a = path_str.split(".")
    x= config_dict
    for i in a:
        try:
            x = x.get(i)
            print(f'{x}')
        except:
            return default
        print(i, x ,sep="=="*5)
    if x == None:
        return default
    else: 
        return x

def main():
    ...
    config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8080,
        "ssl": {
            "enabled": True,
            "cert_path": "/etc/ssl/certs"
        }
    },
    "database": "postgresql://localhost:5432"
}
    res = traverse_nested_config(config, "server.ssl.cert_path", "Good")
    print(res)

main()


