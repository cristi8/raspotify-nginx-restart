# raspotify-nginx-restart

This project addresses an issue from `librespot` that sometimes loses authentication and needs to be restarted in order to re-authenticate.

I am using `raspotify` on a dedicated raspberry pi and needed a way to easily restart raspotify when it loses connection, without ssh.


So I can now do a `POST` request to `/restart-raspotify` on my raspotify device and it will restart (and re-authenticate to spotify).

## Components
- Daemon (as root) that actually restarts the `raspotify` service
- Nginx small lua script that writes `1` to a file (/etc/restart-raspotify)


## Dependencies
- `python3`
- `nginx`
- `nginx-extras`   (for the lua script)

## Install
Get the files with either:
```bash
git clone https://github.com/cristi8/raspotify-nginx-restart.git
```
or
```bash
wget [TODO]
```


To install the daemon:
```bash
cd daemon
make install
```

To install the nginx part, copy/edit this location block to the nginx site config that you want to use:


```

    location /restart-raspotify {
        ## Optional: Set up nginx access control like allow only some source ip addresses or set up basicauth

        ## Optional: Only allow POST requests
        # if ( $request_method != POST ) { return 405; }

        default_type application/json;
        content_by_lua '
            local file = assert(io.open("/etc/restart-raspotify", "w"), "Inaccessible file")
            file:write("1")
            file:close()
            ngx.say("{\\"success\\": 1}")
        ';
    }

```




## Uninstall
To uninstall the daemon:

```bash
cd daemon
make uninstall
```

And then remove the /restart-raspotify location from nginx config.
