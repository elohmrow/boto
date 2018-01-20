#!/bin/bash

# make sure we have the name of a process to make a plugin for:
if [ -z "$1" ]
then
    echo "you need to tell me what process to create a plugin for - try again."
    exit;
fi

# check if a plugin with this name already esists:
if [ -e /usr/share/munin/plugins/$1 ]
then
    echo "plugin already exists - try again."
    exit;
fi

# write the plugin:
cat > $1 << EOF
#!/bin/bash

case $1 in
   config)
        cat <<'EOM'
graph_title process running
graph_vlabel running
running.label running
EOM
        exit 0;;
esac

result=\$(pgrep -c $1)
echo "running" \$result
EOF

# change ownership and permissions:
sudo chmod 755 $1
sudo chown root:root $1

# put the plugin where it goes:
sudo mv $1 /usr/share/munin/plugins/
sudo ln -s /usr/share/munin/plugins/$1 /etc/munin/plugins

# restart munin-node to pick up the new plugin:
sudo /etc/init.d/munin-node restart
