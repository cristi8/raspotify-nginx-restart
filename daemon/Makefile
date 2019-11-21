
install:
	sudo cp raspotify-nginx-restart.py /usr/sbin/
	sudo cp raspotify-nginx-restart.service /lib/systemd/system/

	sudo chmod +x /usr/sbin/raspotify-nginx-restart.py
	sudo systemctl enable raspotify-nginx-restart
	sudo systemctl start raspotify-nginx-restart


uninstall:
	sudo systemctl disable raspotify-nginx-restart
	sudo systemctl stop raspotify-nginx-restart
	sudo rm -f \
		/usr/sbin/raspotify-nginx-restart.py \
		/lib/systemd/system/raspotify-nginx-restart.service \
		/etc/restart-raspotify
